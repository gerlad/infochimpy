# infochimpy
# Copyright 2011 Gerald McCollam
# Portions Copyright 2009-2010 Joshua Roesslein

# Please see license.txt.

from infochimpy.api import API
from infochimpy.auth import NoAuth
import logging

# Global, unauthenticated instance of API
api = API(NoAuth())
debug_level = 3

def debug(level=debug_level):
    import httplib
    httplib.HTTPConnection.debuglevel = level