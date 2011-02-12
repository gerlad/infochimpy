#!/usr/bin/env python

# chimpshell
# Copyright 2011 Gerald McCollam
# Portions Copyright 2009-2010 Joshua Roesslein

# Please see license.txt.

from getpass import getpass
from optparse import OptionParser
import infochimpy
from infochimpy import API
from infochimpy.auth import NoAuth

"""
This script for debugging infochimps during development or just play with the library.
It imports infochimps and creates an authenticated API instance (api).
"""

opt = OptionParser(usage='chimpshell [action] [options]')
opt.add_option('-d', '--debug',
        action='store',
        dest='debug',
        help='enable debug mode')
options, args = opt.parse_args()

auth = None

if options.debug:
    infochimps.debug()

local_ns = {'infochimpy': infochimpy, 'api': API(NoAuth())}
shellbanner = '<chimpshell>'

try:
    import IPython
    ipshell = IPython.Shell.IPShell([''], user_ns = local_ns)
    ipshell.mainloop(sys_exit=1, banner = shellbanner)
except ImportError:
    import code
    code.interact(shellbanner, local = local_ns)

