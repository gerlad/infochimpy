# infochimpy
# Please see LICENSE

import urllib
from base64 import encodestring
import oauth2 as oauth


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
    ''' For now, this function does OAuth authentication
        directly to Twitter, for doing bulk lookups of 
        screen_names for user_ids. Not sure if Infochimps does
        this. I should probably ask.'''
    pass