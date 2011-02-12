# infochimpy
# Copyright 2011 Gerald McCollam
# Portions Copyright 2009-2010 Joshua Roesslein

# Please see license.txt.

import httplib
import urllib
import urllib2
import time
import re
import logging

from infochimpy.error import ChimpsError
from infochimpy.utils import convert_to_utf8_str
from infochimpy.parser import import_simplejson

re_path_template = re.compile('{\w+}')

log = logging.getLogger('infochimpy')
console = logging.StreamHandler()
log.addHandler(console)
log.setLevel(logging.DEBUG)
        
def bind_api(**config):

    class APIMethod(object):

        path = config['path']
        payload_type = config.get('payload_type', None)
        required_params = config.get('required_params', [])
        method = config.get('method', 'GET')
        require_auth = config.get('require_auth', True)
        
        def __init__(self, api, args, kargs):

            if self.require_auth and not api.auth:
                raise ChimpsError('Authentication required.')

            self.api = api
            self.host = api.host
            self.format = api.format
            self.apikey = api.get_user_key()
            self.screen_name = api.get_user_screen_name()

            if api.secure:
                self.scheme = 'https://'
            else:
                self.scheme = 'http://'
                
            self.build_query(args, kargs)

            if (self.format not in ("json", "xml", "")):
                raise ValueError("Unknown data format '%s'" %(format))

        def build_query(self, args, kargs):
            # build query parameters
            self.parameters = {}
            if args:
                for idx, arg in enumerate(args):
                    self.parameters[self.required_params[idx]] = convert_to_utf8_str(arg)
            else:
                if self.required_params:
                    pass # Exception. get default argument list from config?
            
        def execute(self):
            # Build the request
            global resp, conn
            base = '%s%s%s' % (self.scheme, self.host, self.path)
            
            if len(self.parameters):
                url = '%s?%s' % (base, urllib.urlencode(self.parameters))
            
            if self.api.secure:
                conn = httplib.HTTPSConnection(self.host)
            else:
                conn = httplib.HTTPConnection(self.host)
            
            # Execute
            try:
                conn.request(self.method, url)
                resp = conn.getresponse()
            except Exception, e:
                raise ChimpsError('Failed to send request: %s' % e)

            if resp.status != 200:
                try:
                    error_msg = self.api.parser.parse_error(resp.read())
                except Exception:
                    error_msg = "Infochimps response: status code = %s" % resp.status
                raise ChimpsError(error_msg, resp)

            # Read response
            result = resp.read()
            # Clean up
            conn.close()
            
            parse_json = import_simplejson()
            
            # Parse response
            result = parse_json(result)
            return result

    def _call(api, *args, **kargs):
        method = APIMethod(api, args, kargs)
        return method.execute()

    return _call