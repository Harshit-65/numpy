"""
A small templating language

This implements a small templating language.  This language implements
if/elif/else, for/continue/break, expressions, and blocks of Python
code.  The syntax is::

  {{any expression (function calls etc)}}
  {{if predicate}}
    block
  {{elif predicate}}
    block
  {{else}}
    block
  {{endif}}

  {{for x in y}}
    block
  {{endfor}}

  {{py:
  any Python code
  }}

You use this with the ``Template`` class or the ``sub`` shortcut.
The ``Template`` class takes the template string and the name of
the template (for errors) and a default namespace.  Then (like
``string.Template``) you can call the ``tmpl.substitute(**kw)``
method to make a substitution (or ``tmpl.substitute(a_dict)``).

``sub(content, **kw)`` substitutes the template immediately.  You
can use ``__name='tmpl.html'`` to set the name of the template.

If there are syntax errors ``TemplateError`` will be raised.
"""

import re
import sys
import ast
from urllib.parse import quote as url_quote
import os
import tokenize
from io import StringIO

__all__ = ['TemplateError', 'Template', 'sub', 'HTMLTemplate',
           'sub_html', 'html', 'bunch']

in_re = re.compile(r'\s+in\s+')
var_re = re.compile(r'^[a-z_][a-z0-9_]*$', re.I)


class TemplateError(Exception):
    """Exception raised while parsing a template
    """

    def __init__(self, message, position, name=None):
        self.message = message
        self.position = position
        self.name = name

    def __str__(self):
        msg = '%s at line %s column %s' % (
            self.message, self.position[0], self.position[1])
        if self.name:
            msg += ' in %s' % self.name
        return msg


class _TemplateContinue(Exception):
    pass


class _TemplateBreak(Exception):
    pass


def get_file_template(name, from_template):
    path = os.path.join(os.path.dirname(from_template.name), name)
    return from_template.__class__.from_filename(
        path, namespace=from_template.namespace,
        get_template=from_template.get_template)


class Template:

    default_namespace = {
        'start_braces': '{{',
        'end_braces': '}}',
        'loremipsum': '''\
Lorem ipsum dolor sit amet, consectetuer adipiscing elit. Integer
euismod ante non diam. Sed eleifend odio sed quam. Sed vulputate,
turpis at tincidunt porttitor, est elit consequat metus, non dignissim augue
mauris quis arcu. Phasellus faucibus blandit eros. Curabitur porttitor ante
non est. Maecenas dolor. Aenean egestas sem. Class aptent taciti sociosqu
ad litora torquent per conubia nostra, per inceptos hymenaeos. Sed suscipit
eros nisi. Morbi vehicula hendrerit justo. Praesent vitae nulla et neque
venenatis pretium. Fusce rutrum tellus vitae libero. Vestibulum eget quam.
Pellentesque habitant morbi tristique senectus et netus et malesuada fames
ac turpis egestas. Aenean vel justo. Aliquam erat volutpat.''',
        'url_quote': url_quote,
        'get_file_template': get_file_template,
    }

    default_encoding = 'utf8'
    default_inherit = None

    def __init__(self, content, name=None, namespace=None, encoding=None,
                 get_template=None, inherit=None, line_offset=0, delimeters=None):
        self.content = content

        # set delimeters
        if delimeters is None:
            delimeters = ('{{', '}}')
        else:
            # we need to quote for regular expression
            delimeters = (re.escape(delimeters[0]), re.escape(delimeters[1]))
        self.delimeters = delimeters

        self.name = name
        if namespace is None:
            namespace = {}
        self.namespace = namespace
        if encoding is None:
            encoding = self.default_encoding
        self.encoding = encoding
        if get_template is None:
            get_template = self.default_get_template
        self.get_template = get_template
        if inherit is None:
            inherit = self.default_inherit
        self.inherit = inherit
        self.line_offset = line_offset
        self._parse()

    def from_filename(cls, filename, namespace=None, encoding=None,
                      get_template=None, inherit=None, line_offset=0,
                      delimeters=None):
        with open(filename, 'rb') as f:
            content = f.read()
        if encoding:
            content = content.decode(encoding)
        return cls(content=content, name=filename, namespace=namespace,
                   encoding=encoding, get_template=get_template,
                   inherit=inherit, line_offset=line_offset,
                   delimeters=delimeters)

    from_filename = classmethod(from_filename)

    def default_get_template(self, name):
        return self.__class__.from_filename(
            name, namespace=self.namespace,
            get_template=self.get_template)

    def __repr__(self):
        return '<%s %s name=%r>' % (
            self.__class__.__name__,
            hex(id(self))[2:], self.name)

    def substitute(self, *args, **kw):
        if args:
            if kw:
                raise TypeError(
                    "You can only give positional *or* keyword arguments")
            if len(args) > 1:
                raise TypeError(
                    "You can only give one positional argument")
            if not hasattr(args[0], 'items'):
                raise TypeError(
                    "If you pass in a single argument, it must be a dictionary "
                    "(not a %s)" % type(args[0]).__name__)
            kw = args[0]
        ns = self.namespace.copy()
        ns.update(kw)
        result, defs, inherit = self._interpret(ns)
        if not inherit:
            return result
        tmpl = self.get_template(inherit)
        for name, value in defs.items():
            ns[name] = value
        return tmpl.substitute(ns)

    def _parse(self):
        delimeters = self.delimeters
        in_expr = []
        source = []
        pos = 0
        content = self.content
        self._codes = []

        file_template_re = re.compile(
            r'^%s\s*inherit\s+([^\s]+)\s*%s' % delimeters)
        match = file_template_re.search(content)
        if match:
            self.inherit = match.group(1)
            self.content = content = content[match.end():]

        while 1:
            next_pos = content.find(delimeters[0], pos)
            if next_pos == -1:
                source.append(content[pos:])
                break
            source.append(content[pos:next_pos])
            pos = next_pos
            next_pos = content.find(delimeters[1], next_pos + len(delimeters[0]))
            if next_pos == -1:
                raise TemplateError(
                    'No closing braces (%s) for %s' % (delimeters[1], delimeters[0]),
                    (self.line_offset + 1, 1), self.name)
            if content[pos + len(delimeters[0])] == '!':
                # Comment
                source.append('')
                pos = next_pos + len(delimeters[1])
                continue
            expr = content[pos + len(delimeters[0]):next_pos]
            pos = next_pos + len(delimeters[1])
            if expr.startswith('py:'):
                expr = expr[3:].lstrip(' \t')
                self._codes.append(expr)
                source.append('\x01%s\x01' % (len(self._codes) - 1))
            elif expr.startswith('if '):
                expr = expr[3:].lstrip(' \t')
                in_expr.append('if')
                source.append('\x02(%s) if True:\n' % expr)
            elif expr.startswith('elif '):
                expr = expr[5:].lstrip(' \t')
                if not in_expr or in_expr[-1] != 'if':
                    raise TemplateError(
                        'elif outside of if block',
                        (self.line_offset + 1, 1), self.name)
                source.append('\x02elif (%s):\n' % expr)
            elif expr.startswith('else'):
                if not in_expr or in_expr[-1] != 'if':
                    raise TemplateError(
                        'else outside of if block',
                        (self.line_offset + 1, 1), self.name)
                source.append('\x02else:\n')
            elif expr.startswith('for '):
                expr = expr[4:].lstrip(' \t')
                if not in_re.search(expr):
                    raise TemplateError(
                        'Bad for loop; need the syntax: for var in expr',
                        (self.line_offset + 1, 1), self.name)
                in_expr.append('for')
                source.append('\x02for %s:\n' % expr)
            elif expr.startswith('py:continue'):
                if not in_expr or in_expr[-1] != 'for':
                    raise TemplateError(
                        'continue outside of for loop',
                        (self.line_offset + 1, 1), self.name)
                source.append('\x02raise _TemplateContinue\n')
            elif expr.startswith('py:break'):
                if not in_expr or in_expr[-1] != 'for':
                    raise TemplateError(
                        'break outside of for loop',
                        (self.line_offset + 1, 1), self.name)
                source.append('\x02raise _TemplateBreak\n')
            elif expr.startswith('endif') or expr.startswith('end if'):
                if not in_expr or in_expr[-1] != 'if':
                    raise TemplateError(
                        'Unexpected endif',
                        (self.line_offset + 1, 1), self.name)
                in_expr.pop()
                source.append('\x02\n')
            elif expr.startswith('endfor') or expr.startswith('end for'):
                if not in_expr or in_expr[-1] != 'for':
                    raise TemplateError(
                        'Unexpected endfor',
                        (self.line_offset + 1, 1), self.name)
                in_expr.pop()
                source.append('\x02\n')
            elif expr.startswith('#'):
                # Comment
                source.append('')
            else:
                source.append('\x03(%s)\x03' % expr)
        if in_expr:
            raise TemplateError(
                'You have an unclosed %s expression' % in_expr[-1],
                (self.line_offset + 1, 1), self.name)
        self._source = ''.join(source)

    def _interpret(self, ns):
        __traceback_hide__ = True
        source = self._source
        code_str = ''
        source_len = len(source)

        for i in range(source_len):
            if source[i] == '\x01':
                for j in range(i + 1, source_len):
                    if source[j] == '\x01':
                        code_str += '_str.append(%s)\n' % repr(source[i + 1:j])
                        i = j
                        break
                else:
                    assert 0, "Malformed template"
            elif source[i] == '\x02':
                for j in range(i + 1, source_len):
                    if source[j] == '\n':
                        code_str += source[i + 1:j + 1]
                        i = j
                        break
                else:
                    assert 0, "Malformed template"
            elif source[i] == '\x03':
                for j in range(i + 1, source_len):
                    if source[j] == '\x03':
                        code_str += '_str.append(str(%s))\n' % source[i + 1:j]
                        i = j
                        break
                else:
                    assert 0, "Malformed template"
            else:
                part = source[i]
                if i < source_len - 1:
                    if source[i] == '\\' and source[i + 1] == 'n':
                        part = '\n'
                        i += 1
                code_str += '_str.append(%s)\n' % repr(part)

        result = []
        defs = {}
        inherit = None

        def _str_append(string):
            result.append(string)

        def _inherit(template):
            nonlocal inherit
            inherit = template
            return ''

        def _def(name, func_content):
            defs[name] = func_content
            return ''

        # Create a restricted execution environment
        safe_globals = {
            '_str': result,
            '_str_append': _str_append,
            '_inherit': _inherit,
            '_def': _def,
            '_TemplateContinue': _TemplateContinue,
            '_TemplateBreak': _TemplateBreak,
            'str': str,
            'repr': repr,
            'len': len,
            'dict': dict,
            'list': list,
            'tuple': tuple,
            'int': int,
            'float': float,
            'bool': bool,
            'range': range,
            'zip': zip,
            'map': map,
            'filter': filter,
            'sorted': sorted,
            'enumerate': enumerate,
            'min': min,
            'max': max,
            'sum': sum,
            'abs': abs,
            'all': all,
            'any': any,
            'round': round,
            'divmod': divmod,
            'isinstance': isinstance,
            'issubclass': issubclass,
            'hasattr': hasattr,
            'getattr': getattr,
            'setattr': setattr,
            'delattr': delattr,
            'callable': callable,
            'pow': pow,
            'chr': chr,
            'ord': ord,
            'hex': hex,
            'oct': oct,
            'bin': bin,
            'None': None,
            'True': True,
            'False': False,
        }

        # Add namespace items to the safe globals
        for key, value in ns.items():
            if key not in safe_globals:
                safe_globals[key] = value

        # Execute the template code in the restricted environment
        try:
            # Compile the code
            compiled_code = compile(code_str, '<template>', 'exec')
            
            # Execute the code with restricted globals
            exec(compiled_code, safe_globals)
            
        except _TemplateContinue:
            pass
        except _TemplateBreak:
            pass
        except Exception as e:
            if hasattr(e, 'lineno') and hasattr(e, 'offset'):
                raise TemplateError(
                    str(e), (e.lineno + self.line_offset, e.offset),
                    self.name)
            else:
                raise

        return ''.join(result), defs, inherit


class bunch(dict):
    """
    A dictionary that also allows for attributes.
    """

    def __getattr__(self, name):
        try:
            return self[name]
        except KeyError:
            raise AttributeError(name)

    def __setattr__(self, name, value):
        self[name] = value


def sub(content, **kw):
    name = kw.pop('__name', None)
    tmpl = Template(content, name=name)
    return tmpl.substitute(kw)


def paste_script_template_renderer(content, vars, filename=None):
    tmpl = Template(content, name=filename)
    return tmpl.substitute(vars)


class HTMLTemplate(Template):

    default_namespace = Template.default_namespace.copy()
    default_namespace.update(dict(
        html_quote=html_quote,
        ))

    def _interpret(self, ns):
        ns.setdefault('html_quote', html_quote)
        return super(HTMLTemplate, self)._interpret(ns)


def sub_html(content, **kw):
    name = kw.pop('__name', None)
    tmpl = HTMLTemplate(content, name=name)
    return tmpl.substitute(kw)


def html(**kw):
    return bunch(kw)


def html_quote(value, force=True):
    if not force and isinstance(value, html):
        return value
    if value is None:
        return ''
    if not isinstance(value, str):
        value = str(value)
    value = (value.replace('&', '&amp;')
             .replace('<', '&lt;')
             .replace('>', '&gt;')
             .replace('"', '&quot;')
             .replace("'", '&#39;'))
    return value


def test():
    import doctest
    doctest.testmod()


if __name__ == '__main__':
    test()
