"""
two1-httpie: a 21BC fork of httpie

"""
__author__ = 'Ian Chen'
__version__ = '0.0.1'
__licence__ = 'BSD'


class ExitStatus:
    """Exit status code constants."""
    OK = 0
    ERROR = 1
    ERROR_TIMEOUT = 2

    # Used only when requested with --check-status:
    ERROR_HTTP_3XX = 3
    ERROR_HTTP_4XX = 4
    ERROR_HTTP_5XX = 5
