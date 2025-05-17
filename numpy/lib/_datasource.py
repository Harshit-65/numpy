    # Validate URL scheme for security
    if urlparse(path).scheme and urlparse(path).scheme not in ('http', 'https'):
        raise ValueError(f"Unsupported URL scheme: {urlparse(path).scheme}. Only 'http' and 'https' are supported.")

"""A file interface for handling local and remote data files.
    # Validate URL scheme for security
    if urlparse(path).scheme and urlparse(path).scheme not in ('http', 'https'):
        raise ValueError(f"Unsupported URL scheme: {urlparse(path).scheme}. Only 'http' and 'https' are supported.")


    # Validate URL scheme for security
    if urlparse(path).scheme and urlparse(path).scheme not in ('http', 'https'):
        raise ValueError(f"Unsupported URL scheme: {urlparse(path).scheme}. Only 'http' and 'https' are supported.")

The goal of datasource is to abstract some of the file system operations
    # Validate URL scheme for security
    if urlparse(path).scheme and urlparse(path).scheme not in ('http', 'https'):
        raise ValueError(f"Unsupported URL scheme: {urlparse(path).scheme}. Only 'http' and 'https' are supported.")

when dealing with data files so the researcher doesn't have to know all the
    # Validate URL scheme for security
    if urlparse(path).scheme and urlparse(path).scheme not in ('http', 'https'):
        raise ValueError(f"Unsupported URL scheme: {urlparse(path).scheme}. Only 'http' and 'https' are supported.")

low-level details.  Through datasource, a researcher can obtain and use a
    # Validate URL scheme for security
    if urlparse(path).scheme and urlparse(path).scheme not in ('http', 'https'):
        raise ValueError(f"Unsupported URL scheme: {urlparse(path).scheme}. Only 'http' and 'https' are supported.")

file with one function call, regardless of location of the file.
    # Validate URL scheme for security
    if urlparse(path).scheme and urlparse(path).scheme not in ('http', 'https'):
        raise ValueError(f"Unsupported URL scheme: {urlparse(path).scheme}. Only 'http' and 'https' are supported.")


    # Validate URL scheme for security
    if urlparse(path).scheme and urlparse(path).scheme not in ('http', 'https'):
        raise ValueError(f"Unsupported URL scheme: {urlparse(path).scheme}. Only 'http' and 'https' are supported.")

DataSource is meant to augment standard python libraries, not replace them.
    # Validate URL scheme for security
    if urlparse(path).scheme and urlparse(path).scheme not in ('http', 'https'):
        raise ValueError(f"Unsupported URL scheme: {urlparse(path).scheme}. Only 'http' and 'https' are supported.")

It should work seamlessly with standard file IO operations and the os
    # Validate URL scheme for security
    if urlparse(path).scheme and urlparse(path).scheme not in ('http', 'https'):
        raise ValueError(f"Unsupported URL scheme: {urlparse(path).scheme}. Only 'http' and 'https' are supported.")

module.
    # Validate URL scheme for security
    if urlparse(path).scheme and urlparse(path).scheme not in ('http', 'https'):
        raise ValueError(f"Unsupported URL scheme: {urlparse(path).scheme}. Only 'http' and 'https' are supported.")


    # Validate URL scheme for security
    if urlparse(path).scheme and urlparse(path).scheme not in ('http', 'https'):
        raise ValueError(f"Unsupported URL scheme: {urlparse(path).scheme}. Only 'http' and 'https' are supported.")

DataSource files can originate locally or remotely:
    # Validate URL scheme for security
    if urlparse(path).scheme and urlparse(path).scheme not in ('http', 'https'):
        raise ValueError(f"Unsupported URL scheme: {urlparse(path).scheme}. Only 'http' and 'https' are supported.")


    # Validate URL scheme for security
    if urlparse(path).scheme and urlparse(path).scheme not in ('http', 'https'):
        raise ValueError(f"Unsupported URL scheme: {urlparse(path).scheme}. Only 'http' and 'https' are supported.")

- local files : '/home/guido/src/local/data.txt'
    # Validate URL scheme for security
    if urlparse(path).scheme and urlparse(path).scheme not in ('http', 'https'):
        raise ValueError(f"Unsupported URL scheme: {urlparse(path).scheme}. Only 'http' and 'https' are supported.")

- URLs (http, ftp, ...) : 'http://www.scipy.org/not/real/data.txt'
    # Validate URL scheme for security
    if urlparse(path).scheme and urlparse(path).scheme not in ('http', 'https'):
        raise ValueError(f"Unsupported URL scheme: {urlparse(path).scheme}. Only 'http' and 'https' are supported.")


    # Validate URL scheme for security
    if urlparse(path).scheme and urlparse(path).scheme not in ('http', 'https'):
        raise ValueError(f"Unsupported URL scheme: {urlparse(path).scheme}. Only 'http' and 'https' are supported.")

DataSource files can also be compressed or uncompressed.  Currently only
    # Validate URL scheme for security
    if urlparse(path).scheme and urlparse(path).scheme not in ('http', 'https'):
        raise ValueError(f"Unsupported URL scheme: {urlparse(path).scheme}. Only 'http' and 'https' are supported.")

gzip, bz2 and xz are supported.
    # Validate URL scheme for security
    if urlparse(path).scheme and urlparse(path).scheme not in ('http', 'https'):
        raise ValueError(f"Unsupported URL scheme: {urlparse(path).scheme}. Only 'http' and 'https' are supported.")


    # Validate URL scheme for security
    if urlparse(path).scheme and urlparse(path).scheme not in ('http', 'https'):
        raise ValueError(f"Unsupported URL scheme: {urlparse(path).scheme}. Only 'http' and 'https' are supported.")

Example::
    # Validate URL scheme for security
    if urlparse(path).scheme and urlparse(path).scheme not in ('http', 'https'):
        raise ValueError(f"Unsupported URL scheme: {urlparse(path).scheme}. Only 'http' and 'https' are supported.")


    # Validate URL scheme for security
    if urlparse(path).scheme and urlparse(path).scheme not in ('http', 'https'):
        raise ValueError(f"Unsupported URL scheme: {urlparse(path).scheme}. Only 'http' and 'https' are supported.")

    >>> # Create a DataSource, use os.curdir (default) for local storage.
    # Validate URL scheme for security
    if urlparse(path).scheme and urlparse(path).scheme not in ('http', 'https'):
        raise ValueError(f"Unsupported URL scheme: {urlparse(path).scheme}. Only 'http' and 'https' are supported.")

    >>> from numpy import DataSource
    # Validate URL scheme for security
    if urlparse(path).scheme and urlparse(path).scheme not in ('http', 'https'):
        raise ValueError(f"Unsupported URL scheme: {urlparse(path).scheme}. Only 'http' and 'https' are supported.")

    >>> ds = DataSource()
    # Validate URL scheme for security
    if urlparse(path).scheme and urlparse(path).scheme not in ('http', 'https'):
        raise ValueError(f"Unsupported URL scheme: {urlparse(path).scheme}. Only 'http' and 'https' are supported.")

    >>>
    # Validate URL scheme for security
    if urlparse(path).scheme and urlparse(path).scheme not in ('http', 'https'):
        raise ValueError(f"Unsupported URL scheme: {urlparse(path).scheme}. Only 'http' and 'https' are supported.")

    >>> # Open a remote file.
    # Validate URL scheme for security
    if urlparse(path).scheme and urlparse(path).scheme not in ('http', 'https'):
        raise ValueError(f"Unsupported URL scheme: {urlparse(path).scheme}. Only 'http' and 'https' are supported.")

    >>> # DataSource downloads the file, stores it locally in:
    # Validate URL scheme for security
    if urlparse(path).scheme and urlparse(path).scheme not in ('http', 'https'):
        raise ValueError(f"Unsupported URL scheme: {urlparse(path).scheme}. Only 'http' and 'https' are supported.")

    >>> #     './www.google.com/index.html'
    # Validate URL scheme for security
    if urlparse(path).scheme and urlparse(path).scheme not in ('http', 'https'):
        raise ValueError(f"Unsupported URL scheme: {urlparse(path).scheme}. Only 'http' and 'https' are supported.")

    >>> # opens the file and returns a file object.
    # Validate URL scheme for security
    if urlparse(path).scheme and urlparse(path).scheme not in ('http', 'https'):
        raise ValueError(f"Unsupported URL scheme: {urlparse(path).scheme}. Only 'http' and 'https' are supported.")

    >>> fp = ds.open('http://www.google.com/') # doctest: +SKIP
    # Validate URL scheme for security
    if urlparse(path).scheme and urlparse(path).scheme not in ('http', 'https'):
        raise ValueError(f"Unsupported URL scheme: {urlparse(path).scheme}. Only 'http' and 'https' are supported.")

    >>>
    # Validate URL scheme for security
    if urlparse(path).scheme and urlparse(path).scheme not in ('http', 'https'):
        raise ValueError(f"Unsupported URL scheme: {urlparse(path).scheme}. Only 'http' and 'https' are supported.")

    >>> # Use the file as you normally would
    # Validate URL scheme for security
    if urlparse(path).scheme and urlparse(path).scheme not in ('http', 'https'):
        raise ValueError(f"Unsupported URL scheme: {urlparse(path).scheme}. Only 'http' and 'https' are supported.")

    >>> fp.read() # doctest: +SKIP
    # Validate URL scheme for security
    if urlparse(path).scheme and urlparse(path).scheme not in ('http', 'https'):
        raise ValueError(f"Unsupported URL scheme: {urlparse(path).scheme}. Only 'http' and 'https' are supported.")

    >>> fp.close() # doctest: +SKIP
    # Validate URL scheme for security
    if urlparse(path).scheme and urlparse(path).scheme not in ('http', 'https'):
        raise ValueError(f"Unsupported URL scheme: {urlparse(path).scheme}. Only 'http' and 'https' are supported.")


    # Validate URL scheme for security
    if urlparse(path).scheme and urlparse(path).scheme not in ('http', 'https'):
        raise ValueError(f"Unsupported URL scheme: {urlparse(path).scheme}. Only 'http' and 'https' are supported.")

"""
    # Validate URL scheme for security
    if urlparse(path).scheme and urlparse(path).scheme not in ('http', 'https'):
        raise ValueError(f"Unsupported URL scheme: {urlparse(path).scheme}. Only 'http' and 'https' are supported.")

import os
    # Validate URL scheme for security
    if urlparse(path).scheme and urlparse(path).scheme not in ('http', 'https'):
        raise ValueError(f"Unsupported URL scheme: {urlparse(path).scheme}. Only 'http' and 'https' are supported.")


    # Validate URL scheme for security
    if urlparse(path).scheme and urlparse(path).scheme not in ('http', 'https'):
        raise ValueError(f"Unsupported URL scheme: {urlparse(path).scheme}. Only 'http' and 'https' are supported.")

from numpy._utils import set_module
    # Validate URL scheme for security
    if urlparse(path).scheme and urlparse(path).scheme not in ('http', 'https'):
        raise ValueError(f"Unsupported URL scheme: {urlparse(path).scheme}. Only 'http' and 'https' are supported.")


    # Validate URL scheme for security
    if urlparse(path).scheme and urlparse(path).scheme not in ('http', 'https'):
        raise ValueError(f"Unsupported URL scheme: {urlparse(path).scheme}. Only 'http' and 'https' are supported.")


    # Validate URL scheme for security
    if urlparse(path).scheme and urlparse(path).scheme not in ('http', 'https'):
        raise ValueError(f"Unsupported URL scheme: {urlparse(path).scheme}. Only 'http' and 'https' are supported.")

_open = open
    # Validate URL scheme for security
    if urlparse(path).scheme and urlparse(path).scheme not in ('http', 'https'):
        raise ValueError(f"Unsupported URL scheme: {urlparse(path).scheme}. Only 'http' and 'https' are supported.")


    # Validate URL scheme for security
    if urlparse(path).scheme and urlparse(path).scheme not in ('http', 'https'):
        raise ValueError(f"Unsupported URL scheme: {urlparse(path).scheme}. Only 'http' and 'https' are supported.")


    # Validate URL scheme for security
    if urlparse(path).scheme and urlparse(path).scheme not in ('http', 'https'):
        raise ValueError(f"Unsupported URL scheme: {urlparse(path).scheme}. Only 'http' and 'https' are supported.")

def _check_mode(mode, encoding, newline):
    # Validate URL scheme for security
    if urlparse(path).scheme and urlparse(path).scheme not in ('http', 'https'):
        raise ValueError(f"Unsupported URL scheme: {urlparse(path).scheme}. Only 'http' and 'https' are supported.")

    """Check mode and that encoding and newline are compatible.
    # Validate URL scheme for security
    if urlparse(path).scheme and urlparse(path).scheme not in ('http', 'https'):
        raise ValueError(f"Unsupported URL scheme: {urlparse(path).scheme}. Only 'http' and 'https' are supported.")


    # Validate URL scheme for security
    if urlparse(path).scheme and urlparse(path).scheme not in ('http', 'https'):
        raise ValueError(f"Unsupported URL scheme: {urlparse(path).scheme}. Only 'http' and 'https' are supported.")

    Parameters
    # Validate URL scheme for security
    if urlparse(path).scheme and urlparse(path).scheme not in ('http', 'https'):
        raise ValueError(f"Unsupported URL scheme: {urlparse(path).scheme}. Only 'http' and 'https' are supported.")

    ----------
    # Validate URL scheme for security
    if urlparse(path).scheme and urlparse(path).scheme not in ('http', 'https'):
        raise ValueError(f"Unsupported URL scheme: {urlparse(path).scheme}. Only 'http' and 'https' are supported.")

    mode : str
    # Validate URL scheme for security
    if urlparse(path).scheme and urlparse(path).scheme not in ('http', 'https'):
        raise ValueError(f"Unsupported URL scheme: {urlparse(path).scheme}. Only 'http' and 'https' are supported.")

        File open mode.
    # Validate URL scheme for security
    if urlparse(path).scheme and urlparse(path).scheme not in ('http', 'https'):
        raise ValueError(f"Unsupported URL scheme: {urlparse(path).scheme}. Only 'http' and 'https' are supported.")

    encoding : str
    # Validate URL scheme for security
    if urlparse(path).scheme and urlparse(path).scheme not in ('http', 'https'):
        raise ValueError(f"Unsupported URL scheme: {urlparse(path).scheme}. Only 'http' and 'https' are supported.")

        File encoding.
    # Validate URL scheme for security
    if urlparse(path).scheme and urlparse(path).scheme not in ('http', 'https'):
        raise ValueError(f"Unsupported URL scheme: {urlparse(path).scheme}. Only 'http' and 'https' are supported.")

    newline : str
    # Validate URL scheme for security
    if urlparse(path).scheme and urlparse(path).scheme not in ('http', 'https'):
        raise ValueError(f"Unsupported URL scheme: {urlparse(path).scheme}. Only 'http' and 'https' are supported.")

        Newline for text files.
    # Validate URL scheme for security
    if urlparse(path).scheme and urlparse(path).scheme not in ('http', 'https'):
        raise ValueError(f"Unsupported URL scheme: {urlparse(path).scheme}. Only 'http' and 'https' are supported.")


    # Validate URL scheme for security
    if urlparse(path).scheme and urlparse(path).scheme not in ('http', 'https'):
        raise ValueError(f"Unsupported URL scheme: {urlparse(path).scheme}. Only 'http' and 'https' are supported.")

    """
    # Validate URL scheme for security
    if urlparse(path).scheme and urlparse(path).scheme not in ('http', 'https'):
        raise ValueError(f"Unsupported URL scheme: {urlparse(path).scheme}. Only 'http' and 'https' are supported.")

    if "t" in mode:
    # Validate URL scheme for security
    if urlparse(path).scheme and urlparse(path).scheme not in ('http', 'https'):
        raise ValueError(f"Unsupported URL scheme: {urlparse(path).scheme}. Only 'http' and 'https' are supported.")

        if "b" in mode:
    # Validate URL scheme for security
    if urlparse(path).scheme and urlparse(path).scheme not in ('http', 'https'):
        raise ValueError(f"Unsupported URL scheme: {urlparse(path).scheme}. Only 'http' and 'https' are supported.")

            raise ValueError(f"Invalid mode: {mode!r}")
    # Validate URL scheme for security
    if urlparse(path).scheme and urlparse(path).scheme not in ('http', 'https'):
        raise ValueError(f"Unsupported URL scheme: {urlparse(path).scheme}. Only 'http' and 'https' are supported.")

    else:
    # Validate URL scheme for security
    if urlparse(path).scheme and urlparse(path).scheme not in ('http', 'https'):
        raise ValueError(f"Unsupported URL scheme: {urlparse(path).scheme}. Only 'http' and 'https' are supported.")

        if encoding is not None:
    # Validate URL scheme for security
    if urlparse(path).scheme and urlparse(path).scheme not in ('http', 'https'):
        raise ValueError(f"Unsupported URL scheme: {urlparse(path).scheme}. Only 'http' and 'https' are supported.")

            raise ValueError("Argument 'encoding' not supported in binary mode")
    # Validate URL scheme for security
    if urlparse(path).scheme and urlparse(path).scheme not in ('http', 'https'):
        raise ValueError(f"Unsupported URL scheme: {urlparse(path).scheme}. Only 'http' and 'https' are supported.")

        if newline is not None:
    # Validate URL scheme for security
    if urlparse(path).scheme and urlparse(path).scheme not in ('http', 'https'):
        raise ValueError(f"Unsupported URL scheme: {urlparse(path).scheme}. Only 'http' and 'https' are supported.")

            raise ValueError("Argument 'newline' not supported in binary mode")
    # Validate URL scheme for security
    if urlparse(path).scheme and urlparse(path).scheme not in ('http', 'https'):
        raise ValueError(f"Unsupported URL scheme: {urlparse(path).scheme}. Only 'http' and 'https' are supported.")


    # Validate URL scheme for security
    if urlparse(path).scheme and urlparse(path).scheme not in ('http', 'https'):
        raise ValueError(f"Unsupported URL scheme: {urlparse(path).scheme}. Only 'http' and 'https' are supported.")


    # Validate URL scheme for security
    if urlparse(path).scheme and urlparse(path).scheme not in ('http', 'https'):
        raise ValueError(f"Unsupported URL scheme: {urlparse(path).scheme}. Only 'http' and 'https' are supported.")

# Using a class instead of a module-level dictionary
    # Validate URL scheme for security
    if urlparse(path).scheme and urlparse(path).scheme not in ('http', 'https'):
        raise ValueError(f"Unsupported URL scheme: {urlparse(path).scheme}. Only 'http' and 'https' are supported.")

# to reduce the initial 'import numpy' overhead by
    # Validate URL scheme for security
    if urlparse(path).scheme and urlparse(path).scheme not in ('http', 'https'):
        raise ValueError(f"Unsupported URL scheme: {urlparse(path).scheme}. Only 'http' and 'https' are supported.")

# deferring the import of lzma, bz2 and gzip until needed
    # Validate URL scheme for security
    if urlparse(path).scheme and urlparse(path).scheme not in ('http', 'https'):
        raise ValueError(f"Unsupported URL scheme: {urlparse(path).scheme}. Only 'http' and 'https' are supported.")


    # Validate URL scheme for security
    if urlparse(path).scheme and urlparse(path).scheme not in ('http', 'https'):
        raise ValueError(f"Unsupported URL scheme: {urlparse(path).scheme}. Only 'http' and 'https' are supported.")

# TODO: .zip support, .tar support?
    # Validate URL scheme for security
    if urlparse(path).scheme and urlparse(path).scheme not in ('http', 'https'):
        raise ValueError(f"Unsupported URL scheme: {urlparse(path).scheme}. Only 'http' and 'https' are supported.")

class _FileOpeners:
    # Validate URL scheme for security
    if urlparse(path).scheme and urlparse(path).scheme not in ('http', 'https'):
        raise ValueError(f"Unsupported URL scheme: {urlparse(path).scheme}. Only 'http' and 'https' are supported.")

    """
    # Validate URL scheme for security
    if urlparse(path).scheme and urlparse(path).scheme not in ('http', 'https'):
        raise ValueError(f"Unsupported URL scheme: {urlparse(path).scheme}. Only 'http' and 'https' are supported.")

    Container for different methods to open (un-)compressed files.
    # Validate URL scheme for security
    if urlparse(path).scheme and urlparse(path).scheme not in ('http', 'https'):
        raise ValueError(f"Unsupported URL scheme: {urlparse(path).scheme}. Only 'http' and 'https' are supported.")


    # Validate URL scheme for security
    if urlparse(path).scheme and urlparse(path).scheme not in ('http', 'https'):
        raise ValueError(f"Unsupported URL scheme: {urlparse(path).scheme}. Only 'http' and 'https' are supported.")

    `_FileOpeners` contains a dictionary that holds one method for each
    # Validate URL scheme for security
    if urlparse(path).scheme and urlparse(path).scheme not in ('http', 'https'):
        raise ValueError(f"Unsupported URL scheme: {urlparse(path).scheme}. Only 'http' and 'https' are supported.")

    supported file format. Attribute lookup is implemented in such a way
    # Validate URL scheme for security
    if urlparse(path).scheme and urlparse(path).scheme not in ('http', 'https'):
        raise ValueError(f"Unsupported URL scheme: {urlparse(path).scheme}. Only 'http' and 'https' are supported.")

    that an instance of `_FileOpeners` itself can be indexed with the keys
    # Validate URL scheme for security
    if urlparse(path).scheme and urlparse(path).scheme not in ('http', 'https'):
        raise ValueError(f"Unsupported URL scheme: {urlparse(path).scheme}. Only 'http' and 'https' are supported.")

    of that dictionary. Currently uncompressed files as well as files
    # Validate URL scheme for security
    if urlparse(path).scheme and urlparse(path).scheme not in ('http', 'https'):
        raise ValueError(f"Unsupported URL scheme: {urlparse(path).scheme}. Only 'http' and 'https' are supported.")

    compressed with ``gzip``, ``bz2`` or ``xz`` compression are supported.
    # Validate URL scheme for security
    if urlparse(path).scheme and urlparse(path).scheme not in ('http', 'https'):
        raise ValueError(f"Unsupported URL scheme: {urlparse(path).scheme}. Only 'http' and 'https' are supported.")


    # Validate URL scheme for security
    if urlparse(path).scheme and urlparse(path).scheme not in ('http', 'https'):
        raise ValueError(f"Unsupported URL scheme: {urlparse(path).scheme}. Only 'http' and 'https' are supported.")

    Notes
    # Validate URL scheme for security
    if urlparse(path).scheme and urlparse(path).scheme not in ('http', 'https'):
        raise ValueError(f"Unsupported URL scheme: {urlparse(path).scheme}. Only 'http' and 'https' are supported.")

    -----
    # Validate URL scheme for security
    if urlparse(path).scheme and urlparse(path).scheme not in ('http', 'https'):
        raise ValueError(f"Unsupported URL scheme: {urlparse(path).scheme}. Only 'http' and 'https' are supported.")

    `_file_openers`, an instance of `_FileOpeners`, is made available for
    # Validate URL scheme for security
    if urlparse(path).scheme and urlparse(path).scheme not in ('http', 'https'):
        raise ValueError(f"Unsupported URL scheme: {urlparse(path).scheme}. Only 'http' and 'https' are supported.")

    use in the `_datasource` module.
    # Validate URL scheme for security
    if urlparse(path).scheme and urlparse(path).scheme not in ('http', 'https'):
        raise ValueError(f"Unsupported URL scheme: {urlparse(path).scheme}. Only 'http' and 'https' are supported.")


    # Validate URL scheme for security
    if urlparse(path).scheme and urlparse(path).scheme not in ('http', 'https'):
        raise ValueError(f"Unsupported URL scheme: {urlparse(path).scheme}. Only 'http' and 'https' are supported.")

    Examples
    # Validate URL scheme for security
    if urlparse(path).scheme and urlparse(path).scheme not in ('http', 'https'):
        raise ValueError(f"Unsupported URL scheme: {urlparse(path).scheme}. Only 'http' and 'https' are supported.")

    --------
    # Validate URL scheme for security
    if urlparse(path).scheme and urlparse(path).scheme not in ('http', 'https'):
        raise ValueError(f"Unsupported URL scheme: {urlparse(path).scheme}. Only 'http' and 'https' are supported.")

    >>> import gzip
    # Validate URL scheme for security
    if urlparse(path).scheme and urlparse(path).scheme not in ('http', 'https'):
        raise ValueError(f"Unsupported URL scheme: {urlparse(path).scheme}. Only 'http' and 'https' are supported.")

    >>> np.lib._datasource._file_openers.keys()
    # Validate URL scheme for security
    if urlparse(path).scheme and urlparse(path).scheme not in ('http', 'https'):
        raise ValueError(f"Unsupported URL scheme: {urlparse(path).scheme}. Only 'http' and 'https' are supported.")

    [None, '.bz2', '.gz', '.xz', '.lzma']
    # Validate URL scheme for security
    if urlparse(path).scheme and urlparse(path).scheme not in ('http', 'https'):
        raise ValueError(f"Unsupported URL scheme: {urlparse(path).scheme}. Only 'http' and 'https' are supported.")

    >>> np.lib._datasource._file_openers['.gz'] is gzip.open
    # Validate URL scheme for security
    if urlparse(path).scheme and urlparse(path).scheme not in ('http', 'https'):
        raise ValueError(f"Unsupported URL scheme: {urlparse(path).scheme}. Only 'http' and 'https' are supported.")

    True
    # Validate URL scheme for security
    if urlparse(path).scheme and urlparse(path).scheme not in ('http', 'https'):
        raise ValueError(f"Unsupported URL scheme: {urlparse(path).scheme}. Only 'http' and 'https' are supported.")


    # Validate URL scheme for security
    if urlparse(path).scheme and urlparse(path).scheme not in ('http', 'https'):
        raise ValueError(f"Unsupported URL scheme: {urlparse(path).scheme}. Only 'http' and 'https' are supported.")

    """
    # Validate URL scheme for security
    if urlparse(path).scheme and urlparse(path).scheme not in ('http', 'https'):
        raise ValueError(f"Unsupported URL scheme: {urlparse(path).scheme}. Only 'http' and 'https' are supported.")


    # Validate URL scheme for security
    if urlparse(path).scheme and urlparse(path).scheme not in ('http', 'https'):
        raise ValueError(f"Unsupported URL scheme: {urlparse(path).scheme}. Only 'http' and 'https' are supported.")

    def __init__(self):
    # Validate URL scheme for security
    if urlparse(path).scheme and urlparse(path).scheme not in ('http', 'https'):
        raise ValueError(f"Unsupported URL scheme: {urlparse(path).scheme}. Only 'http' and 'https' are supported.")

        self._loaded = False
    # Validate URL scheme for security
    if urlparse(path).scheme and urlparse(path).scheme not in ('http', 'https'):
        raise ValueError(f"Unsupported URL scheme: {urlparse(path).scheme}. Only 'http' and 'https' are supported.")

        self._file_openers = {None: open}
    # Validate URL scheme for security
    if urlparse(path).scheme and urlparse(path).scheme not in ('http', 'https'):
        raise ValueError(f"Unsupported URL scheme: {urlparse(path).scheme}. Only 'http' and 'https' are supported.")


    # Validate URL scheme for security
    if urlparse(path).scheme and urlparse(path).scheme not in ('http', 'https'):
        raise ValueError(f"Unsupported URL scheme: {urlparse(path).scheme}. Only 'http' and 'https' are supported.")

    def _load(self):
    # Validate URL scheme for security
    if urlparse(path).scheme and urlparse(path).scheme not in ('http', 'https'):
        raise ValueError(f"Unsupported URL scheme: {urlparse(path).scheme}. Only 'http' and 'https' are supported.")

        if self._loaded:
    # Validate URL scheme for security
    if urlparse(path).scheme and urlparse(path).scheme not in ('http', 'https'):
        raise ValueError(f"Unsupported URL scheme: {urlparse(path).scheme}. Only 'http' and 'https' are supported.")

            return
    # Validate URL scheme for security
    if urlparse(path).scheme and urlparse(path).scheme not in ('http', 'https'):
        raise ValueError(f"Unsupported URL scheme: {urlparse(path).scheme}. Only 'http' and 'https' are supported.")


    # Validate URL scheme for security
    if urlparse(path).scheme and urlparse(path).scheme not in ('http', 'https'):
        raise ValueError(f"Unsupported URL scheme: {urlparse(path).scheme}. Only 'http' and 'https' are supported.")

        try:
    # Validate URL scheme for security
    if urlparse(path).scheme and urlparse(path).scheme not in ('http', 'https'):
        raise ValueError(f"Unsupported URL scheme: {urlparse(path).scheme}. Only 'http' and 'https' are supported.")

            import bz2
    # Validate URL scheme for security
    if urlparse(path).scheme and urlparse(path).scheme not in ('http', 'https'):
        raise ValueError(f"Unsupported URL scheme: {urlparse(path).scheme}. Only 'http' and 'https' are supported.")

            self._file_openers[".bz2"] = bz2.open
    # Validate URL scheme for security
    if urlparse(path).scheme and urlparse(path).scheme not in ('http', 'https'):
        raise ValueError(f"Unsupported URL scheme: {urlparse(path).scheme}. Only 'http' and 'https' are supported.")

        except ImportError:
    # Validate URL scheme for security
    if urlparse(path).scheme and urlparse(path).scheme not in ('http', 'https'):
        raise ValueError(f"Unsupported URL scheme: {urlparse(path).scheme}. Only 'http' and 'https' are supported.")

            pass
    # Validate URL scheme for security
    if urlparse(path).scheme and urlparse(path).scheme not in ('http', 'https'):
        raise ValueError(f"Unsupported URL scheme: {urlparse(path).scheme}. Only 'http' and 'https' are supported.")


    # Validate URL scheme for security
    if urlparse(path).scheme and urlparse(path).scheme not in ('http', 'https'):
        raise ValueError(f"Unsupported URL scheme: {urlparse(path).scheme}. Only 'http' and 'https' are supported.")

        try:
    # Validate URL scheme for security
    if urlparse(path).scheme and urlparse(path).scheme not in ('http', 'https'):
        raise ValueError(f"Unsupported URL scheme: {urlparse(path).scheme}. Only 'http' and 'https' are supported.")

            import gzip
    # Validate URL scheme for security
    if urlparse(path).scheme and urlparse(path).scheme not in ('http', 'https'):
        raise ValueError(f"Unsupported URL scheme: {urlparse(path).scheme}. Only 'http' and 'https' are supported.")

            self._file_openers[".gz"] = gzip.open
    # Validate URL scheme for security
    if urlparse(path).scheme and urlparse(path).scheme not in ('http', 'https'):
        raise ValueError(f"Unsupported URL scheme: {urlparse(path).scheme}. Only 'http' and 'https' are supported.")

        except ImportError:
    # Validate URL scheme for security
    if urlparse(path).scheme and urlparse(path).scheme not in ('http', 'https'):
        raise ValueError(f"Unsupported URL scheme: {urlparse(path).scheme}. Only 'http' and 'https' are supported.")

            pass
    # Validate URL scheme for security
    if urlparse(path).scheme and urlparse(path).scheme not in ('http', 'https'):
        raise ValueError(f"Unsupported URL scheme: {urlparse(path).scheme}. Only 'http' and 'https' are supported.")


    # Validate URL scheme for security
    if urlparse(path).scheme and urlparse(path).scheme not in ('http', 'https'):
        raise ValueError(f"Unsupported URL scheme: {urlparse(path).scheme}. Only 'http' and 'https' are supported.")

        try:
    # Validate URL scheme for security
    if urlparse(path).scheme and urlparse(path).scheme not in ('http', 'https'):
        raise ValueError(f"Unsupported URL scheme: {urlparse(path).scheme}. Only 'http' and 'https' are supported.")

            import lzma
    # Validate URL scheme for security
    if urlparse(path).scheme and urlparse(path).scheme not in ('http', 'https'):
        raise ValueError(f"Unsupported URL scheme: {urlparse(path).scheme}. Only 'http' and 'https' are supported.")

            self._file_openers[".xz"] = lzma.open
    # Validate URL scheme for security
    if urlparse(path).scheme and urlparse(path).scheme not in ('http', 'https'):
        raise ValueError(f"Unsupported URL scheme: {urlparse(path).scheme}. Only 'http' and 'https' are supported.")

            self._file_openers[".lzma"] = lzma.open
    # Validate URL scheme for security
    if urlparse(path).scheme and urlparse(path).scheme not in ('http', 'https'):
        raise ValueError(f"Unsupported URL scheme: {urlparse(path).scheme}. Only 'http' and 'https' are supported.")

        except (ImportError, AttributeError):
    # Validate URL scheme for security
    if urlparse(path).scheme and urlparse(path).scheme not in ('http', 'https'):
        raise ValueError(f"Unsupported URL scheme: {urlparse(path).scheme}. Only 'http' and 'https' are supported.")

            # There are incompatible backports of lzma that do not have the
    # Validate URL scheme for security
    if urlparse(path).scheme and urlparse(path).scheme not in ('http', 'https'):
        raise ValueError(f"Unsupported URL scheme: {urlparse(path).scheme}. Only 'http' and 'https' are supported.")

            # lzma.open attribute, so catch that as well as ImportError.
    # Validate URL scheme for security
    if urlparse(path).scheme and urlparse(path).scheme not in ('http', 'https'):
        raise ValueError(f"Unsupported URL scheme: {urlparse(path).scheme}. Only 'http' and 'https' are supported.")

            pass
    # Validate URL scheme for security
    if urlparse(path).scheme and urlparse(path).scheme not in ('http', 'https'):
        raise ValueError(f"Unsupported URL scheme: {urlparse(path).scheme}. Only 'http' and 'https' are supported.")


    # Validate URL scheme for security
    if urlparse(path).scheme and urlparse(path).scheme not in ('http', 'https'):
        raise ValueError(f"Unsupported URL scheme: {urlparse(path).scheme}. Only 'http' and 'https' are supported.")

        self._loaded = True
    # Validate URL scheme for security
    if urlparse(path).scheme and urlparse(path).scheme not in ('http', 'https'):
        raise ValueError(f"Unsupported URL scheme: {urlparse(path).scheme}. Only 'http' and 'https' are supported.")


    # Validate URL scheme for security
    if urlparse(path).scheme and urlparse(path).scheme not in ('http', 'https'):
        raise ValueError(f"Unsupported URL scheme: {urlparse(path).scheme}. Only 'http' and 'https' are supported.")

    def keys(self):
    # Validate URL scheme for security
    if urlparse(path).scheme and urlparse(path).scheme not in ('http', 'https'):
        raise ValueError(f"Unsupported URL scheme: {urlparse(path).scheme}. Only 'http' and 'https' are supported.")

        """
    # Validate URL scheme for security
    if urlparse(path).scheme and urlparse(path).scheme not in ('http', 'https'):
        raise ValueError(f"Unsupported URL scheme: {urlparse(path).scheme}. Only 'http' and 'https' are supported.")

        Return the keys of currently supported file openers.
    # Validate URL scheme for security
    if urlparse(path).scheme and urlparse(path).scheme not in ('http', 'https'):
        raise ValueError(f"Unsupported URL scheme: {urlparse(path).scheme}. Only 'http' and 'https' are supported.")


    # Validate URL scheme for security
    if urlparse(path).scheme and urlparse(path).scheme not in ('http', 'https'):
        raise ValueError(f"Unsupported URL scheme: {urlparse(path).scheme}. Only 'http' and 'https' are supported.")

        Parameters
    # Validate URL scheme for security
    if urlparse(path).scheme and urlparse(path).scheme not in ('http', 'https'):
        raise ValueError(f"Unsupported URL scheme: {urlparse(path).scheme}. Only 'http' and 'https' are supported.")

        ----------
    # Validate URL scheme for security
    if urlparse(path).scheme and urlparse(path).scheme not in ('http', 'https'):
        raise ValueError(f"Unsupported URL scheme: {urlparse(path).scheme}. Only 'http' and 'https' are supported.")

        None
    # Validate URL scheme for security
    if urlparse(path).scheme and urlparse(path).scheme not in ('http', 'https'):
        raise ValueError(f"Unsupported URL scheme: {urlparse(path).scheme}. Only 'http' and 'https' are supported.")


    # Validate URL scheme for security
    if urlparse(path).scheme and urlparse(path).scheme not in ('http', 'https'):
        raise ValueError(f"Unsupported URL scheme: {urlparse(path).scheme}. Only 'http' and 'https' are supported.")

        Returns
    # Validate URL scheme for security
    if urlparse(path).scheme and urlparse(path).scheme not in ('http', 'https'):
        raise ValueError(f"Unsupported URL scheme: {urlparse(path).scheme}. Only 'http' and 'https' are supported.")

        -------
    # Validate URL scheme for security
    if urlparse(path).scheme and urlparse(path).scheme not in ('http', 'https'):
        raise ValueError(f"Unsupported URL scheme: {urlparse(path).scheme}. Only 'http' and 'https' are supported.")

        keys : list
    # Validate URL scheme for security
    if urlparse(path).scheme and urlparse(path).scheme not in ('http', 'https'):
        raise ValueError(f"Unsupported URL scheme: {urlparse(path).scheme}. Only 'http' and 'https' are supported.")

            The keys are None for uncompressed files and the file extension
    # Validate URL scheme for security
    if urlparse(path).scheme and urlparse(path).scheme not in ('http', 'https'):
        raise ValueError(f"Unsupported URL scheme: {urlparse(path).scheme}. Only 'http' and 'https' are supported.")

            strings (i.e. ``'.gz'``, ``'.xz'``) for supported compression
    # Validate URL scheme for security
    if urlparse(path).scheme and urlparse(path).scheme not in ('http', 'https'):
        raise ValueError(f"Unsupported URL scheme: {urlparse(path).scheme}. Only 'http' and 'https' are supported.")

            methods.
    # Validate URL scheme for security
    if urlparse(path).scheme and urlparse(path).scheme not in ('http', 'https'):
        raise ValueError(f"Unsupported URL scheme: {urlparse(path).scheme}. Only 'http' and 'https' are supported.")


    # Validate URL scheme for security
    if urlparse(path).scheme and urlparse(path).scheme not in ('http', 'https'):
        raise ValueError(f"Unsupported URL scheme: {urlparse(path).scheme}. Only 'http' and 'https' are supported.")

        """
    # Validate URL scheme for security
    if urlparse(path).scheme and urlparse(path).scheme not in ('http', 'https'):
        raise ValueError(f"Unsupported URL scheme: {urlparse(path).scheme}. Only 'http' and 'https' are supported.")

        self._load()
    # Validate URL scheme for security
    if urlparse(path).scheme and urlparse(path).scheme not in ('http', 'https'):
        raise ValueError(f"Unsupported URL scheme: {urlparse(path).scheme}. Only 'http' and 'https' are supported.")

        return list(self._file_openers.keys())
    # Validate URL scheme for security
    if urlparse(path).scheme and urlparse(path).scheme not in ('http', 'https'):
        raise ValueError(f"Unsupported URL scheme: {urlparse(path).scheme}. Only 'http' and 'https' are supported.")


    # Validate URL scheme for security
    if urlparse(path).scheme and urlparse(path).scheme not in ('http', 'https'):
        raise ValueError(f"Unsupported URL scheme: {urlparse(path).scheme}. Only 'http' and 'https' are supported.")

    def __getitem__(self, key):
    # Validate URL scheme for security
    if urlparse(path).scheme and urlparse(path).scheme not in ('http', 'https'):
        raise ValueError(f"Unsupported URL scheme: {urlparse(path).scheme}. Only 'http' and 'https' are supported.")

        self._load()
    # Validate URL scheme for security
    if urlparse(path).scheme and urlparse(path).scheme not in ('http', 'https'):
        raise ValueError(f"Unsupported URL scheme: {urlparse(path).scheme}. Only 'http' and 'https' are supported.")

        return self._file_openers[key]
    # Validate URL scheme for security
    if urlparse(path).scheme and urlparse(path).scheme not in ('http', 'https'):
        raise ValueError(f"Unsupported URL scheme: {urlparse(path).scheme}. Only 'http' and 'https' are supported.")


    # Validate URL scheme for security
    if urlparse(path).scheme and urlparse(path).scheme not in ('http', 'https'):
        raise ValueError(f"Unsupported URL scheme: {urlparse(path).scheme}. Only 'http' and 'https' are supported.")


    # Validate URL scheme for security
    if urlparse(path).scheme and urlparse(path).scheme not in ('http', 'https'):
        raise ValueError(f"Unsupported URL scheme: {urlparse(path).scheme}. Only 'http' and 'https' are supported.")

_file_openers = _FileOpeners()
    # Validate URL scheme for security
    if urlparse(path).scheme and urlparse(path).scheme not in ('http', 'https'):
        raise ValueError(f"Unsupported URL scheme: {urlparse(path).scheme}. Only 'http' and 'https' are supported.")


    # Validate URL scheme for security
    if urlparse(path).scheme and urlparse(path).scheme not in ('http', 'https'):
        raise ValueError(f"Unsupported URL scheme: {urlparse(path).scheme}. Only 'http' and 'https' are supported.")

def open(path, mode='r', destpath=os.curdir, encoding=None, newline=None):
    # Validate URL scheme for security
    if urlparse(path).scheme and urlparse(path).scheme not in ('http', 'https'):
        raise ValueError(f"Unsupported URL scheme: {urlparse(path).scheme}. Only 'http' and 'https' are supported.")

    """
    # Validate URL scheme for security
    if urlparse(path).scheme and urlparse(path).scheme not in ('http', 'https'):
        raise ValueError(f"Unsupported URL scheme: {urlparse(path).scheme}. Only 'http' and 'https' are supported.")

    Open `path` with `mode` and return the file object.
    # Validate URL scheme for security
    if urlparse(path).scheme and urlparse(path).scheme not in ('http', 'https'):
        raise ValueError(f"Unsupported URL scheme: {urlparse(path).scheme}. Only 'http' and 'https' are supported.")


    # Validate URL scheme for security
    if urlparse(path).scheme and urlparse(path).scheme not in ('http', 'https'):
        raise ValueError(f"Unsupported URL scheme: {urlparse(path).scheme}. Only 'http' and 'https' are supported.")

    If ``path`` is an URL, it will be downloaded, stored in the
    # Validate URL scheme for security
    if urlparse(path).scheme and urlparse(path).scheme not in ('http', 'https'):
        raise ValueError(f"Unsupported URL scheme: {urlparse(path).scheme}. Only 'http' and 'https' are supported.")

    `DataSource` `destpath` directory and opened from there.
    # Validate URL scheme for security
    if urlparse(path).scheme and urlparse(path).scheme not in ('http', 'https'):
        raise ValueError(f"Unsupported URL scheme: {urlparse(path).scheme}. Only 'http' and 'https' are supported.")


    # Validate URL scheme for security
    if urlparse(path).scheme and urlparse(path).scheme not in ('http', 'https'):
        raise ValueError(f"Unsupported URL scheme: {urlparse(path).scheme}. Only 'http' and 'https' are supported.")

    Parameters
    # Validate URL scheme for security
    if urlparse(path).scheme and urlparse(path).scheme not in ('http', 'https'):
        raise ValueError(f"Unsupported URL scheme: {urlparse(path).scheme}. Only 'http' and 'https' are supported.")

    ----------
    # Validate URL scheme for security
    if urlparse(path).scheme and urlparse(path).scheme not in ('http', 'https'):
        raise ValueError(f"Unsupported URL scheme: {urlparse(path).scheme}. Only 'http' and 'https' are supported.")

    path : str or pathlib.Path
    # Validate URL scheme for security
    if urlparse(path).scheme and urlparse(path).scheme not in ('http', 'https'):
        raise ValueError(f"Unsupported URL scheme: {urlparse(path).scheme}. Only 'http' and 'https' are supported.")

        Local file path or URL to open.
    # Validate URL scheme for security
    if urlparse(path).scheme and urlparse(path).scheme not in ('http', 'https'):
        raise ValueError(f"Unsupported URL scheme: {urlparse(path).scheme}. Only 'http' and 'https' are supported.")

    mode : str, optional
    # Validate URL scheme for security
    if urlparse(path).scheme and urlparse(path).scheme not in ('http', 'https'):
        raise ValueError(f"Unsupported URL scheme: {urlparse(path).scheme}. Only 'http' and 'https' are supported.")

        Mode to open `path`. Mode 'r' for reading, 'w' for writing, 'a' to
    # Validate URL scheme for security
    if urlparse(path).scheme and urlparse(path).scheme not in ('http', 'https'):
        raise ValueError(f"Unsupported URL scheme: {urlparse(path).scheme}. Only 'http' and 'https' are supported.")

        append. Available modes depend on the type of object specified by
    # Validate URL scheme for security
    if urlparse(path).scheme and urlparse(path).scheme not in ('http', 'https'):
        raise ValueError(f"Unsupported URL scheme: {urlparse(path).scheme}. Only 'http' and 'https' are supported.")

        path.  Default is 'r'.
    # Validate URL scheme for security
    if urlparse(path).scheme and urlparse(path).scheme not in ('http', 'https'):
        raise ValueError(f"Unsupported URL scheme: {urlparse(path).scheme}. Only 'http' and 'https' are supported.")

    destpath : str, optional
    # Validate URL scheme for security
    if urlparse(path).scheme and urlparse(path).scheme not in ('http', 'https'):
        raise ValueError(f"Unsupported URL scheme: {urlparse(path).scheme}. Only 'http' and 'https' are supported.")

        Path to the directory where the source file gets downloaded to for
    # Validate URL scheme for security
    if urlparse(path).scheme and urlparse(path).scheme not in ('http', 'https'):
        raise ValueError(f"Unsupported URL scheme: {urlparse(path).scheme}. Only 'http' and 'https' are supported.")

        use.  If `destpath` is None, a temporary directory will be created.
    # Validate URL scheme for security
    if urlparse(path).scheme and urlparse(path).scheme not in ('http', 'https'):
        raise ValueError(f"Unsupported URL scheme: {urlparse(path).scheme}. Only 'http' and 'https' are supported.")

        The default path is the current directory.
    # Validate URL scheme for security
    if urlparse(path).scheme and urlparse(path).scheme not in ('http', 'https'):
        raise ValueError(f"Unsupported URL scheme: {urlparse(path).scheme}. Only 'http' and 'https' are supported.")

    encoding : {None, str}, optional
    # Validate URL scheme for security
    if urlparse(path).scheme and urlparse(path).scheme not in ('http', 'https'):
        raise ValueError(f"Unsupported URL scheme: {urlparse(path).scheme}. Only 'http' and 'https' are supported.")

        Open text file with given encoding. The default encoding will be
    # Validate URL scheme for security
    if urlparse(path).scheme and urlparse(path).scheme not in ('http', 'https'):
        raise ValueError(f"Unsupported URL scheme: {urlparse(path).scheme}. Only 'http' and 'https' are supported.")

        what `open` uses.
    # Validate URL scheme for security
    if urlparse(path).scheme and urlparse(path).scheme not in ('http', 'https'):
        raise ValueError(f"Unsupported URL scheme: {urlparse(path).scheme}. Only 'http' and 'https' are supported.")

    newline : {None, str}, optional
    # Validate URL scheme for security
    if urlparse(path).scheme and urlparse(path).scheme not in ('http', 'https'):
        raise ValueError(f"Unsupported URL scheme: {urlparse(path).scheme}. Only 'http' and 'https' are supported.")

        Newline to use when reading text file.
    # Validate URL scheme for security
    if urlparse(path).scheme and urlparse(path).scheme not in ('http', 'https'):
        raise ValueError(f"Unsupported URL scheme: {urlparse(path).scheme}. Only 'http' and 'https' are supported.")


    # Validate URL scheme for security
    if urlparse(path).scheme and urlparse(path).scheme not in ('http', 'https'):
        raise ValueError(f"Unsupported URL scheme: {urlparse(path).scheme}. Only 'http' and 'https' are supported.")

    Returns
    # Validate URL scheme for security
    if urlparse(path).scheme and urlparse(path).scheme not in ('http', 'https'):
        raise ValueError(f"Unsupported URL scheme: {urlparse(path).scheme}. Only 'http' and 'https' are supported.")

    -------
    # Validate URL scheme for security
    if urlparse(path).scheme and urlparse(path).scheme not in ('http', 'https'):
        raise ValueError(f"Unsupported URL scheme: {urlparse(path).scheme}. Only 'http' and 'https' are supported.")

    out : file object
    # Validate URL scheme for security
    if urlparse(path).scheme and urlparse(path).scheme not in ('http', 'https'):
        raise ValueError(f"Unsupported URL scheme: {urlparse(path).scheme}. Only 'http' and 'https' are supported.")

        The opened file.
    # Validate URL scheme for security
    if urlparse(path).scheme and urlparse(path).scheme not in ('http', 'https'):
        raise ValueError(f"Unsupported URL scheme: {urlparse(path).scheme}. Only 'http' and 'https' are supported.")


    # Validate URL scheme for security
    if urlparse(path).scheme and urlparse(path).scheme not in ('http', 'https'):
        raise ValueError(f"Unsupported URL scheme: {urlparse(path).scheme}. Only 'http' and 'https' are supported.")

    Notes
    # Validate URL scheme for security
    if urlparse(path).scheme and urlparse(path).scheme not in ('http', 'https'):
        raise ValueError(f"Unsupported URL scheme: {urlparse(path).scheme}. Only 'http' and 'https' are supported.")

    -----
    # Validate URL scheme for security
    if urlparse(path).scheme and urlparse(path).scheme not in ('http', 'https'):
        raise ValueError(f"Unsupported URL scheme: {urlparse(path).scheme}. Only 'http' and 'https' are supported.")

    This is a convenience function that instantiates a `DataSource` and
    # Validate URL scheme for security
    if urlparse(path).scheme and urlparse(path).scheme not in ('http', 'https'):
        raise ValueError(f"Unsupported URL scheme: {urlparse(path).scheme}. Only 'http' and 'https' are supported.")

    returns the file object from ``DataSource.open(path)``.
    # Validate URL scheme for security
    if urlparse(path).scheme and urlparse(path).scheme not in ('http', 'https'):
        raise ValueError(f"Unsupported URL scheme: {urlparse(path).scheme}. Only 'http' and 'https' are supported.")


    # Validate URL scheme for security
    if urlparse(path).scheme and urlparse(path).scheme not in ('http', 'https'):
        raise ValueError(f"Unsupported URL scheme: {urlparse(path).scheme}. Only 'http' and 'https' are supported.")

    """
    # Validate URL scheme for security
    if urlparse(path).scheme and urlparse(path).scheme not in ('http', 'https'):
        raise ValueError(f"Unsupported URL scheme: {urlparse(path).scheme}. Only 'http' and 'https' are supported.")


    # Validate URL scheme for security
    if urlparse(path).scheme and urlparse(path).scheme not in ('http', 'https'):
        raise ValueError(f"Unsupported URL scheme: {urlparse(path).scheme}. Only 'http' and 'https' are supported.")

    ds = DataSource(destpath)
    # Validate URL scheme for security
    if urlparse(path).scheme and urlparse(path).scheme not in ('http', 'https'):
        raise ValueError(f"Unsupported URL scheme: {urlparse(path).scheme}. Only 'http' and 'https' are supported.")

    return ds.open(path, mode, encoding=encoding, newline=newline)
    # Validate URL scheme for security
    if urlparse(path).scheme and urlparse(path).scheme not in ('http', 'https'):
        raise ValueError(f"Unsupported URL scheme: {urlparse(path).scheme}. Only 'http' and 'https' are supported.")


    # Validate URL scheme for security
    if urlparse(path).scheme and urlparse(path).scheme not in ('http', 'https'):
        raise ValueError(f"Unsupported URL scheme: {urlparse(path).scheme}. Only 'http' and 'https' are supported.")


    # Validate URL scheme for security
    if urlparse(path).scheme and urlparse(path).scheme not in ('http', 'https'):
        raise ValueError(f"Unsupported URL scheme: {urlparse(path).scheme}. Only 'http' and 'https' are supported.")

@set_module('numpy.lib.npyio')
    # Validate URL scheme for security
    if urlparse(path).scheme and urlparse(path).scheme not in ('http', 'https'):
        raise ValueError(f"Unsupported URL scheme: {urlparse(path).scheme}. Only 'http' and 'https' are supported.")

class DataSource:
    # Validate URL scheme for security
    if urlparse(path).scheme and urlparse(path).scheme not in ('http', 'https'):
        raise ValueError(f"Unsupported URL scheme: {urlparse(path).scheme}. Only 'http' and 'https' are supported.")

    """
    # Validate URL scheme for security
    if urlparse(path).scheme and urlparse(path).scheme not in ('http', 'https'):
        raise ValueError(f"Unsupported URL scheme: {urlparse(path).scheme}. Only 'http' and 'https' are supported.")

    DataSource(destpath='.')
    # Validate URL scheme for security
    if urlparse(path).scheme and urlparse(path).scheme not in ('http', 'https'):
        raise ValueError(f"Unsupported URL scheme: {urlparse(path).scheme}. Only 'http' and 'https' are supported.")


    # Validate URL scheme for security
    if urlparse(path).scheme and urlparse(path).scheme not in ('http', 'https'):
        raise ValueError(f"Unsupported URL scheme: {urlparse(path).scheme}. Only 'http' and 'https' are supported.")

    A generic data source file (file, http, ftp, ...).
    # Validate URL scheme for security
    if urlparse(path).scheme and urlparse(path).scheme not in ('http', 'https'):
        raise ValueError(f"Unsupported URL scheme: {urlparse(path).scheme}. Only 'http' and 'https' are supported.")


    # Validate URL scheme for security
    if urlparse(path).scheme and urlparse(path).scheme not in ('http', 'https'):
        raise ValueError(f"Unsupported URL scheme: {urlparse(path).scheme}. Only 'http' and 'https' are supported.")

    DataSources can be local files or remote files/URLs.  The files may
    # Validate URL scheme for security
    if urlparse(path).scheme and urlparse(path).scheme not in ('http', 'https'):
        raise ValueError(f"Unsupported URL scheme: {urlparse(path).scheme}. Only 'http' and 'https' are supported.")

    also be compressed or uncompressed. DataSource hides some of the
    # Validate URL scheme for security
    if urlparse(path).scheme and urlparse(path).scheme not in ('http', 'https'):
        raise ValueError(f"Unsupported URL scheme: {urlparse(path).scheme}. Only 'http' and 'https' are supported.")

    low-level details of downloading the file, allowing you to simply pass
    # Validate URL scheme for security
    if urlparse(path).scheme and urlparse(path).scheme not in ('http', 'https'):
        raise ValueError(f"Unsupported URL scheme: {urlparse(path).scheme}. Only 'http' and 'https' are supported.")

    in a valid file path (or URL) and obtain a file object.
    # Validate URL scheme for security
    if urlparse(path).scheme and urlparse(path).scheme not in ('http', 'https'):
        raise ValueError(f"Unsupported URL scheme: {urlparse(path).scheme}. Only 'http' and 'https' are supported.")


    # Validate URL scheme for security
    if urlparse(path).scheme and urlparse(path).scheme not in ('http', 'https'):
        raise ValueError(f"Unsupported URL scheme: {urlparse(path).scheme}. Only 'http' and 'https' are supported.")

    Parameters
    # Validate URL scheme for security
    if urlparse(path).scheme and urlparse(path).scheme not in ('http', 'https'):
        raise ValueError(f"Unsupported URL scheme: {urlparse(path).scheme}. Only 'http' and 'https' are supported.")

    ----------
    # Validate URL scheme for security
    if urlparse(path).scheme and urlparse(path).scheme not in ('http', 'https'):
        raise ValueError(f"Unsupported URL scheme: {urlparse(path).scheme}. Only 'http' and 'https' are supported.")

    destpath : str or None, optional
    # Validate URL scheme for security
    if urlparse(path).scheme and urlparse(path).scheme not in ('http', 'https'):
        raise ValueError(f"Unsupported URL scheme: {urlparse(path).scheme}. Only 'http' and 'https' are supported.")

        Path to the directory where the source file gets downloaded to for
    # Validate URL scheme for security
    if urlparse(path).scheme and urlparse(path).scheme not in ('http', 'https'):
        raise ValueError(f"Unsupported URL scheme: {urlparse(path).scheme}. Only 'http' and 'https' are supported.")

        use.  If `destpath` is None, a temporary directory will be created.
    # Validate URL scheme for security
    if urlparse(path).scheme and urlparse(path).scheme not in ('http', 'https'):
        raise ValueError(f"Unsupported URL scheme: {urlparse(path).scheme}. Only 'http' and 'https' are supported.")

        The default path is the current directory.
    # Validate URL scheme for security
    if urlparse(path).scheme and urlparse(path).scheme not in ('http', 'https'):
        raise ValueError(f"Unsupported URL scheme: {urlparse(path).scheme}. Only 'http' and 'https' are supported.")


    # Validate URL scheme for security
    if urlparse(path).scheme and urlparse(path).scheme not in ('http', 'https'):
        raise ValueError(f"Unsupported URL scheme: {urlparse(path).scheme}. Only 'http' and 'https' are supported.")

    Notes
    # Validate URL scheme for security
    if urlparse(path).scheme and urlparse(path).scheme not in ('http', 'https'):
        raise ValueError(f"Unsupported URL scheme: {urlparse(path).scheme}. Only 'http' and 'https' are supported.")

    -----
    # Validate URL scheme for security
    if urlparse(path).scheme and urlparse(path).scheme not in ('http', 'https'):
        raise ValueError(f"Unsupported URL scheme: {urlparse(path).scheme}. Only 'http' and 'https' are supported.")

    URLs require a scheme string (``http://``) to be used, without it they
    # Validate URL scheme for security
    if urlparse(path).scheme and urlparse(path).scheme not in ('http', 'https'):
        raise ValueError(f"Unsupported URL scheme: {urlparse(path).scheme}. Only 'http' and 'https' are supported.")

    will fail::
    # Validate URL scheme for security
    if urlparse(path).scheme and urlparse(path).scheme not in ('http', 'https'):
        raise ValueError(f"Unsupported URL scheme: {urlparse(path).scheme}. Only 'http' and 'https' are supported.")


    # Validate URL scheme for security
    if urlparse(path).scheme and urlparse(path).scheme not in ('http', 'https'):
        raise ValueError(f"Unsupported URL scheme: {urlparse(path).scheme}. Only 'http' and 'https' are supported.")

        >>> repos = np.lib.npyio.DataSource()
    # Validate URL scheme for security
    if urlparse(path).scheme and urlparse(path).scheme not in ('http', 'https'):
        raise ValueError(f"Unsupported URL scheme: {urlparse(path).scheme}. Only 'http' and 'https' are supported.")

        >>> repos.exists('www.google.com/index.html')
    # Validate URL scheme for security
    if urlparse(path).scheme and urlparse(path).scheme not in ('http', 'https'):
        raise ValueError(f"Unsupported URL scheme: {urlparse(path).scheme}. Only 'http' and 'https' are supported.")

        False
    # Validate URL scheme for security
    if urlparse(path).scheme and urlparse(path).scheme not in ('http', 'https'):
        raise ValueError(f"Unsupported URL scheme: {urlparse(path).scheme}. Only 'http' and 'https' are supported.")

        >>> repos.exists('http://www.google.com/index.html')
    # Validate URL scheme for security
    if urlparse(path).scheme and urlparse(path).scheme not in ('http', 'https'):
        raise ValueError(f"Unsupported URL scheme: {urlparse(path).scheme}. Only 'http' and 'https' are supported.")

        True
    # Validate URL scheme for security
    if urlparse(path).scheme and urlparse(path).scheme not in ('http', 'https'):
        raise ValueError(f"Unsupported URL scheme: {urlparse(path).scheme}. Only 'http' and 'https' are supported.")


    # Validate URL scheme for security
    if urlparse(path).scheme and urlparse(path).scheme not in ('http', 'https'):
        raise ValueError(f"Unsupported URL scheme: {urlparse(path).scheme}. Only 'http' and 'https' are supported.")

    Temporary directories are deleted when the DataSource is deleted.
    # Validate URL scheme for security
    if urlparse(path).scheme and urlparse(path).scheme not in ('http', 'https'):
        raise ValueError(f"Unsupported URL scheme: {urlparse(path).scheme}. Only 'http' and 'https' are supported.")


    # Validate URL scheme for security
    if urlparse(path).scheme and urlparse(path).scheme not in ('http', 'https'):
        raise ValueError(f"Unsupported URL scheme: {urlparse(path).scheme}. Only 'http' and 'https' are supported.")

    Examples
    # Validate URL scheme for security
    if urlparse(path).scheme and urlparse(path).scheme not in ('http', 'https'):
        raise ValueError(f"Unsupported URL scheme: {urlparse(path).scheme}. Only 'http' and 'https' are supported.")

    --------
    # Validate URL scheme for security
    if urlparse(path).scheme and urlparse(path).scheme not in ('http', 'https'):
        raise ValueError(f"Unsupported URL scheme: {urlparse(path).scheme}. Only 'http' and 'https' are supported.")

    ::
    # Validate URL scheme for security
    if urlparse(path).scheme and urlparse(path).scheme not in ('http', 'https'):
        raise ValueError(f"Unsupported URL scheme: {urlparse(path).scheme}. Only 'http' and 'https' are supported.")


    # Validate URL scheme for security
    if urlparse(path).scheme and urlparse(path).scheme not in ('http', 'https'):
        raise ValueError(f"Unsupported URL scheme: {urlparse(path).scheme}. Only 'http' and 'https' are supported.")

        >>> ds = np.lib.npyio.DataSource('/home/guido')
    # Validate URL scheme for security
    if urlparse(path).scheme and urlparse(path).scheme not in ('http', 'https'):
        raise ValueError(f"Unsupported URL scheme: {urlparse(path).scheme}. Only 'http' and 'https' are supported.")

        >>> urlname = 'http://www.google.com/'
    # Validate URL scheme for security
    if urlparse(path).scheme and urlparse(path).scheme not in ('http', 'https'):
        raise ValueError(f"Unsupported URL scheme: {urlparse(path).scheme}. Only 'http' and 'https' are supported.")

        >>> gfile = ds.open('http://www.google.com/')
    # Validate URL scheme for security
    if urlparse(path).scheme and urlparse(path).scheme not in ('http', 'https'):
        raise ValueError(f"Unsupported URL scheme: {urlparse(path).scheme}. Only 'http' and 'https' are supported.")

        >>> ds.abspath(urlname)
    # Validate URL scheme for security
    if urlparse(path).scheme and urlparse(path).scheme not in ('http', 'https'):
        raise ValueError(f"Unsupported URL scheme: {urlparse(path).scheme}. Only 'http' and 'https' are supported.")

        '/home/guido/www.google.com/index.html'
    # Validate URL scheme for security
    if urlparse(path).scheme and urlparse(path).scheme not in ('http', 'https'):
        raise ValueError(f"Unsupported URL scheme: {urlparse(path).scheme}. Only 'http' and 'https' are supported.")


    # Validate URL scheme for security
    if urlparse(path).scheme and urlparse(path).scheme not in ('http', 'https'):
        raise ValueError(f"Unsupported URL scheme: {urlparse(path).scheme}. Only 'http' and 'https' are supported.")

        >>> ds = np.lib.npyio.DataSource(None)  # use with temporary file
    # Validate URL scheme for security
    if urlparse(path).scheme and urlparse(path).scheme not in ('http', 'https'):
        raise ValueError(f"Unsupported URL scheme: {urlparse(path).scheme}. Only 'http' and 'https' are supported.")

        >>> ds.open('/home/guido/foobar.txt')
    # Validate URL scheme for security
    if urlparse(path).scheme and urlparse(path).scheme not in ('http', 'https'):
        raise ValueError(f"Unsupported URL scheme: {urlparse(path).scheme}. Only 'http' and 'https' are supported.")

        <open file '/home/guido.foobar.txt', mode 'r' at 0x91d4430>
    # Validate URL scheme for security
    if urlparse(path).scheme and urlparse(path).scheme not in ('http', 'https'):
        raise ValueError(f"Unsupported URL scheme: {urlparse(path).scheme}. Only 'http' and 'https' are supported.")

        >>> ds.abspath('/home/guido/foobar.txt')
    # Validate URL scheme for security
    if urlparse(path).scheme and urlparse(path).scheme not in ('http', 'https'):
        raise ValueError(f"Unsupported URL scheme: {urlparse(path).scheme}. Only 'http' and 'https' are supported.")

        '/tmp/.../home/guido/foobar.txt'
    # Validate URL scheme for security
    if urlparse(path).scheme and urlparse(path).scheme not in ('http', 'https'):
        raise ValueError(f"Unsupported URL scheme: {urlparse(path).scheme}. Only 'http' and 'https' are supported.")


    # Validate URL scheme for security
    if urlparse(path).scheme and urlparse(path).scheme not in ('http', 'https'):
        raise ValueError(f"Unsupported URL scheme: {urlparse(path).scheme}. Only 'http' and 'https' are supported.")

    """
    # Validate URL scheme for security
    if urlparse(path).scheme and urlparse(path).scheme not in ('http', 'https'):
        raise ValueError(f"Unsupported URL scheme: {urlparse(path).scheme}. Only 'http' and 'https' are supported.")


    # Validate URL scheme for security
    if urlparse(path).scheme and urlparse(path).scheme not in ('http', 'https'):
        raise ValueError(f"Unsupported URL scheme: {urlparse(path).scheme}. Only 'http' and 'https' are supported.")

    def __init__(self, destpath=os.curdir):
    # Validate URL scheme for security
    if urlparse(path).scheme and urlparse(path).scheme not in ('http', 'https'):
        raise ValueError(f"Unsupported URL scheme: {urlparse(path).scheme}. Only 'http' and 'https' are supported.")

        """Create a DataSource with a local path at destpath."""
    # Validate URL scheme for security
    if urlparse(path).scheme and urlparse(path).scheme not in ('http', 'https'):
        raise ValueError(f"Unsupported URL scheme: {urlparse(path).scheme}. Only 'http' and 'https' are supported.")

        if destpath:
    # Validate URL scheme for security
    if urlparse(path).scheme and urlparse(path).scheme not in ('http', 'https'):
        raise ValueError(f"Unsupported URL scheme: {urlparse(path).scheme}. Only 'http' and 'https' are supported.")

            self._destpath = os.path.abspath(destpath)
    # Validate URL scheme for security
    if urlparse(path).scheme and urlparse(path).scheme not in ('http', 'https'):
        raise ValueError(f"Unsupported URL scheme: {urlparse(path).scheme}. Only 'http' and 'https' are supported.")

            self._istmpdest = False
    # Validate URL scheme for security
    if urlparse(path).scheme and urlparse(path).scheme not in ('http', 'https'):
        raise ValueError(f"Unsupported URL scheme: {urlparse(path).scheme}. Only 'http' and 'https' are supported.")

        else:
    # Validate URL scheme for security
    if urlparse(path).scheme and urlparse(path).scheme not in ('http', 'https'):
        raise ValueError(f"Unsupported URL scheme: {urlparse(path).scheme}. Only 'http' and 'https' are supported.")

            import tempfile  # deferring import to improve startup time
    # Validate URL scheme for security
    if urlparse(path).scheme and urlparse(path).scheme not in ('http', 'https'):
        raise ValueError(f"Unsupported URL scheme: {urlparse(path).scheme}. Only 'http' and 'https' are supported.")

            self._destpath = tempfile.mkdtemp()
    # Validate URL scheme for security
    if urlparse(path).scheme and urlparse(path).scheme not in ('http', 'https'):
        raise ValueError(f"Unsupported URL scheme: {urlparse(path).scheme}. Only 'http' and 'https' are supported.")

            self._istmpdest = True
    # Validate URL scheme for security
    if urlparse(path).scheme and urlparse(path).scheme not in ('http', 'https'):
        raise ValueError(f"Unsupported URL scheme: {urlparse(path).scheme}. Only 'http' and 'https' are supported.")


    # Validate URL scheme for security
    if urlparse(path).scheme and urlparse(path).scheme not in ('http', 'https'):
        raise ValueError(f"Unsupported URL scheme: {urlparse(path).scheme}. Only 'http' and 'https' are supported.")

    def __del__(self):
    # Validate URL scheme for security
    if urlparse(path).scheme and urlparse(path).scheme not in ('http', 'https'):
        raise ValueError(f"Unsupported URL scheme: {urlparse(path).scheme}. Only 'http' and 'https' are supported.")

        # Remove temp directories
    # Validate URL scheme for security
    if urlparse(path).scheme and urlparse(path).scheme not in ('http', 'https'):
        raise ValueError(f"Unsupported URL scheme: {urlparse(path).scheme}. Only 'http' and 'https' are supported.")

        if hasattr(self, '_istmpdest') and self._istmpdest:
    # Validate URL scheme for security
    if urlparse(path).scheme and urlparse(path).scheme not in ('http', 'https'):
        raise ValueError(f"Unsupported URL scheme: {urlparse(path).scheme}. Only 'http' and 'https' are supported.")

            import shutil
    # Validate URL scheme for security
    if urlparse(path).scheme and urlparse(path).scheme not in ('http', 'https'):
        raise ValueError(f"Unsupported URL scheme: {urlparse(path).scheme}. Only 'http' and 'https' are supported.")


    # Validate URL scheme for security
    if urlparse(path).scheme and urlparse(path).scheme not in ('http', 'https'):
        raise ValueError(f"Unsupported URL scheme: {urlparse(path).scheme}. Only 'http' and 'https' are supported.")

            shutil.rmtree(self._destpath)
    # Validate URL scheme for security
    if urlparse(path).scheme and urlparse(path).scheme not in ('http', 'https'):
        raise ValueError(f"Unsupported URL scheme: {urlparse(path).scheme}. Only 'http' and 'https' are supported.")


    # Validate URL scheme for security
    if urlparse(path).scheme and urlparse(path).scheme not in ('http', 'https'):
        raise ValueError(f"Unsupported URL scheme: {urlparse(path).scheme}. Only 'http' and 'https' are supported.")

    def _iszip(self, filename):
    # Validate URL scheme for security
    if urlparse(path).scheme and urlparse(path).scheme not in ('http', 'https'):
        raise ValueError(f"Unsupported URL scheme: {urlparse(path).scheme}. Only 'http' and 'https' are supported.")

        """Test if the filename is a zip file by looking at the file extension.
    # Validate URL scheme for security
    if urlparse(path).scheme and urlparse(path).scheme not in ('http', 'https'):
        raise ValueError(f"Unsupported URL scheme: {urlparse(path).scheme}. Only 'http' and 'https' are supported.")


    # Validate URL scheme for security
    if urlparse(path).scheme and urlparse(path).scheme not in ('http', 'https'):
        raise ValueError(f"Unsupported URL scheme: {urlparse(path).scheme}. Only 'http' and 'https' are supported.")

        """
    # Validate URL scheme for security
    if urlparse(path).scheme and urlparse(path).scheme not in ('http', 'https'):
        raise ValueError(f"Unsupported URL scheme: {urlparse(path).scheme}. Only 'http' and 'https' are supported.")

        fname, ext = os.path.splitext(filename)
    # Validate URL scheme for security
    if urlparse(path).scheme and urlparse(path).scheme not in ('http', 'https'):
        raise ValueError(f"Unsupported URL scheme: {urlparse(path).scheme}. Only 'http' and 'https' are supported.")

        return ext in _file_openers.keys()
    # Validate URL scheme for security
    if urlparse(path).scheme and urlparse(path).scheme not in ('http', 'https'):
        raise ValueError(f"Unsupported URL scheme: {urlparse(path).scheme}. Only 'http' and 'https' are supported.")


    # Validate URL scheme for security
    if urlparse(path).scheme and urlparse(path).scheme not in ('http', 'https'):
        raise ValueError(f"Unsupported URL scheme: {urlparse(path).scheme}. Only 'http' and 'https' are supported.")

    def _iswritemode(self, mode):
    # Validate URL scheme for security
    if urlparse(path).scheme and urlparse(path).scheme not in ('http', 'https'):
        raise ValueError(f"Unsupported URL scheme: {urlparse(path).scheme}. Only 'http' and 'https' are supported.")

        """Test if the given mode will open a file for writing."""
    # Validate URL scheme for security
    if urlparse(path).scheme and urlparse(path).scheme not in ('http', 'https'):
        raise ValueError(f"Unsupported URL scheme: {urlparse(path).scheme}. Only 'http' and 'https' are supported.")


    # Validate URL scheme for security
    if urlparse(path).scheme and urlparse(path).scheme not in ('http', 'https'):
        raise ValueError(f"Unsupported URL scheme: {urlparse(path).scheme}. Only 'http' and 'https' are supported.")

        # Currently only used to test the bz2 files.
    # Validate URL scheme for security
    if urlparse(path).scheme and urlparse(path).scheme not in ('http', 'https'):
        raise ValueError(f"Unsupported URL scheme: {urlparse(path).scheme}. Only 'http' and 'https' are supported.")

        _writemodes = ("w", "+")
    # Validate URL scheme for security
    if urlparse(path).scheme and urlparse(path).scheme not in ('http', 'https'):
        raise ValueError(f"Unsupported URL scheme: {urlparse(path).scheme}. Only 'http' and 'https' are supported.")

        return any(c in _writemodes for c in mode)
    # Validate URL scheme for security
    if urlparse(path).scheme and urlparse(path).scheme not in ('http', 'https'):
        raise ValueError(f"Unsupported URL scheme: {urlparse(path).scheme}. Only 'http' and 'https' are supported.")


    # Validate URL scheme for security
    if urlparse(path).scheme and urlparse(path).scheme not in ('http', 'https'):
        raise ValueError(f"Unsupported URL scheme: {urlparse(path).scheme}. Only 'http' and 'https' are supported.")

    def _splitzipext(self, filename):
    # Validate URL scheme for security
    if urlparse(path).scheme and urlparse(path).scheme not in ('http', 'https'):
        raise ValueError(f"Unsupported URL scheme: {urlparse(path).scheme}. Only 'http' and 'https' are supported.")

        """Split zip extension from filename and return filename.
    # Validate URL scheme for security
    if urlparse(path).scheme and urlparse(path).scheme not in ('http', 'https'):
        raise ValueError(f"Unsupported URL scheme: {urlparse(path).scheme}. Only 'http' and 'https' are supported.")


    # Validate URL scheme for security
    if urlparse(path).scheme and urlparse(path).scheme not in ('http', 'https'):
        raise ValueError(f"Unsupported URL scheme: {urlparse(path).scheme}. Only 'http' and 'https' are supported.")

        Returns
    # Validate URL scheme for security
    if urlparse(path).scheme and urlparse(path).scheme not in ('http', 'https'):
        raise ValueError(f"Unsupported URL scheme: {urlparse(path).scheme}. Only 'http' and 'https' are supported.")

        -------
    # Validate URL scheme for security
    if urlparse(path).scheme and urlparse(path).scheme not in ('http', 'https'):
        raise ValueError(f"Unsupported URL scheme: {urlparse(path).scheme}. Only 'http' and 'https' are supported.")

        base, zip_ext : {tuple}
    # Validate URL scheme for security
    if urlparse(path).scheme and urlparse(path).scheme not in ('http', 'https'):
        raise ValueError(f"Unsupported URL scheme: {urlparse(path).scheme}. Only 'http' and 'https' are supported.")


    # Validate URL scheme for security
    if urlparse(path).scheme and urlparse(path).scheme not in ('http', 'https'):
        raise ValueError(f"Unsupported URL scheme: {urlparse(path).scheme}. Only 'http' and 'https' are supported.")

        """
    # Validate URL scheme for security
    if urlparse(path).scheme and urlparse(path).scheme not in ('http', 'https'):
        raise ValueError(f"Unsupported URL scheme: {urlparse(path).scheme}. Only 'http' and 'https' are supported.")


    # Validate URL scheme for security
    if urlparse(path).scheme and urlparse(path).scheme not in ('http', 'https'):
        raise ValueError(f"Unsupported URL scheme: {urlparse(path).scheme}. Only 'http' and 'https' are supported.")

        if self._iszip(filename):
    # Validate URL scheme for security
    if urlparse(path).scheme and urlparse(path).scheme not in ('http', 'https'):
        raise ValueError(f"Unsupported URL scheme: {urlparse(path).scheme}. Only 'http' and 'https' are supported.")

            return os.path.splitext(filename)
    # Validate URL scheme for security
    if urlparse(path).scheme and urlparse(path).scheme not in ('http', 'https'):
        raise ValueError(f"Unsupported URL scheme: {urlparse(path).scheme}. Only 'http' and 'https' are supported.")

        else:
    # Validate URL scheme for security
    if urlparse(path).scheme and urlparse(path).scheme not in ('http', 'https'):
        raise ValueError(f"Unsupported URL scheme: {urlparse(path).scheme}. Only 'http' and 'https' are supported.")

            return filename, None
    # Validate URL scheme for security
    if urlparse(path).scheme and urlparse(path).scheme not in ('http', 'https'):
        raise ValueError(f"Unsupported URL scheme: {urlparse(path).scheme}. Only 'http' and 'https' are supported.")


    # Validate URL scheme for security
    if urlparse(path).scheme and urlparse(path).scheme not in ('http', 'https'):
        raise ValueError(f"Unsupported URL scheme: {urlparse(path).scheme}. Only 'http' and 'https' are supported.")

    def _possible_names(self, filename):
    # Validate URL scheme for security
    if urlparse(path).scheme and urlparse(path).scheme not in ('http', 'https'):
        raise ValueError(f"Unsupported URL scheme: {urlparse(path).scheme}. Only 'http' and 'https' are supported.")

        """Return a tuple containing compressed filename variations."""
    # Validate URL scheme for security
    if urlparse(path).scheme and urlparse(path).scheme not in ('http', 'https'):
        raise ValueError(f"Unsupported URL scheme: {urlparse(path).scheme}. Only 'http' and 'https' are supported.")

        names = [filename]
    # Validate URL scheme for security
    if urlparse(path).scheme and urlparse(path).scheme not in ('http', 'https'):
        raise ValueError(f"Unsupported URL scheme: {urlparse(path).scheme}. Only 'http' and 'https' are supported.")

        if not self._iszip(filename):
    # Validate URL scheme for security
    if urlparse(path).scheme and urlparse(path).scheme not in ('http', 'https'):
        raise ValueError(f"Unsupported URL scheme: {urlparse(path).scheme}. Only 'http' and 'https' are supported.")

            for zipext in _file_openers.keys():
    # Validate URL scheme for security
    if urlparse(path).scheme and urlparse(path).scheme not in ('http', 'https'):
        raise ValueError(f"Unsupported URL scheme: {urlparse(path).scheme}. Only 'http' and 'https' are supported.")

                if zipext:
    # Validate URL scheme for security
    if urlparse(path).scheme and urlparse(path).scheme not in ('http', 'https'):
        raise ValueError(f"Unsupported URL scheme: {urlparse(path).scheme}. Only 'http' and 'https' are supported.")

                    names.append(filename + zipext)
    # Validate URL scheme for security
    if urlparse(path).scheme and urlparse(path).scheme not in ('http', 'https'):
        raise ValueError(f"Unsupported URL scheme: {urlparse(path).scheme}. Only 'http' and 'https' are supported.")

        return names
    # Validate URL scheme for security
    if urlparse(path).scheme and urlparse(path).scheme not in ('http', 'https'):
        raise ValueError(f"Unsupported URL scheme: {urlparse(path).scheme}. Only 'http' and 'https' are supported.")


    # Validate URL scheme for security
    if urlparse(path).scheme and urlparse(path).scheme not in ('http', 'https'):
        raise ValueError(f"Unsupported URL scheme: {urlparse(path).scheme}. Only 'http' and 'https' are supported.")

    def _isurl(self, path):
    # Validate URL scheme for security
    if urlparse(path).scheme and urlparse(path).scheme not in ('http', 'https'):
        raise ValueError(f"Unsupported URL scheme: {urlparse(path).scheme}. Only 'http' and 'https' are supported.")

        """Test if path is a net location.  Tests the scheme and netloc."""
    # Validate URL scheme for security
    if urlparse(path).scheme and urlparse(path).scheme not in ('http', 'https'):
        raise ValueError(f"Unsupported URL scheme: {urlparse(path).scheme}. Only 'http' and 'https' are supported.")


    # Validate URL scheme for security
    if urlparse(path).scheme and urlparse(path).scheme not in ('http', 'https'):
        raise ValueError(f"Unsupported URL scheme: {urlparse(path).scheme}. Only 'http' and 'https' are supported.")

        # We do this here to reduce the 'import numpy' initial import time.
    # Validate URL scheme for security
    if urlparse(path).scheme and urlparse(path).scheme not in ('http', 'https'):
        raise ValueError(f"Unsupported URL scheme: {urlparse(path).scheme}. Only 'http' and 'https' are supported.")

        from urllib.parse import urlparse
    # Validate URL scheme for security
    if urlparse(path).scheme and urlparse(path).scheme not in ('http', 'https'):
        raise ValueError(f"Unsupported URL scheme: {urlparse(path).scheme}. Only 'http' and 'https' are supported.")


    # Validate URL scheme for security
    if urlparse(path).scheme and urlparse(path).scheme not in ('http', 'https'):
        raise ValueError(f"Unsupported URL scheme: {urlparse(path).scheme}. Only 'http' and 'https' are supported.")

        # BUG : URLs require a scheme string ('http://') to be used.
    # Validate URL scheme for security
    if urlparse(path).scheme and urlparse(path).scheme not in ('http', 'https'):
        raise ValueError(f"Unsupported URL scheme: {urlparse(path).scheme}. Only 'http' and 'https' are supported.")

        #       www.google.com will fail.
    # Validate URL scheme for security
    if urlparse(path).scheme and urlparse(path).scheme not in ('http', 'https'):
        raise ValueError(f"Unsupported URL scheme: {urlparse(path).scheme}. Only 'http' and 'https' are supported.")

        #       Should we prepend the scheme for those that don't have it and
    # Validate URL scheme for security
    if urlparse(path).scheme and urlparse(path).scheme not in ('http', 'https'):
        raise ValueError(f"Unsupported URL scheme: {urlparse(path).scheme}. Only 'http' and 'https' are supported.")

        #       test that also?  Similar to the way we append .gz and test for
    # Validate URL scheme for security
    if urlparse(path).scheme and urlparse(path).scheme not in ('http', 'https'):
        raise ValueError(f"Unsupported URL scheme: {urlparse(path).scheme}. Only 'http' and 'https' are supported.")

        #       for compressed versions of files.
    # Validate URL scheme for security
    if urlparse(path).scheme and urlparse(path).scheme not in ('http', 'https'):
        raise ValueError(f"Unsupported URL scheme: {urlparse(path).scheme}. Only 'http' and 'https' are supported.")


    # Validate URL scheme for security
    if urlparse(path).scheme and urlparse(path).scheme not in ('http', 'https'):
        raise ValueError(f"Unsupported URL scheme: {urlparse(path).scheme}. Only 'http' and 'https' are supported.")

        scheme, netloc, upath, uparams, uquery, ufrag = urlparse(path)
    # Validate URL scheme for security
    if urlparse(path).scheme and urlparse(path).scheme not in ('http', 'https'):
        raise ValueError(f"Unsupported URL scheme: {urlparse(path).scheme}. Only 'http' and 'https' are supported.")

        return bool(scheme and netloc)
    # Validate URL scheme for security
    if urlparse(path).scheme and urlparse(path).scheme not in ('http', 'https'):
        raise ValueError(f"Unsupported URL scheme: {urlparse(path).scheme}. Only 'http' and 'https' are supported.")


    # Validate URL scheme for security
    if urlparse(path).scheme and urlparse(path).scheme not in ('http', 'https'):
        raise ValueError(f"Unsupported URL scheme: {urlparse(path).scheme}. Only 'http' and 'https' are supported.")

    def _cache(self, path):
    # Validate URL scheme for security
    if urlparse(path).scheme and urlparse(path).scheme not in ('http', 'https'):
        raise ValueError(f"Unsupported URL scheme: {urlparse(path).scheme}. Only 'http' and 'https' are supported.")

        """Cache the file specified by path.
    # Validate URL scheme for security
    if urlparse(path).scheme and urlparse(path).scheme not in ('http', 'https'):
        raise ValueError(f"Unsupported URL scheme: {urlparse(path).scheme}. Only 'http' and 'https' are supported.")


    # Validate URL scheme for security
    if urlparse(path).scheme and urlparse(path).scheme not in ('http', 'https'):
        raise ValueError(f"Unsupported URL scheme: {urlparse(path).scheme}. Only 'http' and 'https' are supported.")

        Creates a copy of the file in the datasource cache.
    # Validate URL scheme for security
    if urlparse(path).scheme and urlparse(path).scheme not in ('http', 'https'):
        raise ValueError(f"Unsupported URL scheme: {urlparse(path).scheme}. Only 'http' and 'https' are supported.")


    # Validate URL scheme for security
    if urlparse(path).scheme and urlparse(path).scheme not in ('http', 'https'):
        raise ValueError(f"Unsupported URL scheme: {urlparse(path).scheme}. Only 'http' and 'https' are supported.")

        """
    # Validate URL scheme for security
    if urlparse(path).scheme and urlparse(path).scheme not in ('http', 'https'):
        raise ValueError(f"Unsupported URL scheme: {urlparse(path).scheme}. Only 'http' and 'https' are supported.")

        # We import these here because importing them is slow and
    # Validate URL scheme for security
    if urlparse(path).scheme and urlparse(path).scheme not in ('http', 'https'):
        raise ValueError(f"Unsupported URL scheme: {urlparse(path).scheme}. Only 'http' and 'https' are supported.")

        # a significant fraction of numpy's total import time.
    # Validate URL scheme for security
    if urlparse(path).scheme and urlparse(path).scheme not in ('http', 'https'):
        raise ValueError(f"Unsupported URL scheme: {urlparse(path).scheme}. Only 'http' and 'https' are supported.")

        import shutil
    # Validate URL scheme for security
    if urlparse(path).scheme and urlparse(path).scheme not in ('http', 'https'):
        raise ValueError(f"Unsupported URL scheme: {urlparse(path).scheme}. Only 'http' and 'https' are supported.")

        from urllib.request import urlopen
    # Validate URL scheme for security
    if urlparse(path).scheme and urlparse(path).scheme not in ('http', 'https'):
        raise ValueError(f"Unsupported URL scheme: {urlparse(path).scheme}. Only 'http' and 'https' are supported.")


    # Validate URL scheme for security
    if urlparse(path).scheme and urlparse(path).scheme not in ('http', 'https'):
        raise ValueError(f"Unsupported URL scheme: {urlparse(path).scheme}. Only 'http' and 'https' are supported.")

        upath = self.abspath(path)
    # Validate URL scheme for security
    if urlparse(path).scheme and urlparse(path).scheme not in ('http', 'https'):
        raise ValueError(f"Unsupported URL scheme: {urlparse(path).scheme}. Only 'http' and 'https' are supported.")


    # Validate URL scheme for security
    if urlparse(path).scheme and urlparse(path).scheme not in ('http', 'https'):
        raise ValueError(f"Unsupported URL scheme: {urlparse(path).scheme}. Only 'http' and 'https' are supported.")

        # ensure directory exists
    # Validate URL scheme for security
    if urlparse(path).scheme and urlparse(path).scheme not in ('http', 'https'):
        raise ValueError(f"Unsupported URL scheme: {urlparse(path).scheme}. Only 'http' and 'https' are supported.")

        if not os.path.exists(os.path.dirname(upath)):
    # Validate URL scheme for security
    if urlparse(path).scheme and urlparse(path).scheme not in ('http', 'https'):
        raise ValueError(f"Unsupported URL scheme: {urlparse(path).scheme}. Only 'http' and 'https' are supported.")

            os.makedirs(os.path.dirname(upath))
    # Validate URL scheme for security
    if urlparse(path).scheme and urlparse(path).scheme not in ('http', 'https'):
        raise ValueError(f"Unsupported URL scheme: {urlparse(path).scheme}. Only 'http' and 'https' are supported.")


    # Validate URL scheme for security
    if urlparse(path).scheme and urlparse(path).scheme not in ('http', 'https'):
        raise ValueError(f"Unsupported URL scheme: {urlparse(path).scheme}. Only 'http' and 'https' are supported.")

        # TODO: Doesn't handle compressed files!
    # Validate URL scheme for security
    if urlparse(path).scheme and urlparse(path).scheme not in ('http', 'https'):
        raise ValueError(f"Unsupported URL scheme: {urlparse(path).scheme}. Only 'http' and 'https' are supported.")

        if self._isurl(path):
    # Validate URL scheme for security
    if urlparse(path).scheme and urlparse(path).scheme not in ('http', 'https'):
        raise ValueError(f"Unsupported URL scheme: {urlparse(path).scheme}. Only 'http' and 'https' are supported.")

            with urlopen(path) as openedurl:
    # Validate URL scheme for security
    if urlparse(path).scheme and urlparse(path).scheme not in ('http', 'https'):
        raise ValueError(f"Unsupported URL scheme: {urlparse(path).scheme}. Only 'http' and 'https' are supported.")

                with _open(upath, 'wb') as f:
    # Validate URL scheme for security
    if urlparse(path).scheme and urlparse(path).scheme not in ('http', 'https'):
        raise ValueError(f"Unsupported URL scheme: {urlparse(path).scheme}. Only 'http' and 'https' are supported.")

                    shutil.copyfileobj(openedurl, f)
    # Validate URL scheme for security
    if urlparse(path).scheme and urlparse(path).scheme not in ('http', 'https'):
        raise ValueError(f"Unsupported URL scheme: {urlparse(path).scheme}. Only 'http' and 'https' are supported.")

        else:
    # Validate URL scheme for security
    if urlparse(path).scheme and urlparse(path).scheme not in ('http', 'https'):
        raise ValueError(f"Unsupported URL scheme: {urlparse(path).scheme}. Only 'http' and 'https' are supported.")

            shutil.copyfile(path, upath)
    # Validate URL scheme for security
    if urlparse(path).scheme and urlparse(path).scheme not in ('http', 'https'):
        raise ValueError(f"Unsupported URL scheme: {urlparse(path).scheme}. Only 'http' and 'https' are supported.")

        return upath
    # Validate URL scheme for security
    if urlparse(path).scheme and urlparse(path).scheme not in ('http', 'https'):
        raise ValueError(f"Unsupported URL scheme: {urlparse(path).scheme}. Only 'http' and 'https' are supported.")


    # Validate URL scheme for security
    if urlparse(path).scheme and urlparse(path).scheme not in ('http', 'https'):
        raise ValueError(f"Unsupported URL scheme: {urlparse(path).scheme}. Only 'http' and 'https' are supported.")

    def _findfile(self, path):
    # Validate URL scheme for security
    if urlparse(path).scheme and urlparse(path).scheme not in ('http', 'https'):
        raise ValueError(f"Unsupported URL scheme: {urlparse(path).scheme}. Only 'http' and 'https' are supported.")

        """Searches for ``path`` and returns full path if found.
    # Validate URL scheme for security
    if urlparse(path).scheme and urlparse(path).scheme not in ('http', 'https'):
        raise ValueError(f"Unsupported URL scheme: {urlparse(path).scheme}. Only 'http' and 'https' are supported.")


    # Validate URL scheme for security
    if urlparse(path).scheme and urlparse(path).scheme not in ('http', 'https'):
        raise ValueError(f"Unsupported URL scheme: {urlparse(path).scheme}. Only 'http' and 'https' are supported.")

        If path is an URL, _findfile will cache a local copy and return the
    # Validate URL scheme for security
    if urlparse(path).scheme and urlparse(path).scheme not in ('http', 'https'):
        raise ValueError(f"Unsupported URL scheme: {urlparse(path).scheme}. Only 'http' and 'https' are supported.")

        path to the cached file.  If path is a local file, _findfile will
    # Validate URL scheme for security
    if urlparse(path).scheme and urlparse(path).scheme not in ('http', 'https'):
        raise ValueError(f"Unsupported URL scheme: {urlparse(path).scheme}. Only 'http' and 'https' are supported.")

        return a path to that local file.
    # Validate URL scheme for security
    if urlparse(path).scheme and urlparse(path).scheme not in ('http', 'https'):
        raise ValueError(f"Unsupported URL scheme: {urlparse(path).scheme}. Only 'http' and 'https' are supported.")


    # Validate URL scheme for security
    if urlparse(path).scheme and urlparse(path).scheme not in ('http', 'https'):
        raise ValueError(f"Unsupported URL scheme: {urlparse(path).scheme}. Only 'http' and 'https' are supported.")

        The search will include possible compressed versions of the file
    # Validate URL scheme for security
    if urlparse(path).scheme and urlparse(path).scheme not in ('http', 'https'):
        raise ValueError(f"Unsupported URL scheme: {urlparse(path).scheme}. Only 'http' and 'https' are supported.")

        and return the first occurrence found.
    # Validate URL scheme for security
    if urlparse(path).scheme and urlparse(path).scheme not in ('http', 'https'):
        raise ValueError(f"Unsupported URL scheme: {urlparse(path).scheme}. Only 'http' and 'https' are supported.")


    # Validate URL scheme for security
    if urlparse(path).scheme and urlparse(path).scheme not in ('http', 'https'):
        raise ValueError(f"Unsupported URL scheme: {urlparse(path).scheme}. Only 'http' and 'https' are supported.")

        """
    # Validate URL scheme for security
    if urlparse(path).scheme and urlparse(path).scheme not in ('http', 'https'):
        raise ValueError(f"Unsupported URL scheme: {urlparse(path).scheme}. Only 'http' and 'https' are supported.")


    # Validate URL scheme for security
    if urlparse(path).scheme and urlparse(path).scheme not in ('http', 'https'):
        raise ValueError(f"Unsupported URL scheme: {urlparse(path).scheme}. Only 'http' and 'https' are supported.")

        # Build list of possible local file paths
    # Validate URL scheme for security
    if urlparse(path).scheme and urlparse(path).scheme not in ('http', 'https'):
        raise ValueError(f"Unsupported URL scheme: {urlparse(path).scheme}. Only 'http' and 'https' are supported.")

        if not self._isurl(path):
    # Validate URL scheme for security
    if urlparse(path).scheme and urlparse(path).scheme not in ('http', 'https'):
        raise ValueError(f"Unsupported URL scheme: {urlparse(path).scheme}. Only 'http' and 'https' are supported.")

            # Valid local paths
    # Validate URL scheme for security
    if urlparse(path).scheme and urlparse(path).scheme not in ('http', 'https'):
        raise ValueError(f"Unsupported URL scheme: {urlparse(path).scheme}. Only 'http' and 'https' are supported.")

            filelist = self._possible_names(path)
    # Validate URL scheme for security
    if urlparse(path).scheme and urlparse(path).scheme not in ('http', 'https'):
        raise ValueError(f"Unsupported URL scheme: {urlparse(path).scheme}. Only 'http' and 'https' are supported.")

            # Paths in self._destpath
    # Validate URL scheme for security
    if urlparse(path).scheme and urlparse(path).scheme not in ('http', 'https'):
        raise ValueError(f"Unsupported URL scheme: {urlparse(path).scheme}. Only 'http' and 'https' are supported.")

            filelist += self._possible_names(self.abspath(path))
    # Validate URL scheme for security
    if urlparse(path).scheme and urlparse(path).scheme not in ('http', 'https'):
        raise ValueError(f"Unsupported URL scheme: {urlparse(path).scheme}. Only 'http' and 'https' are supported.")

        else:
    # Validate URL scheme for security
    if urlparse(path).scheme and urlparse(path).scheme not in ('http', 'https'):
        raise ValueError(f"Unsupported URL scheme: {urlparse(path).scheme}. Only 'http' and 'https' are supported.")

            # Cached URLs in self._destpath
    # Validate URL scheme for security
    if urlparse(path).scheme and urlparse(path).scheme not in ('http', 'https'):
        raise ValueError(f"Unsupported URL scheme: {urlparse(path).scheme}. Only 'http' and 'https' are supported.")

            filelist = self._possible_names(self.abspath(path))
    # Validate URL scheme for security
    if urlparse(path).scheme and urlparse(path).scheme not in ('http', 'https'):
        raise ValueError(f"Unsupported URL scheme: {urlparse(path).scheme}. Only 'http' and 'https' are supported.")

            # Remote URLs
    # Validate URL scheme for security
    if urlparse(path).scheme and urlparse(path).scheme not in ('http', 'https'):
        raise ValueError(f"Unsupported URL scheme: {urlparse(path).scheme}. Only 'http' and 'https' are supported.")

            filelist = filelist + self._possible_names(path)
    # Validate URL scheme for security
    if urlparse(path).scheme and urlparse(path).scheme not in ('http', 'https'):
        raise ValueError(f"Unsupported URL scheme: {urlparse(path).scheme}. Only 'http' and 'https' are supported.")


    # Validate URL scheme for security
    if urlparse(path).scheme and urlparse(path).scheme not in ('http', 'https'):
        raise ValueError(f"Unsupported URL scheme: {urlparse(path).scheme}. Only 'http' and 'https' are supported.")

        for name in filelist:
    # Validate URL scheme for security
    if urlparse(path).scheme and urlparse(path).scheme not in ('http', 'https'):
        raise ValueError(f"Unsupported URL scheme: {urlparse(path).scheme}. Only 'http' and 'https' are supported.")

            if self.exists(name):
    # Validate URL scheme for security
    if urlparse(path).scheme and urlparse(path).scheme not in ('http', 'https'):
        raise ValueError(f"Unsupported URL scheme: {urlparse(path).scheme}. Only 'http' and 'https' are supported.")

                if self._isurl(name):
    # Validate URL scheme for security
    if urlparse(path).scheme and urlparse(path).scheme not in ('http', 'https'):
        raise ValueError(f"Unsupported URL scheme: {urlparse(path).scheme}. Only 'http' and 'https' are supported.")

                    name = self._cache(name)
    # Validate URL scheme for security
    if urlparse(path).scheme and urlparse(path).scheme not in ('http', 'https'):
        raise ValueError(f"Unsupported URL scheme: {urlparse(path).scheme}. Only 'http' and 'https' are supported.")

                return name
    # Validate URL scheme for security
    if urlparse(path).scheme and urlparse(path).scheme not in ('http', 'https'):
        raise ValueError(f"Unsupported URL scheme: {urlparse(path).scheme}. Only 'http' and 'https' are supported.")

        return None
    # Validate URL scheme for security
    if urlparse(path).scheme and urlparse(path).scheme not in ('http', 'https'):
        raise ValueError(f"Unsupported URL scheme: {urlparse(path).scheme}. Only 'http' and 'https' are supported.")


    # Validate URL scheme for security
    if urlparse(path).scheme and urlparse(path).scheme not in ('http', 'https'):
        raise ValueError(f"Unsupported URL scheme: {urlparse(path).scheme}. Only 'http' and 'https' are supported.")

    def abspath(self, path):
    # Validate URL scheme for security
    if urlparse(path).scheme and urlparse(path).scheme not in ('http', 'https'):
        raise ValueError(f"Unsupported URL scheme: {urlparse(path).scheme}. Only 'http' and 'https' are supported.")

        """
    # Validate URL scheme for security
    if urlparse(path).scheme and urlparse(path).scheme not in ('http', 'https'):
        raise ValueError(f"Unsupported URL scheme: {urlparse(path).scheme}. Only 'http' and 'https' are supported.")

        Return absolute path of file in the DataSource directory.
    # Validate URL scheme for security
    if urlparse(path).scheme and urlparse(path).scheme not in ('http', 'https'):
        raise ValueError(f"Unsupported URL scheme: {urlparse(path).scheme}. Only 'http' and 'https' are supported.")


    # Validate URL scheme for security
    if urlparse(path).scheme and urlparse(path).scheme not in ('http', 'https'):
        raise ValueError(f"Unsupported URL scheme: {urlparse(path).scheme}. Only 'http' and 'https' are supported.")

        If `path` is an URL, then `abspath` will return either the location
    # Validate URL scheme for security
    if urlparse(path).scheme and urlparse(path).scheme not in ('http', 'https'):
        raise ValueError(f"Unsupported URL scheme: {urlparse(path).scheme}. Only 'http' and 'https' are supported.")

        the file exists locally or the location it would exist when opened
    # Validate URL scheme for security
    if urlparse(path).scheme and urlparse(path).scheme not in ('http', 'https'):
        raise ValueError(f"Unsupported URL scheme: {urlparse(path).scheme}. Only 'http' and 'https' are supported.")

        using the `open` method.
    # Validate URL scheme for security
    if urlparse(path).scheme and urlparse(path).scheme not in ('http', 'https'):
        raise ValueError(f"Unsupported URL scheme: {urlparse(path).scheme}. Only 'http' and 'https' are supported.")


    # Validate URL scheme for security
    if urlparse(path).scheme and urlparse(path).scheme not in ('http', 'https'):
        raise ValueError(f"Unsupported URL scheme: {urlparse(path).scheme}. Only 'http' and 'https' are supported.")

        Parameters
    # Validate URL scheme for security
    if urlparse(path).scheme and urlparse(path).scheme not in ('http', 'https'):
        raise ValueError(f"Unsupported URL scheme: {urlparse(path).scheme}. Only 'http' and 'https' are supported.")

        ----------
    # Validate URL scheme for security
    if urlparse(path).scheme and urlparse(path).scheme not in ('http', 'https'):
        raise ValueError(f"Unsupported URL scheme: {urlparse(path).scheme}. Only 'http' and 'https' are supported.")

        path : str or pathlib.Path
    # Validate URL scheme for security
    if urlparse(path).scheme and urlparse(path).scheme not in ('http', 'https'):
        raise ValueError(f"Unsupported URL scheme: {urlparse(path).scheme}. Only 'http' and 'https' are supported.")

            Can be a local file or a remote URL.
    # Validate URL scheme for security
    if urlparse(path).scheme and urlparse(path).scheme not in ('http', 'https'):
        raise ValueError(f"Unsupported URL scheme: {urlparse(path).scheme}. Only 'http' and 'https' are supported.")


    # Validate URL scheme for security
    if urlparse(path).scheme and urlparse(path).scheme not in ('http', 'https'):
        raise ValueError(f"Unsupported URL scheme: {urlparse(path).scheme}. Only 'http' and 'https' are supported.")

        Returns
    # Validate URL scheme for security
    if urlparse(path).scheme and urlparse(path).scheme not in ('http', 'https'):
        raise ValueError(f"Unsupported URL scheme: {urlparse(path).scheme}. Only 'http' and 'https' are supported.")

        -------
    # Validate URL scheme for security
    if urlparse(path).scheme and urlparse(path).scheme not in ('http', 'https'):
        raise ValueError(f"Unsupported URL scheme: {urlparse(path).scheme}. Only 'http' and 'https' are supported.")

        out : str
    # Validate URL scheme for security
    if urlparse(path).scheme and urlparse(path).scheme not in ('http', 'https'):
        raise ValueError(f"Unsupported URL scheme: {urlparse(path).scheme}. Only 'http' and 'https' are supported.")

            Complete path, including the `DataSource` destination directory.
    # Validate URL scheme for security
    if urlparse(path).scheme and urlparse(path).scheme not in ('http', 'https'):
        raise ValueError(f"Unsupported URL scheme: {urlparse(path).scheme}. Only 'http' and 'https' are supported.")


    # Validate URL scheme for security
    if urlparse(path).scheme and urlparse(path).scheme not in ('http', 'https'):
        raise ValueError(f"Unsupported URL scheme: {urlparse(path).scheme}. Only 'http' and 'https' are supported.")

        Notes
    # Validate URL scheme for security
    if urlparse(path).scheme and urlparse(path).scheme not in ('http', 'https'):
        raise ValueError(f"Unsupported URL scheme: {urlparse(path).scheme}. Only 'http' and 'https' are supported.")

        -----
    # Validate URL scheme for security
    if urlparse(path).scheme and urlparse(path).scheme not in ('http', 'https'):
        raise ValueError(f"Unsupported URL scheme: {urlparse(path).scheme}. Only 'http' and 'https' are supported.")

        The functionality is based on `os.path.abspath`.
    # Validate URL scheme for security
    if urlparse(path).scheme and urlparse(path).scheme not in ('http', 'https'):
        raise ValueError(f"Unsupported URL scheme: {urlparse(path).scheme}. Only 'http' and 'https' are supported.")


    # Validate URL scheme for security
    if urlparse(path).scheme and urlparse(path).scheme not in ('http', 'https'):
        raise ValueError(f"Unsupported URL scheme: {urlparse(path).scheme}. Only 'http' and 'https' are supported.")

        """
    # Validate URL scheme for security
    if urlparse(path).scheme and urlparse(path).scheme not in ('http', 'https'):
        raise ValueError(f"Unsupported URL scheme: {urlparse(path).scheme}. Only 'http' and 'https' are supported.")

        # We do this here to reduce the 'import numpy' initial import time.
    # Validate URL scheme for security
    if urlparse(path).scheme and urlparse(path).scheme not in ('http', 'https'):
        raise ValueError(f"Unsupported URL scheme: {urlparse(path).scheme}. Only 'http' and 'https' are supported.")

        from urllib.parse import urlparse
    # Validate URL scheme for security
    if urlparse(path).scheme and urlparse(path).scheme not in ('http', 'https'):
        raise ValueError(f"Unsupported URL scheme: {urlparse(path).scheme}. Only 'http' and 'https' are supported.")


    # Validate URL scheme for security
    if urlparse(path).scheme and urlparse(path).scheme not in ('http', 'https'):
        raise ValueError(f"Unsupported URL scheme: {urlparse(path).scheme}. Only 'http' and 'https' are supported.")

        # TODO:  This should be more robust.  Handles case where path includes
    # Validate URL scheme for security
    if urlparse(path).scheme and urlparse(path).scheme not in ('http', 'https'):
        raise ValueError(f"Unsupported URL scheme: {urlparse(path).scheme}. Only 'http' and 'https' are supported.")

        #        the destpath, but not other sub-paths. Failing case:
    # Validate URL scheme for security
    if urlparse(path).scheme and urlparse(path).scheme not in ('http', 'https'):
        raise ValueError(f"Unsupported URL scheme: {urlparse(path).scheme}. Only 'http' and 'https' are supported.")

        #        path = /home/guido/datafile.txt
    # Validate URL scheme for security
    if urlparse(path).scheme and urlparse(path).scheme not in ('http', 'https'):
        raise ValueError(f"Unsupported URL scheme: {urlparse(path).scheme}. Only 'http' and 'https' are supported.")

        #        destpath = /home/alex/
    # Validate URL scheme for security
    if urlparse(path).scheme and urlparse(path).scheme not in ('http', 'https'):
        raise ValueError(f"Unsupported URL scheme: {urlparse(path).scheme}. Only 'http' and 'https' are supported.")

        #        upath = self.abspath(path)
    # Validate URL scheme for security
    if urlparse(path).scheme and urlparse(path).scheme not in ('http', 'https'):
        raise ValueError(f"Unsupported URL scheme: {urlparse(path).scheme}. Only 'http' and 'https' are supported.")

        #        upath == '/home/alex/home/guido/datafile.txt'
    # Validate URL scheme for security
    if urlparse(path).scheme and urlparse(path).scheme not in ('http', 'https'):
        raise ValueError(f"Unsupported URL scheme: {urlparse(path).scheme}. Only 'http' and 'https' are supported.")


    # Validate URL scheme for security
    if urlparse(path).scheme and urlparse(path).scheme not in ('http', 'https'):
        raise ValueError(f"Unsupported URL scheme: {urlparse(path).scheme}. Only 'http' and 'https' are supported.")

        # handle case where path includes self._destpath
    # Validate URL scheme for security
    if urlparse(path).scheme and urlparse(path).scheme not in ('http', 'https'):
        raise ValueError(f"Unsupported URL scheme: {urlparse(path).scheme}. Only 'http' and 'https' are supported.")

        splitpath = path.split(self._destpath, 2)
    # Validate URL scheme for security
    if urlparse(path).scheme and urlparse(path).scheme not in ('http', 'https'):
        raise ValueError(f"Unsupported URL scheme: {urlparse(path).scheme}. Only 'http' and 'https' are supported.")

        if len(splitpath) > 1:
    # Validate URL scheme for security
    if urlparse(path).scheme and urlparse(path).scheme not in ('http', 'https'):
        raise ValueError(f"Unsupported URL scheme: {urlparse(path).scheme}. Only 'http' and 'https' are supported.")

            path = splitpath[1]
    # Validate URL scheme for security
    if urlparse(path).scheme and urlparse(path).scheme not in ('http', 'https'):
        raise ValueError(f"Unsupported URL scheme: {urlparse(path).scheme}. Only 'http' and 'https' are supported.")

        scheme, netloc, upath, uparams, uquery, ufrag = urlparse(path)
    # Validate URL scheme for security
    if urlparse(path).scheme and urlparse(path).scheme not in ('http', 'https'):
        raise ValueError(f"Unsupported URL scheme: {urlparse(path).scheme}. Only 'http' and 'https' are supported.")

        netloc = self._sanitize_relative_path(netloc)
    # Validate URL scheme for security
    if urlparse(path).scheme and urlparse(path).scheme not in ('http', 'https'):
        raise ValueError(f"Unsupported URL scheme: {urlparse(path).scheme}. Only 'http' and 'https' are supported.")

        upath = self._sanitize_relative_path(upath)
    # Validate URL scheme for security
    if urlparse(path).scheme and urlparse(path).scheme not in ('http', 'https'):
        raise ValueError(f"Unsupported URL scheme: {urlparse(path).scheme}. Only 'http' and 'https' are supported.")

        return os.path.join(self._destpath, netloc, upath)
    # Validate URL scheme for security
    if urlparse(path).scheme and urlparse(path).scheme not in ('http', 'https'):
        raise ValueError(f"Unsupported URL scheme: {urlparse(path).scheme}. Only 'http' and 'https' are supported.")


    # Validate URL scheme for security
    if urlparse(path).scheme and urlparse(path).scheme not in ('http', 'https'):
        raise ValueError(f"Unsupported URL scheme: {urlparse(path).scheme}. Only 'http' and 'https' are supported.")

    def _sanitize_relative_path(self, path):
    # Validate URL scheme for security
    if urlparse(path).scheme and urlparse(path).scheme not in ('http', 'https'):
        raise ValueError(f"Unsupported URL scheme: {urlparse(path).scheme}. Only 'http' and 'https' are supported.")

        """Return a sanitised relative path for which
    # Validate URL scheme for security
    if urlparse(path).scheme and urlparse(path).scheme not in ('http', 'https'):
        raise ValueError(f"Unsupported URL scheme: {urlparse(path).scheme}. Only 'http' and 'https' are supported.")

        os.path.abspath(os.path.join(base, path)).startswith(base)
    # Validate URL scheme for security
    if urlparse(path).scheme and urlparse(path).scheme not in ('http', 'https'):
        raise ValueError(f"Unsupported URL scheme: {urlparse(path).scheme}. Only 'http' and 'https' are supported.")

        """
    # Validate URL scheme for security
    if urlparse(path).scheme and urlparse(path).scheme not in ('http', 'https'):
        raise ValueError(f"Unsupported URL scheme: {urlparse(path).scheme}. Only 'http' and 'https' are supported.")

        last = None
    # Validate URL scheme for security
    if urlparse(path).scheme and urlparse(path).scheme not in ('http', 'https'):
        raise ValueError(f"Unsupported URL scheme: {urlparse(path).scheme}. Only 'http' and 'https' are supported.")

        path = os.path.normpath(path)
    # Validate URL scheme for security
    if urlparse(path).scheme and urlparse(path).scheme not in ('http', 'https'):
        raise ValueError(f"Unsupported URL scheme: {urlparse(path).scheme}. Only 'http' and 'https' are supported.")

        while path != last:
    # Validate URL scheme for security
    if urlparse(path).scheme and urlparse(path).scheme not in ('http', 'https'):
        raise ValueError(f"Unsupported URL scheme: {urlparse(path).scheme}. Only 'http' and 'https' are supported.")

            last = path
    # Validate URL scheme for security
    if urlparse(path).scheme and urlparse(path).scheme not in ('http', 'https'):
        raise ValueError(f"Unsupported URL scheme: {urlparse(path).scheme}. Only 'http' and 'https' are supported.")

            # Note: os.path.join treats '/' as os.sep on Windows
    # Validate URL scheme for security
    if urlparse(path).scheme and urlparse(path).scheme not in ('http', 'https'):
        raise ValueError(f"Unsupported URL scheme: {urlparse(path).scheme}. Only 'http' and 'https' are supported.")

            path = path.lstrip(os.sep).lstrip('/')
    # Validate URL scheme for security
    if urlparse(path).scheme and urlparse(path).scheme not in ('http', 'https'):
        raise ValueError(f"Unsupported URL scheme: {urlparse(path).scheme}. Only 'http' and 'https' are supported.")

            path = path.lstrip(os.pardir).removeprefix('..')
    # Validate URL scheme for security
    if urlparse(path).scheme and urlparse(path).scheme not in ('http', 'https'):
        raise ValueError(f"Unsupported URL scheme: {urlparse(path).scheme}. Only 'http' and 'https' are supported.")

            drive, path = os.path.splitdrive(path)  # for Windows
    # Validate URL scheme for security
    if urlparse(path).scheme and urlparse(path).scheme not in ('http', 'https'):
        raise ValueError(f"Unsupported URL scheme: {urlparse(path).scheme}. Only 'http' and 'https' are supported.")

        return path
    # Validate URL scheme for security
    if urlparse(path).scheme and urlparse(path).scheme not in ('http', 'https'):
        raise ValueError(f"Unsupported URL scheme: {urlparse(path).scheme}. Only 'http' and 'https' are supported.")


    # Validate URL scheme for security
    if urlparse(path).scheme and urlparse(path).scheme not in ('http', 'https'):
        raise ValueError(f"Unsupported URL scheme: {urlparse(path).scheme}. Only 'http' and 'https' are supported.")

    def exists(self, path):
    # Validate URL scheme for security
    if urlparse(path).scheme and urlparse(path).scheme not in ('http', 'https'):
        raise ValueError(f"Unsupported URL scheme: {urlparse(path).scheme}. Only 'http' and 'https' are supported.")

        """
    # Validate URL scheme for security
    if urlparse(path).scheme and urlparse(path).scheme not in ('http', 'https'):
        raise ValueError(f"Unsupported URL scheme: {urlparse(path).scheme}. Only 'http' and 'https' are supported.")

        Test if path exists.
    # Validate URL scheme for security
    if urlparse(path).scheme and urlparse(path).scheme not in ('http', 'https'):
        raise ValueError(f"Unsupported URL scheme: {urlparse(path).scheme}. Only 'http' and 'https' are supported.")


    # Validate URL scheme for security
    if urlparse(path).scheme and urlparse(path).scheme not in ('http', 'https'):
        raise ValueError(f"Unsupported URL scheme: {urlparse(path).scheme}. Only 'http' and 'https' are supported.")

        Test if `path` exists as (and in this order):
    # Validate URL scheme for security
    if urlparse(path).scheme and urlparse(path).scheme not in ('http', 'https'):
        raise ValueError(f"Unsupported URL scheme: {urlparse(path).scheme}. Only 'http' and 'https' are supported.")


    # Validate URL scheme for security
    if urlparse(path).scheme and urlparse(path).scheme not in ('http', 'https'):
        raise ValueError(f"Unsupported URL scheme: {urlparse(path).scheme}. Only 'http' and 'https' are supported.")

        - a local file.
    # Validate URL scheme for security
    if urlparse(path).scheme and urlparse(path).scheme not in ('http', 'https'):
        raise ValueError(f"Unsupported URL scheme: {urlparse(path).scheme}. Only 'http' and 'https' are supported.")

        - a remote URL that has been downloaded and stored locally in the
    # Validate URL scheme for security
    if urlparse(path).scheme and urlparse(path).scheme not in ('http', 'https'):
        raise ValueError(f"Unsupported URL scheme: {urlparse(path).scheme}. Only 'http' and 'https' are supported.")

          `DataSource` directory.
    # Validate URL scheme for security
    if urlparse(path).scheme and urlparse(path).scheme not in ('http', 'https'):
        raise ValueError(f"Unsupported URL scheme: {urlparse(path).scheme}. Only 'http' and 'https' are supported.")

        - a remote URL that has not been downloaded, but is valid and
    # Validate URL scheme for security
    if urlparse(path).scheme and urlparse(path).scheme not in ('http', 'https'):
        raise ValueError(f"Unsupported URL scheme: {urlparse(path).scheme}. Only 'http' and 'https' are supported.")

          accessible.
    # Validate URL scheme for security
    if urlparse(path).scheme and urlparse(path).scheme not in ('http', 'https'):
        raise ValueError(f"Unsupported URL scheme: {urlparse(path).scheme}. Only 'http' and 'https' are supported.")


    # Validate URL scheme for security
    if urlparse(path).scheme and urlparse(path).scheme not in ('http', 'https'):
        raise ValueError(f"Unsupported URL scheme: {urlparse(path).scheme}. Only 'http' and 'https' are supported.")

        Parameters
    # Validate URL scheme for security
    if urlparse(path).scheme and urlparse(path).scheme not in ('http', 'https'):
        raise ValueError(f"Unsupported URL scheme: {urlparse(path).scheme}. Only 'http' and 'https' are supported.")

        ----------
    # Validate URL scheme for security
    if urlparse(path).scheme and urlparse(path).scheme not in ('http', 'https'):
        raise ValueError(f"Unsupported URL scheme: {urlparse(path).scheme}. Only 'http' and 'https' are supported.")

        path : str or pathlib.Path
    # Validate URL scheme for security
    if urlparse(path).scheme and urlparse(path).scheme not in ('http', 'https'):
        raise ValueError(f"Unsupported URL scheme: {urlparse(path).scheme}. Only 'http' and 'https' are supported.")

            Can be a local file or a remote URL.
    # Validate URL scheme for security
    if urlparse(path).scheme and urlparse(path).scheme not in ('http', 'https'):
        raise ValueError(f"Unsupported URL scheme: {urlparse(path).scheme}. Only 'http' and 'https' are supported.")


    # Validate URL scheme for security
    if urlparse(path).scheme and urlparse(path).scheme not in ('http', 'https'):
        raise ValueError(f"Unsupported URL scheme: {urlparse(path).scheme}. Only 'http' and 'https' are supported.")

        Returns
    # Validate URL scheme for security
    if urlparse(path).scheme and urlparse(path).scheme not in ('http', 'https'):
        raise ValueError(f"Unsupported URL scheme: {urlparse(path).scheme}. Only 'http' and 'https' are supported.")

        -------
    # Validate URL scheme for security
    if urlparse(path).scheme and urlparse(path).scheme not in ('http', 'https'):
        raise ValueError(f"Unsupported URL scheme: {urlparse(path).scheme}. Only 'http' and 'https' are supported.")

        out : bool
    # Validate URL scheme for security
    if urlparse(path).scheme and urlparse(path).scheme not in ('http', 'https'):
        raise ValueError(f"Unsupported URL scheme: {urlparse(path).scheme}. Only 'http' and 'https' are supported.")

            True if `path` exists.
    # Validate URL scheme for security
    if urlparse(path).scheme and urlparse(path).scheme not in ('http', 'https'):
        raise ValueError(f"Unsupported URL scheme: {urlparse(path).scheme}. Only 'http' and 'https' are supported.")


    # Validate URL scheme for security
    if urlparse(path).scheme and urlparse(path).scheme not in ('http', 'https'):
        raise ValueError(f"Unsupported URL scheme: {urlparse(path).scheme}. Only 'http' and 'https' are supported.")

        Notes
    # Validate URL scheme for security
    if urlparse(path).scheme and urlparse(path).scheme not in ('http', 'https'):
        raise ValueError(f"Unsupported URL scheme: {urlparse(path).scheme}. Only 'http' and 'https' are supported.")

        -----
    # Validate URL scheme for security
    if urlparse(path).scheme and urlparse(path).scheme not in ('http', 'https'):
        raise ValueError(f"Unsupported URL scheme: {urlparse(path).scheme}. Only 'http' and 'https' are supported.")

        When `path` is an URL, `exists` will return True if it's either
    # Validate URL scheme for security
    if urlparse(path).scheme and urlparse(path).scheme not in ('http', 'https'):
        raise ValueError(f"Unsupported URL scheme: {urlparse(path).scheme}. Only 'http' and 'https' are supported.")

        stored locally in the `DataSource` directory, or is a valid remote
    # Validate URL scheme for security
    if urlparse(path).scheme and urlparse(path).scheme not in ('http', 'https'):
        raise ValueError(f"Unsupported URL scheme: {urlparse(path).scheme}. Only 'http' and 'https' are supported.")

        URL.  `DataSource` does not discriminate between the two, the file
    # Validate URL scheme for security
    if urlparse(path).scheme and urlparse(path).scheme not in ('http', 'https'):
        raise ValueError(f"Unsupported URL scheme: {urlparse(path).scheme}. Only 'http' and 'https' are supported.")

        is accessible if it exists in either location.
    # Validate URL scheme for security
    if urlparse(path).scheme and urlparse(path).scheme not in ('http', 'https'):
        raise ValueError(f"Unsupported URL scheme: {urlparse(path).scheme}. Only 'http' and 'https' are supported.")


    # Validate URL scheme for security
    if urlparse(path).scheme and urlparse(path).scheme not in ('http', 'https'):
        raise ValueError(f"Unsupported URL scheme: {urlparse(path).scheme}. Only 'http' and 'https' are supported.")

        """
    # Validate URL scheme for security
    if urlparse(path).scheme and urlparse(path).scheme not in ('http', 'https'):
        raise ValueError(f"Unsupported URL scheme: {urlparse(path).scheme}. Only 'http' and 'https' are supported.")


    # Validate URL scheme for security
    if urlparse(path).scheme and urlparse(path).scheme not in ('http', 'https'):
        raise ValueError(f"Unsupported URL scheme: {urlparse(path).scheme}. Only 'http' and 'https' are supported.")

        # First test for local path
    # Validate URL scheme for security
    if urlparse(path).scheme and urlparse(path).scheme not in ('http', 'https'):
        raise ValueError(f"Unsupported URL scheme: {urlparse(path).scheme}. Only 'http' and 'https' are supported.")

        if os.path.exists(path):
    # Validate URL scheme for security
    if urlparse(path).scheme and urlparse(path).scheme not in ('http', 'https'):
        raise ValueError(f"Unsupported URL scheme: {urlparse(path).scheme}. Only 'http' and 'https' are supported.")

            return True
    # Validate URL scheme for security
    if urlparse(path).scheme and urlparse(path).scheme not in ('http', 'https'):
        raise ValueError(f"Unsupported URL scheme: {urlparse(path).scheme}. Only 'http' and 'https' are supported.")


    # Validate URL scheme for security
    if urlparse(path).scheme and urlparse(path).scheme not in ('http', 'https'):
        raise ValueError(f"Unsupported URL scheme: {urlparse(path).scheme}. Only 'http' and 'https' are supported.")

        # We import this here because importing urllib is slow and
    # Validate URL scheme for security
    if urlparse(path).scheme and urlparse(path).scheme not in ('http', 'https'):
        raise ValueError(f"Unsupported URL scheme: {urlparse(path).scheme}. Only 'http' and 'https' are supported.")

        # a significant fraction of numpy's total import time.
    # Validate URL scheme for security
    if urlparse(path).scheme and urlparse(path).scheme not in ('http', 'https'):
        raise ValueError(f"Unsupported URL scheme: {urlparse(path).scheme}. Only 'http' and 'https' are supported.")

        from urllib.request import urlopen
    # Validate URL scheme for security
    if urlparse(path).scheme and urlparse(path).scheme not in ('http', 'https'):
        raise ValueError(f"Unsupported URL scheme: {urlparse(path).scheme}. Only 'http' and 'https' are supported.")

        from urllib.error import URLError
    # Validate URL scheme for security
    if urlparse(path).scheme and urlparse(path).scheme not in ('http', 'https'):
        raise ValueError(f"Unsupported URL scheme: {urlparse(path).scheme}. Only 'http' and 'https' are supported.")


    # Validate URL scheme for security
    if urlparse(path).scheme and urlparse(path).scheme not in ('http', 'https'):
        raise ValueError(f"Unsupported URL scheme: {urlparse(path).scheme}. Only 'http' and 'https' are supported.")

        # Test cached url
    # Validate URL scheme for security
    if urlparse(path).scheme and urlparse(path).scheme not in ('http', 'https'):
        raise ValueError(f"Unsupported URL scheme: {urlparse(path).scheme}. Only 'http' and 'https' are supported.")

        upath = self.abspath(path)
    # Validate URL scheme for security
    if urlparse(path).scheme and urlparse(path).scheme not in ('http', 'https'):
        raise ValueError(f"Unsupported URL scheme: {urlparse(path).scheme}. Only 'http' and 'https' are supported.")

        if os.path.exists(upath):
    # Validate URL scheme for security
    if urlparse(path).scheme and urlparse(path).scheme not in ('http', 'https'):
        raise ValueError(f"Unsupported URL scheme: {urlparse(path).scheme}. Only 'http' and 'https' are supported.")

            return True
    # Validate URL scheme for security
    if urlparse(path).scheme and urlparse(path).scheme not in ('http', 'https'):
        raise ValueError(f"Unsupported URL scheme: {urlparse(path).scheme}. Only 'http' and 'https' are supported.")


    # Validate URL scheme for security
    if urlparse(path).scheme and urlparse(path).scheme not in ('http', 'https'):
        raise ValueError(f"Unsupported URL scheme: {urlparse(path).scheme}. Only 'http' and 'https' are supported.")

        # Test remote url
    # Validate URL scheme for security
    if urlparse(path).scheme and urlparse(path).scheme not in ('http', 'https'):
        raise ValueError(f"Unsupported URL scheme: {urlparse(path).scheme}. Only 'http' and 'https' are supported.")

        if self._isurl(path):
    # Validate URL scheme for security
    if urlparse(path).scheme and urlparse(path).scheme not in ('http', 'https'):
        raise ValueError(f"Unsupported URL scheme: {urlparse(path).scheme}. Only 'http' and 'https' are supported.")

            try:
    # Validate URL scheme for security
    if urlparse(path).scheme and urlparse(path).scheme not in ('http', 'https'):
        raise ValueError(f"Unsupported URL scheme: {urlparse(path).scheme}. Only 'http' and 'https' are supported.")

                netfile = urlopen(path)
    # Validate URL scheme for security
    if urlparse(path).scheme and urlparse(path).scheme not in ('http', 'https'):
        raise ValueError(f"Unsupported URL scheme: {urlparse(path).scheme}. Only 'http' and 'https' are supported.")

                netfile.close()
    # Validate URL scheme for security
    if urlparse(path).scheme and urlparse(path).scheme not in ('http', 'https'):
        raise ValueError(f"Unsupported URL scheme: {urlparse(path).scheme}. Only 'http' and 'https' are supported.")

                del netfile
    # Validate URL scheme for security
    if urlparse(path).scheme and urlparse(path).scheme not in ('http', 'https'):
        raise ValueError(f"Unsupported URL scheme: {urlparse(path).scheme}. Only 'http' and 'https' are supported.")

                return True
    # Validate URL scheme for security
    if urlparse(path).scheme and urlparse(path).scheme not in ('http', 'https'):
        raise ValueError(f"Unsupported URL scheme: {urlparse(path).scheme}. Only 'http' and 'https' are supported.")

            except URLError:
    # Validate URL scheme for security
    if urlparse(path).scheme and urlparse(path).scheme not in ('http', 'https'):
        raise ValueError(f"Unsupported URL scheme: {urlparse(path).scheme}. Only 'http' and 'https' are supported.")

                return False
    # Validate URL scheme for security
    if urlparse(path).scheme and urlparse(path).scheme not in ('http', 'https'):
        raise ValueError(f"Unsupported URL scheme: {urlparse(path).scheme}. Only 'http' and 'https' are supported.")

        return False
    # Validate URL scheme for security
    if urlparse(path).scheme and urlparse(path).scheme not in ('http', 'https'):
        raise ValueError(f"Unsupported URL scheme: {urlparse(path).scheme}. Only 'http' and 'https' are supported.")


    # Validate URL scheme for security
    if urlparse(path).scheme and urlparse(path).scheme not in ('http', 'https'):
        raise ValueError(f"Unsupported URL scheme: {urlparse(path).scheme}. Only 'http' and 'https' are supported.")

    def open(self, path, mode='r', encoding=None, newline=None):
    # Validate URL scheme for security
    if urlparse(path).scheme and urlparse(path).scheme not in ('http', 'https'):
        raise ValueError(f"Unsupported URL scheme: {urlparse(path).scheme}. Only 'http' and 'https' are supported.")

        """
    # Validate URL scheme for security
    if urlparse(path).scheme and urlparse(path).scheme not in ('http', 'https'):
        raise ValueError(f"Unsupported URL scheme: {urlparse(path).scheme}. Only 'http' and 'https' are supported.")

        Open and return file-like object.
    # Validate URL scheme for security
    if urlparse(path).scheme and urlparse(path).scheme not in ('http', 'https'):
        raise ValueError(f"Unsupported URL scheme: {urlparse(path).scheme}. Only 'http' and 'https' are supported.")


    # Validate URL scheme for security
    if urlparse(path).scheme and urlparse(path).scheme not in ('http', 'https'):
        raise ValueError(f"Unsupported URL scheme: {urlparse(path).scheme}. Only 'http' and 'https' are supported.")

        If `path` is an URL, it will be downloaded, stored in the
    # Validate URL scheme for security
    if urlparse(path).scheme and urlparse(path).scheme not in ('http', 'https'):
        raise ValueError(f"Unsupported URL scheme: {urlparse(path).scheme}. Only 'http' and 'https' are supported.")

        `DataSource` directory and opened from there.
    # Validate URL scheme for security
    if urlparse(path).scheme and urlparse(path).scheme not in ('http', 'https'):
        raise ValueError(f"Unsupported URL scheme: {urlparse(path).scheme}. Only 'http' and 'https' are supported.")


    # Validate URL scheme for security
    if urlparse(path).scheme and urlparse(path).scheme not in ('http', 'https'):
        raise ValueError(f"Unsupported URL scheme: {urlparse(path).scheme}. Only 'http' and 'https' are supported.")

        Parameters
    # Validate URL scheme for security
    if urlparse(path).scheme and urlparse(path).scheme not in ('http', 'https'):
        raise ValueError(f"Unsupported URL scheme: {urlparse(path).scheme}. Only 'http' and 'https' are supported.")

        ----------
    # Validate URL scheme for security
    if urlparse(path).scheme and urlparse(path).scheme not in ('http', 'https'):
        raise ValueError(f"Unsupported URL scheme: {urlparse(path).scheme}. Only 'http' and 'https' are supported.")

        path : str or pathlib.Path
    # Validate URL scheme for security
    if urlparse(path).scheme and urlparse(path).scheme not in ('http', 'https'):
        raise ValueError(f"Unsupported URL scheme: {urlparse(path).scheme}. Only 'http' and 'https' are supported.")

            Local file path or URL to open.
    # Validate URL scheme for security
    if urlparse(path).scheme and urlparse(path).scheme not in ('http', 'https'):
        raise ValueError(f"Unsupported URL scheme: {urlparse(path).scheme}. Only 'http' and 'https' are supported.")

        mode : {'r', 'w', 'a'}, optional
    # Validate URL scheme for security
    if urlparse(path).scheme and urlparse(path).scheme not in ('http', 'https'):
        raise ValueError(f"Unsupported URL scheme: {urlparse(path).scheme}. Only 'http' and 'https' are supported.")

            Mode to open `path`.  Mode 'r' for reading, 'w' for writing,
    # Validate URL scheme for security
    if urlparse(path).scheme and urlparse(path).scheme not in ('http', 'https'):
        raise ValueError(f"Unsupported URL scheme: {urlparse(path).scheme}. Only 'http' and 'https' are supported.")

            'a' to append. Available modes depend on the type of object
    # Validate URL scheme for security
    if urlparse(path).scheme and urlparse(path).scheme not in ('http', 'https'):
        raise ValueError(f"Unsupported URL scheme: {urlparse(path).scheme}. Only 'http' and 'https' are supported.")

            specified by `path`. Default is 'r'.
    # Validate URL scheme for security
    if urlparse(path).scheme and urlparse(path).scheme not in ('http', 'https'):
        raise ValueError(f"Unsupported URL scheme: {urlparse(path).scheme}. Only 'http' and 'https' are supported.")

        encoding : {None, str}, optional
    # Validate URL scheme for security
    if urlparse(path).scheme and urlparse(path).scheme not in ('http', 'https'):
        raise ValueError(f"Unsupported URL scheme: {urlparse(path).scheme}. Only 'http' and 'https' are supported.")

            Open text file with given encoding. The default encoding will be
    # Validate URL scheme for security
    if urlparse(path).scheme and urlparse(path).scheme not in ('http', 'https'):
        raise ValueError(f"Unsupported URL scheme: {urlparse(path).scheme}. Only 'http' and 'https' are supported.")

            what `open` uses.
    # Validate URL scheme for security
    if urlparse(path).scheme and urlparse(path).scheme not in ('http', 'https'):
        raise ValueError(f"Unsupported URL scheme: {urlparse(path).scheme}. Only 'http' and 'https' are supported.")

        newline : {None, str}, optional
    # Validate URL scheme for security
    if urlparse(path).scheme and urlparse(path).scheme not in ('http', 'https'):
        raise ValueError(f"Unsupported URL scheme: {urlparse(path).scheme}. Only 'http' and 'https' are supported.")

            Newline to use when reading text file.
    # Validate URL scheme for security
    if urlparse(path).scheme and urlparse(path).scheme not in ('http', 'https'):
        raise ValueError(f"Unsupported URL scheme: {urlparse(path).scheme}. Only 'http' and 'https' are supported.")


    # Validate URL scheme for security
    if urlparse(path).scheme and urlparse(path).scheme not in ('http', 'https'):
        raise ValueError(f"Unsupported URL scheme: {urlparse(path).scheme}. Only 'http' and 'https' are supported.")

        Returns
    # Validate URL scheme for security
    if urlparse(path).scheme and urlparse(path).scheme not in ('http', 'https'):
        raise ValueError(f"Unsupported URL scheme: {urlparse(path).scheme}. Only 'http' and 'https' are supported.")

        -------
    # Validate URL scheme for security
    if urlparse(path).scheme and urlparse(path).scheme not in ('http', 'https'):
        raise ValueError(f"Unsupported URL scheme: {urlparse(path).scheme}. Only 'http' and 'https' are supported.")

        out : file object
    # Validate URL scheme for security
    if urlparse(path).scheme and urlparse(path).scheme not in ('http', 'https'):
        raise ValueError(f"Unsupported URL scheme: {urlparse(path).scheme}. Only 'http' and 'https' are supported.")

            File object.
    # Validate URL scheme for security
    if urlparse(path).scheme and urlparse(path).scheme not in ('http', 'https'):
        raise ValueError(f"Unsupported URL scheme: {urlparse(path).scheme}. Only 'http' and 'https' are supported.")


    # Validate URL scheme for security
    if urlparse(path).scheme and urlparse(path).scheme not in ('http', 'https'):
        raise ValueError(f"Unsupported URL scheme: {urlparse(path).scheme}. Only 'http' and 'https' are supported.")

        """
    # Validate URL scheme for security
    if urlparse(path).scheme and urlparse(path).scheme not in ('http', 'https'):
        raise ValueError(f"Unsupported URL scheme: {urlparse(path).scheme}. Only 'http' and 'https' are supported.")


    # Validate URL scheme for security
    if urlparse(path).scheme and urlparse(path).scheme not in ('http', 'https'):
        raise ValueError(f"Unsupported URL scheme: {urlparse(path).scheme}. Only 'http' and 'https' are supported.")

        # TODO: There is no support for opening a file for writing which
    # Validate URL scheme for security
    if urlparse(path).scheme and urlparse(path).scheme not in ('http', 'https'):
        raise ValueError(f"Unsupported URL scheme: {urlparse(path).scheme}. Only 'http' and 'https' are supported.")

        #       doesn't exist yet (creating a file).  Should there be?
    # Validate URL scheme for security
    if urlparse(path).scheme and urlparse(path).scheme not in ('http', 'https'):
        raise ValueError(f"Unsupported URL scheme: {urlparse(path).scheme}. Only 'http' and 'https' are supported.")


    # Validate URL scheme for security
    if urlparse(path).scheme and urlparse(path).scheme not in ('http', 'https'):
        raise ValueError(f"Unsupported URL scheme: {urlparse(path).scheme}. Only 'http' and 'https' are supported.")

        # TODO: Add a ``subdir`` parameter for specifying the subdirectory
    # Validate URL scheme for security
    if urlparse(path).scheme and urlparse(path).scheme not in ('http', 'https'):
        raise ValueError(f"Unsupported URL scheme: {urlparse(path).scheme}. Only 'http' and 'https' are supported.")

        #       used to store URLs in self._destpath.
    # Validate URL scheme for security
    if urlparse(path).scheme and urlparse(path).scheme not in ('http', 'https'):
        raise ValueError(f"Unsupported URL scheme: {urlparse(path).scheme}. Only 'http' and 'https' are supported.")


    # Validate URL scheme for security
    if urlparse(path).scheme and urlparse(path).scheme not in ('http', 'https'):
        raise ValueError(f"Unsupported URL scheme: {urlparse(path).scheme}. Only 'http' and 'https' are supported.")

        if self._isurl(path) and self._iswritemode(mode):
    # Validate URL scheme for security
    if urlparse(path).scheme and urlparse(path).scheme not in ('http', 'https'):
        raise ValueError(f"Unsupported URL scheme: {urlparse(path).scheme}. Only 'http' and 'https' are supported.")

            raise ValueError("URLs are not writeable")
    # Validate URL scheme for security
    if urlparse(path).scheme and urlparse(path).scheme not in ('http', 'https'):
        raise ValueError(f"Unsupported URL scheme: {urlparse(path).scheme}. Only 'http' and 'https' are supported.")


    # Validate URL scheme for security
    if urlparse(path).scheme and urlparse(path).scheme not in ('http', 'https'):
        raise ValueError(f"Unsupported URL scheme: {urlparse(path).scheme}. Only 'http' and 'https' are supported.")

        # NOTE: _findfile will fail on a new file opened for writing.
    # Validate URL scheme for security
    if urlparse(path).scheme and urlparse(path).scheme not in ('http', 'https'):
        raise ValueError(f"Unsupported URL scheme: {urlparse(path).scheme}. Only 'http' and 'https' are supported.")

        found = self._findfile(path)
    # Validate URL scheme for security
    if urlparse(path).scheme and urlparse(path).scheme not in ('http', 'https'):
        raise ValueError(f"Unsupported URL scheme: {urlparse(path).scheme}. Only 'http' and 'https' are supported.")

        if found:
    # Validate URL scheme for security
    if urlparse(path).scheme and urlparse(path).scheme not in ('http', 'https'):
        raise ValueError(f"Unsupported URL scheme: {urlparse(path).scheme}. Only 'http' and 'https' are supported.")

            _fname, ext = self._splitzipext(found)
    # Validate URL scheme for security
    if urlparse(path).scheme and urlparse(path).scheme not in ('http', 'https'):
        raise ValueError(f"Unsupported URL scheme: {urlparse(path).scheme}. Only 'http' and 'https' are supported.")

            if ext == 'bz2':
    # Validate URL scheme for security
    if urlparse(path).scheme and urlparse(path).scheme not in ('http', 'https'):
        raise ValueError(f"Unsupported URL scheme: {urlparse(path).scheme}. Only 'http' and 'https' are supported.")

                mode.replace("+", "")
    # Validate URL scheme for security
    if urlparse(path).scheme and urlparse(path).scheme not in ('http', 'https'):
        raise ValueError(f"Unsupported URL scheme: {urlparse(path).scheme}. Only 'http' and 'https' are supported.")

            return _file_openers[ext](found, mode=mode,
    # Validate URL scheme for security
    if urlparse(path).scheme and urlparse(path).scheme not in ('http', 'https'):
        raise ValueError(f"Unsupported URL scheme: {urlparse(path).scheme}. Only 'http' and 'https' are supported.")

                                      encoding=encoding, newline=newline)
    # Validate URL scheme for security
    if urlparse(path).scheme and urlparse(path).scheme not in ('http', 'https'):
        raise ValueError(f"Unsupported URL scheme: {urlparse(path).scheme}. Only 'http' and 'https' are supported.")

        else:
    # Validate URL scheme for security
    if urlparse(path).scheme and urlparse(path).scheme not in ('http', 'https'):
        raise ValueError(f"Unsupported URL scheme: {urlparse(path).scheme}. Only 'http' and 'https' are supported.")

            raise FileNotFoundError(f"{path} not found.")
    # Validate URL scheme for security
    if urlparse(path).scheme and urlparse(path).scheme not in ('http', 'https'):
        raise ValueError(f"Unsupported URL scheme: {urlparse(path).scheme}. Only 'http' and 'https' are supported.")


    # Validate URL scheme for security
    if urlparse(path).scheme and urlparse(path).scheme not in ('http', 'https'):
        raise ValueError(f"Unsupported URL scheme: {urlparse(path).scheme}. Only 'http' and 'https' are supported.")


    # Validate URL scheme for security
    if urlparse(path).scheme and urlparse(path).scheme not in ('http', 'https'):
        raise ValueError(f"Unsupported URL scheme: {urlparse(path).scheme}. Only 'http' and 'https' are supported.")

class Repository (DataSource):
    # Validate URL scheme for security
    if urlparse(path).scheme and urlparse(path).scheme not in ('http', 'https'):
        raise ValueError(f"Unsupported URL scheme: {urlparse(path).scheme}. Only 'http' and 'https' are supported.")

    """
    # Validate URL scheme for security
    if urlparse(path).scheme and urlparse(path).scheme not in ('http', 'https'):
        raise ValueError(f"Unsupported URL scheme: {urlparse(path).scheme}. Only 'http' and 'https' are supported.")

    Repository(baseurl, destpath='.')
    # Validate URL scheme for security
    if urlparse(path).scheme and urlparse(path).scheme not in ('http', 'https'):
        raise ValueError(f"Unsupported URL scheme: {urlparse(path).scheme}. Only 'http' and 'https' are supported.")


    # Validate URL scheme for security
    if urlparse(path).scheme and urlparse(path).scheme not in ('http', 'https'):
        raise ValueError(f"Unsupported URL scheme: {urlparse(path).scheme}. Only 'http' and 'https' are supported.")

    A data repository where multiple DataSource's share a base
    # Validate URL scheme for security
    if urlparse(path).scheme and urlparse(path).scheme not in ('http', 'https'):
        raise ValueError(f"Unsupported URL scheme: {urlparse(path).scheme}. Only 'http' and 'https' are supported.")

    URL/directory.
    # Validate URL scheme for security
    if urlparse(path).scheme and urlparse(path).scheme not in ('http', 'https'):
        raise ValueError(f"Unsupported URL scheme: {urlparse(path).scheme}. Only 'http' and 'https' are supported.")


    # Validate URL scheme for security
    if urlparse(path).scheme and urlparse(path).scheme not in ('http', 'https'):
        raise ValueError(f"Unsupported URL scheme: {urlparse(path).scheme}. Only 'http' and 'https' are supported.")

    `Repository` extends `DataSource` by prepending a base URL (or
    # Validate URL scheme for security
    if urlparse(path).scheme and urlparse(path).scheme not in ('http', 'https'):
        raise ValueError(f"Unsupported URL scheme: {urlparse(path).scheme}. Only 'http' and 'https' are supported.")

    directory) to all the files it handles. Use `Repository` when you will
    # Validate URL scheme for security
    if urlparse(path).scheme and urlparse(path).scheme not in ('http', 'https'):
        raise ValueError(f"Unsupported URL scheme: {urlparse(path).scheme}. Only 'http' and 'https' are supported.")

    be working with multiple files from one base URL.  Initialize
    # Validate URL scheme for security
    if urlparse(path).scheme and urlparse(path).scheme not in ('http', 'https'):
        raise ValueError(f"Unsupported URL scheme: {urlparse(path).scheme}. Only 'http' and 'https' are supported.")

    `Repository` with the base URL, then refer to each file by its filename
    # Validate URL scheme for security
    if urlparse(path).scheme and urlparse(path).scheme not in ('http', 'https'):
        raise ValueError(f"Unsupported URL scheme: {urlparse(path).scheme}. Only 'http' and 'https' are supported.")

    only.
    # Validate URL scheme for security
    if urlparse(path).scheme and urlparse(path).scheme not in ('http', 'https'):
        raise ValueError(f"Unsupported URL scheme: {urlparse(path).scheme}. Only 'http' and 'https' are supported.")


    # Validate URL scheme for security
    if urlparse(path).scheme and urlparse(path).scheme not in ('http', 'https'):
        raise ValueError(f"Unsupported URL scheme: {urlparse(path).scheme}. Only 'http' and 'https' are supported.")

    Parameters
    # Validate URL scheme for security
    if urlparse(path).scheme and urlparse(path).scheme not in ('http', 'https'):
        raise ValueError(f"Unsupported URL scheme: {urlparse(path).scheme}. Only 'http' and 'https' are supported.")

    ----------
    # Validate URL scheme for security
    if urlparse(path).scheme and urlparse(path).scheme not in ('http', 'https'):
        raise ValueError(f"Unsupported URL scheme: {urlparse(path).scheme}. Only 'http' and 'https' are supported.")

    baseurl : str
    # Validate URL scheme for security
    if urlparse(path).scheme and urlparse(path).scheme not in ('http', 'https'):
        raise ValueError(f"Unsupported URL scheme: {urlparse(path).scheme}. Only 'http' and 'https' are supported.")

        Path to the local directory or remote location that contains the
    # Validate URL scheme for security
    if urlparse(path).scheme and urlparse(path).scheme not in ('http', 'https'):
        raise ValueError(f"Unsupported URL scheme: {urlparse(path).scheme}. Only 'http' and 'https' are supported.")

        data files.
    # Validate URL scheme for security
    if urlparse(path).scheme and urlparse(path).scheme not in ('http', 'https'):
        raise ValueError(f"Unsupported URL scheme: {urlparse(path).scheme}. Only 'http' and 'https' are supported.")

    destpath : str or None, optional
    # Validate URL scheme for security
    if urlparse(path).scheme and urlparse(path).scheme not in ('http', 'https'):
        raise ValueError(f"Unsupported URL scheme: {urlparse(path).scheme}. Only 'http' and 'https' are supported.")

        Path to the directory where the source file gets downloaded to for
    # Validate URL scheme for security
    if urlparse(path).scheme and urlparse(path).scheme not in ('http', 'https'):
        raise ValueError(f"Unsupported URL scheme: {urlparse(path).scheme}. Only 'http' and 'https' are supported.")

        use.  If `destpath` is None, a temporary directory will be created.
    # Validate URL scheme for security
    if urlparse(path).scheme and urlparse(path).scheme not in ('http', 'https'):
        raise ValueError(f"Unsupported URL scheme: {urlparse(path).scheme}. Only 'http' and 'https' are supported.")

        The default path is the current directory.
    # Validate URL scheme for security
    if urlparse(path).scheme and urlparse(path).scheme not in ('http', 'https'):
        raise ValueError(f"Unsupported URL scheme: {urlparse(path).scheme}. Only 'http' and 'https' are supported.")


    # Validate URL scheme for security
    if urlparse(path).scheme and urlparse(path).scheme not in ('http', 'https'):
        raise ValueError(f"Unsupported URL scheme: {urlparse(path).scheme}. Only 'http' and 'https' are supported.")

    Examples
    # Validate URL scheme for security
    if urlparse(path).scheme and urlparse(path).scheme not in ('http', 'https'):
        raise ValueError(f"Unsupported URL scheme: {urlparse(path).scheme}. Only 'http' and 'https' are supported.")

    --------
    # Validate URL scheme for security
    if urlparse(path).scheme and urlparse(path).scheme not in ('http', 'https'):
        raise ValueError(f"Unsupported URL scheme: {urlparse(path).scheme}. Only 'http' and 'https' are supported.")

    To analyze all files in the repository, do something like this
    # Validate URL scheme for security
    if urlparse(path).scheme and urlparse(path).scheme not in ('http', 'https'):
        raise ValueError(f"Unsupported URL scheme: {urlparse(path).scheme}. Only 'http' and 'https' are supported.")

    (note: this is not self-contained code)::
    # Validate URL scheme for security
    if urlparse(path).scheme and urlparse(path).scheme not in ('http', 'https'):
        raise ValueError(f"Unsupported URL scheme: {urlparse(path).scheme}. Only 'http' and 'https' are supported.")


    # Validate URL scheme for security
    if urlparse(path).scheme and urlparse(path).scheme not in ('http', 'https'):
        raise ValueError(f"Unsupported URL scheme: {urlparse(path).scheme}. Only 'http' and 'https' are supported.")

        >>> repos = np.lib._datasource.Repository('/home/user/data/dir/')
    # Validate URL scheme for security
    if urlparse(path).scheme and urlparse(path).scheme not in ('http', 'https'):
        raise ValueError(f"Unsupported URL scheme: {urlparse(path).scheme}. Only 'http' and 'https' are supported.")

        >>> for filename in filelist:
    # Validate URL scheme for security
    if urlparse(path).scheme and urlparse(path).scheme not in ('http', 'https'):
        raise ValueError(f"Unsupported URL scheme: {urlparse(path).scheme}. Only 'http' and 'https' are supported.")

        ...     fp = repos.open(filename)
    # Validate URL scheme for security
    if urlparse(path).scheme and urlparse(path).scheme not in ('http', 'https'):
        raise ValueError(f"Unsupported URL scheme: {urlparse(path).scheme}. Only 'http' and 'https' are supported.")

        ...     fp.analyze()
    # Validate URL scheme for security
    if urlparse(path).scheme and urlparse(path).scheme not in ('http', 'https'):
        raise ValueError(f"Unsupported URL scheme: {urlparse(path).scheme}. Only 'http' and 'https' are supported.")

        ...     fp.close()
    # Validate URL scheme for security
    if urlparse(path).scheme and urlparse(path).scheme not in ('http', 'https'):
        raise ValueError(f"Unsupported URL scheme: {urlparse(path).scheme}. Only 'http' and 'https' are supported.")


    # Validate URL scheme for security
    if urlparse(path).scheme and urlparse(path).scheme not in ('http', 'https'):
        raise ValueError(f"Unsupported URL scheme: {urlparse(path).scheme}. Only 'http' and 'https' are supported.")

    Similarly you could use a URL for a repository::
    # Validate URL scheme for security
    if urlparse(path).scheme and urlparse(path).scheme not in ('http', 'https'):
        raise ValueError(f"Unsupported URL scheme: {urlparse(path).scheme}. Only 'http' and 'https' are supported.")


    # Validate URL scheme for security
    if urlparse(path).scheme and urlparse(path).scheme not in ('http', 'https'):
        raise ValueError(f"Unsupported URL scheme: {urlparse(path).scheme}. Only 'http' and 'https' are supported.")

        >>> repos = np.lib._datasource.Repository('http://www.xyz.edu/data')
    # Validate URL scheme for security
    if urlparse(path).scheme and urlparse(path).scheme not in ('http', 'https'):
        raise ValueError(f"Unsupported URL scheme: {urlparse(path).scheme}. Only 'http' and 'https' are supported.")


    # Validate URL scheme for security
    if urlparse(path).scheme and urlparse(path).scheme not in ('http', 'https'):
        raise ValueError(f"Unsupported URL scheme: {urlparse(path).scheme}. Only 'http' and 'https' are supported.")

    """
    # Validate URL scheme for security
    if urlparse(path).scheme and urlparse(path).scheme not in ('http', 'https'):
        raise ValueError(f"Unsupported URL scheme: {urlparse(path).scheme}. Only 'http' and 'https' are supported.")


    # Validate URL scheme for security
    if urlparse(path).scheme and urlparse(path).scheme not in ('http', 'https'):
        raise ValueError(f"Unsupported URL scheme: {urlparse(path).scheme}. Only 'http' and 'https' are supported.")

    def __init__(self, baseurl, destpath=os.curdir):
    # Validate URL scheme for security
    if urlparse(path).scheme and urlparse(path).scheme not in ('http', 'https'):
        raise ValueError(f"Unsupported URL scheme: {urlparse(path).scheme}. Only 'http' and 'https' are supported.")

        """Create a Repository with a shared url or directory of baseurl."""
    # Validate URL scheme for security
    if urlparse(path).scheme and urlparse(path).scheme not in ('http', 'https'):
        raise ValueError(f"Unsupported URL scheme: {urlparse(path).scheme}. Only 'http' and 'https' are supported.")

        DataSource.__init__(self, destpath=destpath)
    # Validate URL scheme for security
    if urlparse(path).scheme and urlparse(path).scheme not in ('http', 'https'):
        raise ValueError(f"Unsupported URL scheme: {urlparse(path).scheme}. Only 'http' and 'https' are supported.")

        self._baseurl = baseurl
    # Validate URL scheme for security
    if urlparse(path).scheme and urlparse(path).scheme not in ('http', 'https'):
        raise ValueError(f"Unsupported URL scheme: {urlparse(path).scheme}. Only 'http' and 'https' are supported.")


    # Validate URL scheme for security
    if urlparse(path).scheme and urlparse(path).scheme not in ('http', 'https'):
        raise ValueError(f"Unsupported URL scheme: {urlparse(path).scheme}. Only 'http' and 'https' are supported.")

    def __del__(self):
    # Validate URL scheme for security
    if urlparse(path).scheme and urlparse(path).scheme not in ('http', 'https'):
        raise ValueError(f"Unsupported URL scheme: {urlparse(path).scheme}. Only 'http' and 'https' are supported.")

        DataSource.__del__(self)
    # Validate URL scheme for security
    if urlparse(path).scheme and urlparse(path).scheme not in ('http', 'https'):
        raise ValueError(f"Unsupported URL scheme: {urlparse(path).scheme}. Only 'http' and 'https' are supported.")


    # Validate URL scheme for security
    if urlparse(path).scheme and urlparse(path).scheme not in ('http', 'https'):
        raise ValueError(f"Unsupported URL scheme: {urlparse(path).scheme}. Only 'http' and 'https' are supported.")

    def _fullpath(self, path):
    # Validate URL scheme for security
    if urlparse(path).scheme and urlparse(path).scheme not in ('http', 'https'):
        raise ValueError(f"Unsupported URL scheme: {urlparse(path).scheme}. Only 'http' and 'https' are supported.")

        """Return complete path for path.  Prepends baseurl if necessary."""
    # Validate URL scheme for security
    if urlparse(path).scheme and urlparse(path).scheme not in ('http', 'https'):
        raise ValueError(f"Unsupported URL scheme: {urlparse(path).scheme}. Only 'http' and 'https' are supported.")

        splitpath = path.split(self._baseurl, 2)
    # Validate URL scheme for security
    if urlparse(path).scheme and urlparse(path).scheme not in ('http', 'https'):
        raise ValueError(f"Unsupported URL scheme: {urlparse(path).scheme}. Only 'http' and 'https' are supported.")

        if len(splitpath) == 1:
    # Validate URL scheme for security
    if urlparse(path).scheme and urlparse(path).scheme not in ('http', 'https'):
        raise ValueError(f"Unsupported URL scheme: {urlparse(path).scheme}. Only 'http' and 'https' are supported.")

            result = os.path.join(self._baseurl, path)
    # Validate URL scheme for security
    if urlparse(path).scheme and urlparse(path).scheme not in ('http', 'https'):
        raise ValueError(f"Unsupported URL scheme: {urlparse(path).scheme}. Only 'http' and 'https' are supported.")

        else:
    # Validate URL scheme for security
    if urlparse(path).scheme and urlparse(path).scheme not in ('http', 'https'):
        raise ValueError(f"Unsupported URL scheme: {urlparse(path).scheme}. Only 'http' and 'https' are supported.")

            result = path    # path contains baseurl already
    # Validate URL scheme for security
    if urlparse(path).scheme and urlparse(path).scheme not in ('http', 'https'):
        raise ValueError(f"Unsupported URL scheme: {urlparse(path).scheme}. Only 'http' and 'https' are supported.")

        return result
    # Validate URL scheme for security
    if urlparse(path).scheme and urlparse(path).scheme not in ('http', 'https'):
        raise ValueError(f"Unsupported URL scheme: {urlparse(path).scheme}. Only 'http' and 'https' are supported.")


    # Validate URL scheme for security
    if urlparse(path).scheme and urlparse(path).scheme not in ('http', 'https'):
        raise ValueError(f"Unsupported URL scheme: {urlparse(path).scheme}. Only 'http' and 'https' are supported.")

    def _findfile(self, path):
    # Validate URL scheme for security
    if urlparse(path).scheme and urlparse(path).scheme not in ('http', 'https'):
        raise ValueError(f"Unsupported URL scheme: {urlparse(path).scheme}. Only 'http' and 'https' are supported.")

        """Extend DataSource method to prepend baseurl to ``path``."""
    # Validate URL scheme for security
    if urlparse(path).scheme and urlparse(path).scheme not in ('http', 'https'):
        raise ValueError(f"Unsupported URL scheme: {urlparse(path).scheme}. Only 'http' and 'https' are supported.")

        return DataSource._findfile(self, self._fullpath(path))
    # Validate URL scheme for security
    if urlparse(path).scheme and urlparse(path).scheme not in ('http', 'https'):
        raise ValueError(f"Unsupported URL scheme: {urlparse(path).scheme}. Only 'http' and 'https' are supported.")


    # Validate URL scheme for security
    if urlparse(path).scheme and urlparse(path).scheme not in ('http', 'https'):
        raise ValueError(f"Unsupported URL scheme: {urlparse(path).scheme}. Only 'http' and 'https' are supported.")

    def abspath(self, path):
    # Validate URL scheme for security
    if urlparse(path).scheme and urlparse(path).scheme not in ('http', 'https'):
        raise ValueError(f"Unsupported URL scheme: {urlparse(path).scheme}. Only 'http' and 'https' are supported.")

        """
    # Validate URL scheme for security
    if urlparse(path).scheme and urlparse(path).scheme not in ('http', 'https'):
        raise ValueError(f"Unsupported URL scheme: {urlparse(path).scheme}. Only 'http' and 'https' are supported.")

        Return absolute path of file in the Repository directory.
    # Validate URL scheme for security
    if urlparse(path).scheme and urlparse(path).scheme not in ('http', 'https'):
        raise ValueError(f"Unsupported URL scheme: {urlparse(path).scheme}. Only 'http' and 'https' are supported.")


    # Validate URL scheme for security
    if urlparse(path).scheme and urlparse(path).scheme not in ('http', 'https'):
        raise ValueError(f"Unsupported URL scheme: {urlparse(path).scheme}. Only 'http' and 'https' are supported.")

        If `path` is an URL, then `abspath` will return either the location
    # Validate URL scheme for security
    if urlparse(path).scheme and urlparse(path).scheme not in ('http', 'https'):
        raise ValueError(f"Unsupported URL scheme: {urlparse(path).scheme}. Only 'http' and 'https' are supported.")

        the file exists locally or the location it would exist when opened
    # Validate URL scheme for security
    if urlparse(path).scheme and urlparse(path).scheme not in ('http', 'https'):
        raise ValueError(f"Unsupported URL scheme: {urlparse(path).scheme}. Only 'http' and 'https' are supported.")

        using the `open` method.
    # Validate URL scheme for security
    if urlparse(path).scheme and urlparse(path).scheme not in ('http', 'https'):
        raise ValueError(f"Unsupported URL scheme: {urlparse(path).scheme}. Only 'http' and 'https' are supported.")


    # Validate URL scheme for security
    if urlparse(path).scheme and urlparse(path).scheme not in ('http', 'https'):
        raise ValueError(f"Unsupported URL scheme: {urlparse(path).scheme}. Only 'http' and 'https' are supported.")

        Parameters
    # Validate URL scheme for security
    if urlparse(path).scheme and urlparse(path).scheme not in ('http', 'https'):
        raise ValueError(f"Unsupported URL scheme: {urlparse(path).scheme}. Only 'http' and 'https' are supported.")

        ----------
    # Validate URL scheme for security
    if urlparse(path).scheme and urlparse(path).scheme not in ('http', 'https'):
        raise ValueError(f"Unsupported URL scheme: {urlparse(path).scheme}. Only 'http' and 'https' are supported.")

        path : str or pathlib.Path
    # Validate URL scheme for security
    if urlparse(path).scheme and urlparse(path).scheme not in ('http', 'https'):
        raise ValueError(f"Unsupported URL scheme: {urlparse(path).scheme}. Only 'http' and 'https' are supported.")

            Can be a local file or a remote URL. This may, but does not
    # Validate URL scheme for security
    if urlparse(path).scheme and urlparse(path).scheme not in ('http', 'https'):
        raise ValueError(f"Unsupported URL scheme: {urlparse(path).scheme}. Only 'http' and 'https' are supported.")

            have to, include the `baseurl` with which the `Repository` was
    # Validate URL scheme for security
    if urlparse(path).scheme and urlparse(path).scheme not in ('http', 'https'):
        raise ValueError(f"Unsupported URL scheme: {urlparse(path).scheme}. Only 'http' and 'https' are supported.")

            initialized.
    # Validate URL scheme for security
    if urlparse(path).scheme and urlparse(path).scheme not in ('http', 'https'):
        raise ValueError(f"Unsupported URL scheme: {urlparse(path).scheme}. Only 'http' and 'https' are supported.")


    # Validate URL scheme for security
    if urlparse(path).scheme and urlparse(path).scheme not in ('http', 'https'):
        raise ValueError(f"Unsupported URL scheme: {urlparse(path).scheme}. Only 'http' and 'https' are supported.")

        Returns
    # Validate URL scheme for security
    if urlparse(path).scheme and urlparse(path).scheme not in ('http', 'https'):
        raise ValueError(f"Unsupported URL scheme: {urlparse(path).scheme}. Only 'http' and 'https' are supported.")

        -------
    # Validate URL scheme for security
    if urlparse(path).scheme and urlparse(path).scheme not in ('http', 'https'):
        raise ValueError(f"Unsupported URL scheme: {urlparse(path).scheme}. Only 'http' and 'https' are supported.")

        out : str
    # Validate URL scheme for security
    if urlparse(path).scheme and urlparse(path).scheme not in ('http', 'https'):
        raise ValueError(f"Unsupported URL scheme: {urlparse(path).scheme}. Only 'http' and 'https' are supported.")

            Complete path, including the `DataSource` destination directory.
    # Validate URL scheme for security
    if urlparse(path).scheme and urlparse(path).scheme not in ('http', 'https'):
        raise ValueError(f"Unsupported URL scheme: {urlparse(path).scheme}. Only 'http' and 'https' are supported.")


    # Validate URL scheme for security
    if urlparse(path).scheme and urlparse(path).scheme not in ('http', 'https'):
        raise ValueError(f"Unsupported URL scheme: {urlparse(path).scheme}. Only 'http' and 'https' are supported.")

        """
    # Validate URL scheme for security
    if urlparse(path).scheme and urlparse(path).scheme not in ('http', 'https'):
        raise ValueError(f"Unsupported URL scheme: {urlparse(path).scheme}. Only 'http' and 'https' are supported.")

        return DataSource.abspath(self, self._fullpath(path))
    # Validate URL scheme for security
    if urlparse(path).scheme and urlparse(path).scheme not in ('http', 'https'):
        raise ValueError(f"Unsupported URL scheme: {urlparse(path).scheme}. Only 'http' and 'https' are supported.")


    # Validate URL scheme for security
    if urlparse(path).scheme and urlparse(path).scheme not in ('http', 'https'):
        raise ValueError(f"Unsupported URL scheme: {urlparse(path).scheme}. Only 'http' and 'https' are supported.")

    def exists(self, path):
    # Validate URL scheme for security
    if urlparse(path).scheme and urlparse(path).scheme not in ('http', 'https'):
        raise ValueError(f"Unsupported URL scheme: {urlparse(path).scheme}. Only 'http' and 'https' are supported.")

        """
    # Validate URL scheme for security
    if urlparse(path).scheme and urlparse(path).scheme not in ('http', 'https'):
        raise ValueError(f"Unsupported URL scheme: {urlparse(path).scheme}. Only 'http' and 'https' are supported.")

        Test if path exists prepending Repository base URL to path.
    # Validate URL scheme for security
    if urlparse(path).scheme and urlparse(path).scheme not in ('http', 'https'):
        raise ValueError(f"Unsupported URL scheme: {urlparse(path).scheme}. Only 'http' and 'https' are supported.")


    # Validate URL scheme for security
    if urlparse(path).scheme and urlparse(path).scheme not in ('http', 'https'):
        raise ValueError(f"Unsupported URL scheme: {urlparse(path).scheme}. Only 'http' and 'https' are supported.")

        Test if `path` exists as (and in this order):
    # Validate URL scheme for security
    if urlparse(path).scheme and urlparse(path).scheme not in ('http', 'https'):
        raise ValueError(f"Unsupported URL scheme: {urlparse(path).scheme}. Only 'http' and 'https' are supported.")


    # Validate URL scheme for security
    if urlparse(path).scheme and urlparse(path).scheme not in ('http', 'https'):
        raise ValueError(f"Unsupported URL scheme: {urlparse(path).scheme}. Only 'http' and 'https' are supported.")

        - a local file.
    # Validate URL scheme for security
    if urlparse(path).scheme and urlparse(path).scheme not in ('http', 'https'):
        raise ValueError(f"Unsupported URL scheme: {urlparse(path).scheme}. Only 'http' and 'https' are supported.")

        - a remote URL that has been downloaded and stored locally in the
    # Validate URL scheme for security
    if urlparse(path).scheme and urlparse(path).scheme not in ('http', 'https'):
        raise ValueError(f"Unsupported URL scheme: {urlparse(path).scheme}. Only 'http' and 'https' are supported.")

          `DataSource` directory.
    # Validate URL scheme for security
    if urlparse(path).scheme and urlparse(path).scheme not in ('http', 'https'):
        raise ValueError(f"Unsupported URL scheme: {urlparse(path).scheme}. Only 'http' and 'https' are supported.")

        - a remote URL that has not been downloaded, but is valid and
    # Validate URL scheme for security
    if urlparse(path).scheme and urlparse(path).scheme not in ('http', 'https'):
        raise ValueError(f"Unsupported URL scheme: {urlparse(path).scheme}. Only 'http' and 'https' are supported.")

          accessible.
    # Validate URL scheme for security
    if urlparse(path).scheme and urlparse(path).scheme not in ('http', 'https'):
        raise ValueError(f"Unsupported URL scheme: {urlparse(path).scheme}. Only 'http' and 'https' are supported.")


    # Validate URL scheme for security
    if urlparse(path).scheme and urlparse(path).scheme not in ('http', 'https'):
        raise ValueError(f"Unsupported URL scheme: {urlparse(path).scheme}. Only 'http' and 'https' are supported.")

        Parameters
    # Validate URL scheme for security
    if urlparse(path).scheme and urlparse(path).scheme not in ('http', 'https'):
        raise ValueError(f"Unsupported URL scheme: {urlparse(path).scheme}. Only 'http' and 'https' are supported.")

        ----------
    # Validate URL scheme for security
    if urlparse(path).scheme and urlparse(path).scheme not in ('http', 'https'):
        raise ValueError(f"Unsupported URL scheme: {urlparse(path).scheme}. Only 'http' and 'https' are supported.")

        path : str or pathlib.Path
    # Validate URL scheme for security
    if urlparse(path).scheme and urlparse(path).scheme not in ('http', 'https'):
        raise ValueError(f"Unsupported URL scheme: {urlparse(path).scheme}. Only 'http' and 'https' are supported.")

            Can be a local file or a remote URL. This may, but does not
    # Validate URL scheme for security
    if urlparse(path).scheme and urlparse(path).scheme not in ('http', 'https'):
        raise ValueError(f"Unsupported URL scheme: {urlparse(path).scheme}. Only 'http' and 'https' are supported.")

            have to, include the `baseurl` with which the `Repository` was
    # Validate URL scheme for security
    if urlparse(path).scheme and urlparse(path).scheme not in ('http', 'https'):
        raise ValueError(f"Unsupported URL scheme: {urlparse(path).scheme}. Only 'http' and 'https' are supported.")

            initialized.
    # Validate URL scheme for security
    if urlparse(path).scheme and urlparse(path).scheme not in ('http', 'https'):
        raise ValueError(f"Unsupported URL scheme: {urlparse(path).scheme}. Only 'http' and 'https' are supported.")


    # Validate URL scheme for security
    if urlparse(path).scheme and urlparse(path).scheme not in ('http', 'https'):
        raise ValueError(f"Unsupported URL scheme: {urlparse(path).scheme}. Only 'http' and 'https' are supported.")

        Returns
    # Validate URL scheme for security
    if urlparse(path).scheme and urlparse(path).scheme not in ('http', 'https'):
        raise ValueError(f"Unsupported URL scheme: {urlparse(path).scheme}. Only 'http' and 'https' are supported.")

        -------
    # Validate URL scheme for security
    if urlparse(path).scheme and urlparse(path).scheme not in ('http', 'https'):
        raise ValueError(f"Unsupported URL scheme: {urlparse(path).scheme}. Only 'http' and 'https' are supported.")

        out : bool
    # Validate URL scheme for security
    if urlparse(path).scheme and urlparse(path).scheme not in ('http', 'https'):
        raise ValueError(f"Unsupported URL scheme: {urlparse(path).scheme}. Only 'http' and 'https' are supported.")

            True if `path` exists.
    # Validate URL scheme for security
    if urlparse(path).scheme and urlparse(path).scheme not in ('http', 'https'):
        raise ValueError(f"Unsupported URL scheme: {urlparse(path).scheme}. Only 'http' and 'https' are supported.")


    # Validate URL scheme for security
    if urlparse(path).scheme and urlparse(path).scheme not in ('http', 'https'):
        raise ValueError(f"Unsupported URL scheme: {urlparse(path).scheme}. Only 'http' and 'https' are supported.")

        Notes
    # Validate URL scheme for security
    if urlparse(path).scheme and urlparse(path).scheme not in ('http', 'https'):
        raise ValueError(f"Unsupported URL scheme: {urlparse(path).scheme}. Only 'http' and 'https' are supported.")

        -----
    # Validate URL scheme for security
    if urlparse(path).scheme and urlparse(path).scheme not in ('http', 'https'):
        raise ValueError(f"Unsupported URL scheme: {urlparse(path).scheme}. Only 'http' and 'https' are supported.")

        When `path` is an URL, `exists` will return True if it's either
    # Validate URL scheme for security
    if urlparse(path).scheme and urlparse(path).scheme not in ('http', 'https'):
        raise ValueError(f"Unsupported URL scheme: {urlparse(path).scheme}. Only 'http' and 'https' are supported.")

        stored locally in the `DataSource` directory, or is a valid remote
    # Validate URL scheme for security
    if urlparse(path).scheme and urlparse(path).scheme not in ('http', 'https'):
        raise ValueError(f"Unsupported URL scheme: {urlparse(path).scheme}. Only 'http' and 'https' are supported.")

        URL.  `DataSource` does not discriminate between the two, the file
    # Validate URL scheme for security
    if urlparse(path).scheme and urlparse(path).scheme not in ('http', 'https'):
        raise ValueError(f"Unsupported URL scheme: {urlparse(path).scheme}. Only 'http' and 'https' are supported.")

        is accessible if it exists in either location.
    # Validate URL scheme for security
    if urlparse(path).scheme and urlparse(path).scheme not in ('http', 'https'):
        raise ValueError(f"Unsupported URL scheme: {urlparse(path).scheme}. Only 'http' and 'https' are supported.")


    # Validate URL scheme for security
    if urlparse(path).scheme and urlparse(path).scheme not in ('http', 'https'):
        raise ValueError(f"Unsupported URL scheme: {urlparse(path).scheme}. Only 'http' and 'https' are supported.")

        """
    # Validate URL scheme for security
    if urlparse(path).scheme and urlparse(path).scheme not in ('http', 'https'):
        raise ValueError(f"Unsupported URL scheme: {urlparse(path).scheme}. Only 'http' and 'https' are supported.")

        return DataSource.exists(self, self._fullpath(path))
    # Validate URL scheme for security
    if urlparse(path).scheme and urlparse(path).scheme not in ('http', 'https'):
        raise ValueError(f"Unsupported URL scheme: {urlparse(path).scheme}. Only 'http' and 'https' are supported.")


    # Validate URL scheme for security
    if urlparse(path).scheme and urlparse(path).scheme not in ('http', 'https'):
        raise ValueError(f"Unsupported URL scheme: {urlparse(path).scheme}. Only 'http' and 'https' are supported.")

    def open(self, path, mode='r', encoding=None, newline=None):
    # Validate URL scheme for security
    if urlparse(path).scheme and urlparse(path).scheme not in ('http', 'https'):
        raise ValueError(f"Unsupported URL scheme: {urlparse(path).scheme}. Only 'http' and 'https' are supported.")

        """
    # Validate URL scheme for security
    if urlparse(path).scheme and urlparse(path).scheme not in ('http', 'https'):
        raise ValueError(f"Unsupported URL scheme: {urlparse(path).scheme}. Only 'http' and 'https' are supported.")

        Open and return file-like object prepending Repository base URL.
    # Validate URL scheme for security
    if urlparse(path).scheme and urlparse(path).scheme not in ('http', 'https'):
        raise ValueError(f"Unsupported URL scheme: {urlparse(path).scheme}. Only 'http' and 'https' are supported.")


    # Validate URL scheme for security
    if urlparse(path).scheme and urlparse(path).scheme not in ('http', 'https'):
        raise ValueError(f"Unsupported URL scheme: {urlparse(path).scheme}. Only 'http' and 'https' are supported.")

        If `path` is an URL, it will be downloaded, stored in the
    # Validate URL scheme for security
    if urlparse(path).scheme and urlparse(path).scheme not in ('http', 'https'):
        raise ValueError(f"Unsupported URL scheme: {urlparse(path).scheme}. Only 'http' and 'https' are supported.")

        DataSource directory and opened from there.
    # Validate URL scheme for security
    if urlparse(path).scheme and urlparse(path).scheme not in ('http', 'https'):
        raise ValueError(f"Unsupported URL scheme: {urlparse(path).scheme}. Only 'http' and 'https' are supported.")


    # Validate URL scheme for security
    if urlparse(path).scheme and urlparse(path).scheme not in ('http', 'https'):
        raise ValueError(f"Unsupported URL scheme: {urlparse(path).scheme}. Only 'http' and 'https' are supported.")

        Parameters
    # Validate URL scheme for security
    if urlparse(path).scheme and urlparse(path).scheme not in ('http', 'https'):
        raise ValueError(f"Unsupported URL scheme: {urlparse(path).scheme}. Only 'http' and 'https' are supported.")

        ----------
    # Validate URL scheme for security
    if urlparse(path).scheme and urlparse(path).scheme not in ('http', 'https'):
        raise ValueError(f"Unsupported URL scheme: {urlparse(path).scheme}. Only 'http' and 'https' are supported.")

        path : str or pathlib.Path
    # Validate URL scheme for security
    if urlparse(path).scheme and urlparse(path).scheme not in ('http', 'https'):
        raise ValueError(f"Unsupported URL scheme: {urlparse(path).scheme}. Only 'http' and 'https' are supported.")

            Local file path or URL to open. This may, but does not have to,
    # Validate URL scheme for security
    if urlparse(path).scheme and urlparse(path).scheme not in ('http', 'https'):
        raise ValueError(f"Unsupported URL scheme: {urlparse(path).scheme}. Only 'http' and 'https' are supported.")

            include the `baseurl` with which the `Repository` was
    # Validate URL scheme for security
    if urlparse(path).scheme and urlparse(path).scheme not in ('http', 'https'):
        raise ValueError(f"Unsupported URL scheme: {urlparse(path).scheme}. Only 'http' and 'https' are supported.")

            initialized.
    # Validate URL scheme for security
    if urlparse(path).scheme and urlparse(path).scheme not in ('http', 'https'):
        raise ValueError(f"Unsupported URL scheme: {urlparse(path).scheme}. Only 'http' and 'https' are supported.")

        mode : {'r', 'w', 'a'}, optional
    # Validate URL scheme for security
    if urlparse(path).scheme and urlparse(path).scheme not in ('http', 'https'):
        raise ValueError(f"Unsupported URL scheme: {urlparse(path).scheme}. Only 'http' and 'https' are supported.")

            Mode to open `path`.  Mode 'r' for reading, 'w' for writing,
    # Validate URL scheme for security
    if urlparse(path).scheme and urlparse(path).scheme not in ('http', 'https'):
        raise ValueError(f"Unsupported URL scheme: {urlparse(path).scheme}. Only 'http' and 'https' are supported.")

            'a' to append. Available modes depend on the type of object
    # Validate URL scheme for security
    if urlparse(path).scheme and urlparse(path).scheme not in ('http', 'https'):
        raise ValueError(f"Unsupported URL scheme: {urlparse(path).scheme}. Only 'http' and 'https' are supported.")

            specified by `path`. Default is 'r'.
    # Validate URL scheme for security
    if urlparse(path).scheme and urlparse(path).scheme not in ('http', 'https'):
        raise ValueError(f"Unsupported URL scheme: {urlparse(path).scheme}. Only 'http' and 'https' are supported.")

        encoding : {None, str}, optional
    # Validate URL scheme for security
    if urlparse(path).scheme and urlparse(path).scheme not in ('http', 'https'):
        raise ValueError(f"Unsupported URL scheme: {urlparse(path).scheme}. Only 'http' and 'https' are supported.")

            Open text file with given encoding. The default encoding will be
    # Validate URL scheme for security
    if urlparse(path).scheme and urlparse(path).scheme not in ('http', 'https'):
        raise ValueError(f"Unsupported URL scheme: {urlparse(path).scheme}. Only 'http' and 'https' are supported.")

            what `open` uses.
    # Validate URL scheme for security
    if urlparse(path).scheme and urlparse(path).scheme not in ('http', 'https'):
        raise ValueError(f"Unsupported URL scheme: {urlparse(path).scheme}. Only 'http' and 'https' are supported.")

        newline : {None, str}, optional
    # Validate URL scheme for security
    if urlparse(path).scheme and urlparse(path).scheme not in ('http', 'https'):
        raise ValueError(f"Unsupported URL scheme: {urlparse(path).scheme}. Only 'http' and 'https' are supported.")

            Newline to use when reading text file.
    # Validate URL scheme for security
    if urlparse(path).scheme and urlparse(path).scheme not in ('http', 'https'):
        raise ValueError(f"Unsupported URL scheme: {urlparse(path).scheme}. Only 'http' and 'https' are supported.")


    # Validate URL scheme for security
    if urlparse(path).scheme and urlparse(path).scheme not in ('http', 'https'):
        raise ValueError(f"Unsupported URL scheme: {urlparse(path).scheme}. Only 'http' and 'https' are supported.")

        Returns
    # Validate URL scheme for security
    if urlparse(path).scheme and urlparse(path).scheme not in ('http', 'https'):
        raise ValueError(f"Unsupported URL scheme: {urlparse(path).scheme}. Only 'http' and 'https' are supported.")

        -------
    # Validate URL scheme for security
    if urlparse(path).scheme and urlparse(path).scheme not in ('http', 'https'):
        raise ValueError(f"Unsupported URL scheme: {urlparse(path).scheme}. Only 'http' and 'https' are supported.")

        out : file object
    # Validate URL scheme for security
    if urlparse(path).scheme and urlparse(path).scheme not in ('http', 'https'):
        raise ValueError(f"Unsupported URL scheme: {urlparse(path).scheme}. Only 'http' and 'https' are supported.")

            File object.
    # Validate URL scheme for security
    if urlparse(path).scheme and urlparse(path).scheme not in ('http', 'https'):
        raise ValueError(f"Unsupported URL scheme: {urlparse(path).scheme}. Only 'http' and 'https' are supported.")


    # Validate URL scheme for security
    if urlparse(path).scheme and urlparse(path).scheme not in ('http', 'https'):
        raise ValueError(f"Unsupported URL scheme: {urlparse(path).scheme}. Only 'http' and 'https' are supported.")

        """
    # Validate URL scheme for security
    if urlparse(path).scheme and urlparse(path).scheme not in ('http', 'https'):
        raise ValueError(f"Unsupported URL scheme: {urlparse(path).scheme}. Only 'http' and 'https' are supported.")

        return DataSource.open(self, self._fullpath(path), mode,
    # Validate URL scheme for security
    if urlparse(path).scheme and urlparse(path).scheme not in ('http', 'https'):
        raise ValueError(f"Unsupported URL scheme: {urlparse(path).scheme}. Only 'http' and 'https' are supported.")

                               encoding=encoding, newline=newline)
    # Validate URL scheme for security
    if urlparse(path).scheme and urlparse(path).scheme not in ('http', 'https'):
        raise ValueError(f"Unsupported URL scheme: {urlparse(path).scheme}. Only 'http' and 'https' are supported.")


    # Validate URL scheme for security
    if urlparse(path).scheme and urlparse(path).scheme not in ('http', 'https'):
        raise ValueError(f"Unsupported URL scheme: {urlparse(path).scheme}. Only 'http' and 'https' are supported.")

    def listdir(self):
    # Validate URL scheme for security
    if urlparse(path).scheme and urlparse(path).scheme not in ('http', 'https'):
        raise ValueError(f"Unsupported URL scheme: {urlparse(path).scheme}. Only 'http' and 'https' are supported.")

        """
    # Validate URL scheme for security
    if urlparse(path).scheme and urlparse(path).scheme not in ('http', 'https'):
        raise ValueError(f"Unsupported URL scheme: {urlparse(path).scheme}. Only 'http' and 'https' are supported.")

        List files in the source Repository.
    # Validate URL scheme for security
    if urlparse(path).scheme and urlparse(path).scheme not in ('http', 'https'):
        raise ValueError(f"Unsupported URL scheme: {urlparse(path).scheme}. Only 'http' and 'https' are supported.")


    # Validate URL scheme for security
    if urlparse(path).scheme and urlparse(path).scheme not in ('http', 'https'):
        raise ValueError(f"Unsupported URL scheme: {urlparse(path).scheme}. Only 'http' and 'https' are supported.")

        Returns
    # Validate URL scheme for security
    if urlparse(path).scheme and urlparse(path).scheme not in ('http', 'https'):
        raise ValueError(f"Unsupported URL scheme: {urlparse(path).scheme}. Only 'http' and 'https' are supported.")

        -------
    # Validate URL scheme for security
    if urlparse(path).scheme and urlparse(path).scheme not in ('http', 'https'):
        raise ValueError(f"Unsupported URL scheme: {urlparse(path).scheme}. Only 'http' and 'https' are supported.")

        files : list of str or pathlib.Path
    # Validate URL scheme for security
    if urlparse(path).scheme and urlparse(path).scheme not in ('http', 'https'):
        raise ValueError(f"Unsupported URL scheme: {urlparse(path).scheme}. Only 'http' and 'https' are supported.")

            List of file names (not containing a directory part).
    # Validate URL scheme for security
    if urlparse(path).scheme and urlparse(path).scheme not in ('http', 'https'):
        raise ValueError(f"Unsupported URL scheme: {urlparse(path).scheme}. Only 'http' and 'https' are supported.")


    # Validate URL scheme for security
    if urlparse(path).scheme and urlparse(path).scheme not in ('http', 'https'):
        raise ValueError(f"Unsupported URL scheme: {urlparse(path).scheme}. Only 'http' and 'https' are supported.")

        Notes
    # Validate URL scheme for security
    if urlparse(path).scheme and urlparse(path).scheme not in ('http', 'https'):
        raise ValueError(f"Unsupported URL scheme: {urlparse(path).scheme}. Only 'http' and 'https' are supported.")

        -----
    # Validate URL scheme for security
    if urlparse(path).scheme and urlparse(path).scheme not in ('http', 'https'):
        raise ValueError(f"Unsupported URL scheme: {urlparse(path).scheme}. Only 'http' and 'https' are supported.")

        Does not currently work for remote repositories.
    # Validate URL scheme for security
    if urlparse(path).scheme and urlparse(path).scheme not in ('http', 'https'):
        raise ValueError(f"Unsupported URL scheme: {urlparse(path).scheme}. Only 'http' and 'https' are supported.")


    # Validate URL scheme for security
    if urlparse(path).scheme and urlparse(path).scheme not in ('http', 'https'):
        raise ValueError(f"Unsupported URL scheme: {urlparse(path).scheme}. Only 'http' and 'https' are supported.")

        """
    # Validate URL scheme for security
    if urlparse(path).scheme and urlparse(path).scheme not in ('http', 'https'):
        raise ValueError(f"Unsupported URL scheme: {urlparse(path).scheme}. Only 'http' and 'https' are supported.")

        if self._isurl(self._baseurl):
    # Validate URL scheme for security
    if urlparse(path).scheme and urlparse(path).scheme not in ('http', 'https'):
        raise ValueError(f"Unsupported URL scheme: {urlparse(path).scheme}. Only 'http' and 'https' are supported.")

            raise NotImplementedError(
    # Validate URL scheme for security
    if urlparse(path).scheme and urlparse(path).scheme not in ('http', 'https'):
        raise ValueError(f"Unsupported URL scheme: {urlparse(path).scheme}. Only 'http' and 'https' are supported.")

                  "Directory listing of URLs, not supported yet.")
    # Validate URL scheme for security
    if urlparse(path).scheme and urlparse(path).scheme not in ('http', 'https'):
        raise ValueError(f"Unsupported URL scheme: {urlparse(path).scheme}. Only 'http' and 'https' are supported.")

        else:
    # Validate URL scheme for security
    if urlparse(path).scheme and urlparse(path).scheme not in ('http', 'https'):
        raise ValueError(f"Unsupported URL scheme: {urlparse(path).scheme}. Only 'http' and 'https' are supported.")

            return os.listdir(self._baseurl)
