# infochimpy
# Please see LICENSE

import os
from ConfigParser import ConfigParser

from infochimpy.bind import bind_api
from infochimpy.error import ChimpsError
from infochimpy.utils import *

config = ConfigParser()
chimps_config = os.path.join(os.environ['HOME'], '.infochimpy')

try:
    config.read([chimps_config])
except:
    pass
    
class API(object):

    """Infochimps API"""
    
    def get_user_key(self):
        return config.get('cred', 'INFOCHIMPS_USER_KEY')
    
    def get_user_screen_name(self):
        return config.get('cred', 'INFOCHIMPS_USER_ID')
        
    def __init__(self, auth_handler=None, host='api.infochimps.com',
    format='json', secure=False, parser=None, retry_count=3, retry_delay=0):
        self.auth = auth_handler
        self.host = host
        self.format = format
        self.secure = secure
        self.parser = parser
        self.retry_count = retry_count
        self.retry_delay = retry_delay

    # tw/trstrank
    trstrank = bind_api(
        path = '/soc/net/tw/trstrank.json',
        payload_type = 'json',
        required_params = ['screen_name', 'apikey'],
        method = 'GET',
        require_auth = False,
    )

    # tw/strong_links
    stronglinks = bind_api(
        path = '/soc/net/tw/strong_links.json',
        payload_type = 'json', 
        required_params = ['screen_name', 'apikey'],
        method = 'GET',
        require_auth = False,
    )

    # tw/influence
    influence = bind_api(
        path = '/soc/net/tw/influence.json',
        payload_type = 'json',
        required_params = ['screen_name', 'apikey'],
        method = 'GET',
        require_auth = False,
    )
    
    # tw/wordbag
    wordbag = bind_api(
        path = '/soc/net/tw/wordbag.json',
        payload_type = 'json',
        required_params = ['screen_name', 'apikey'],
        method = 'GET',
        require_auth = False,
    )
    
    # tw/conversations
    conversations = bind_api(
        path = '/soc/net/tw/conversation.json',
        payload_type = 'json',
        required_params = ['user_a_sn', 'user_a_id', 'user_b_sn', 'user_b_id'],
        method = 'GET',
        require_auth = False,
    )
    
    # tw/wordstats
    word_stats = bind_api(
        path = '/soc/net/tw/word_stats.json',
        payload_type = 'json',
        required_params = ['tok'],
        method = 'GET',
        require_auth = False,
    )
    
    # de/demographics
    demographics = bind_api(
        path = '/web/an/de/demographics.json',
        payload_type = 'json',
        required_params = ['ip'],
        method = 'GET',
        require_auth = False,
    )

    # an/ip_census
    ip_census = bind_api(
        path = '/web/an/ip_census/combined.json',
        payload_type = 'json',
        required_params = ['ip'],
        method = 'GET',
        require_auth = False,
    )
    
    def lookup_users(self, user_ids=None, screen_names=None):
        """ Perform bulk look up of users from user ID or screenname """
        return self._lookup_users(list_to_csv(user_ids), list_to_csv(screen_names))

    _lookup_users = bind_api(
        path = '',
        payload_type = 'user', payload_list = True,
        required_params = ['user_id', 'screen_name'],
        require_auth = False,
    )