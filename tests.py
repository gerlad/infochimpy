import unittest
import random
from time import sleep
import os

from infochimps import *

"""Unit tests"""

class ChimpyAPITests(unittest.TestCase):

    def setUp(self):
        self.api = API(NoAuth())
        
    def testtrstrank(self):
        self.api.required_params(apikey, screen_name)

    def teststronglinks(self):
        self.api.strong_links(apikey, screen_name)

if __name__ == '__main__':
    unittest.main()