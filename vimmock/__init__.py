"""
vim mock object for easier testing of vim plugins written in Python.
"""
from vimmock.mocked import VimMock


__all__ = ['VimMock']
__version__ = '0.2.0.dev'


VERSION = __version__.split('.')


def get_version():
    """
    Returns shorter version (digit parts only) as string.
    """
    return '.'.join((str(each) for each in VERSION[:4]))


def patch_vim():
    """
    Sets new ``VimMock`` instance under ``vim`` key within ``sys.modules``.
    """
    import sys
    sys.modules['vim'] = VimMock()
