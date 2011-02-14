# infochimpy
# Please see LICENSE

from infochimpy.api import API
from infochimpy.auth import NoAuth
import logging

# Global, unauthenticated instance of API
api = API(NoAuth())
debug_level = 3

def debug(level=debug_level):
    import httplib
    httplib.HTTPConnection.debuglevel = level