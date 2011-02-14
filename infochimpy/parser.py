# infochimpy
# Please see LICENSE

import logging

from error import ChimpsError

def import_simplejson():
    '''Find a JSON parser'''
    try:
        import simplejson
        parse_json = lambda s: simplejson.loads(s.decode("utf-8"), strict=False)
    except ImportError:
        try:
            import cjson
            parse_json = lambda s: cjson.decode(s.decode("utf-8"), True)
        except ImportError:
            # For Google AppEngine
            from django.utils import simplejson
            parse_json = lambda s: simplejson.loads(s.decode("utf-8"))
    return parse_json
    
class Parse(object):

    def parse(self, method, payload):
        """
        Parse the response payload and return the result
        """
        raise NotImplementedError

    def parse_error(self, payload):
        """
        Parse the error message from payload.
        """
        raise NotImplementedError

class JSONParser(Parse):

    payload_format = 'json'

    def __init__(self):
        self.json_lib = import_simplejson()

    def parse(self, method, payload):
        try:
            json = self.json_lib.loads(payload)
        except Exception, e:
            raise ChimpsError('Failed to parse JSON payload: %s' % e)
        return json

    def parse_error(self, payload):
        error = self.json_lib.loads(payload)
        if error.has_key('error'):
            return error['error']
        else:
            return error['errors']
            
class XMLParser(Parse):

    payload_format = 'xml'

    def __init__(self):
        pass
        
    def parse(self, action, payload):
        pass
        
    def parse_error(self, payload):
        pass
