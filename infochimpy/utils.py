# infochimpy
# Copyright 2011 Gerald McCollam
# Portions Copyright 2009-2010 Joshua Roesslein

# Please see license.txt.

import re
import urlparse
            
def convert_to_utf8_str(arg):
    # written by Michael Norton (http://docondev.blogspot.com/)
    if isinstance(arg, unicode):
        arg = arg.encode('utf-8')
    elif not isinstance(arg, str):
        arg = str(arg)
    return arg
    
def encode_post_data_dict( post_data ):
    data = []
    for key in post_data.keys():
        data.append( urlencode(key) +'='+ urlencode(post_data[key]) )
    return '&'.join(data)

def encode_post_data( post_data ):
    data = []
    for x in post_data:
        data.append( urlencode(x[0]) +'='+ urlencode(x[1]) )
    return '&'.join(data)
                
def parse_url(url):
    """
    Given a URL, returns a 4-tuple containing the hostname, port,
    a path relative to root (if any), and a boolean representing 
    whether the connection should use SSL or not.
    """
    (scheme, netloc, path, params, query, frag) = urlparse.urlparse(url)

    # We only support web services
    if not scheme in ('http', 'https'):
        raise InvalidUrl('Scheme must be one of http or https')

    is_ssl = scheme == 'https' and True or False

    # Verify hostnames are valid and parse a port spec (if any)
    match = re.match('([a-zA-Z0-9\-\.]+):?([0-9]{2,5})?', netloc)

    if match:
        (host, port) = match.groups()
        if not port:
            port = is_ssl and '443' or '80'
    else:
        raise InvalidUrl('Invalid host and/or port: %s' % netloc)

    return (host, int(port), path.strip('/'), is_ssl)
    
