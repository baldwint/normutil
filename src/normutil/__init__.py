try:
    from setuptools_scm import get_version

    # We are in a dev environment and can recalculate a fresh version number
    __version__ = get_version(root="../..", relative_to=__file__)
    del get_version
except (ImportError, LookupError):
    # Otherwise, use the version that was written the last time setup.py ran
    from ._version import __version__
