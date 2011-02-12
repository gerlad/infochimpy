# infochimpy
# Copyright 2011 Gerald McCollam
# Portions Copyright 2009-2010 Joshua Roesslein

# Please see license.txt.

import urllib
from base64 import encodestring

class Auth(object):
    """
    Authenticator objects.
    """
    def encode_params(self, base_url, method, params):
        """Encodes parameters for a request suitable for including in a URL."""
        raise NotImplementedError()

    def generate_headers(self):
        """Generates headers which should be added to the request if required."""
        raise NotImplementedError()

class NoAuth(Auth):
    """
    No authentication authenticator.
    """
    def __init__(self):
        pass
        
    def encode_params(self, base_url, method, params):
        return urllib.urlencode(params)

    def generate_headers(self):
        return {}

class BasicAuthHandler(Auth):
    pass
    
class OAuthHandler(Auth):
    pass