# infochimpy
# Copyright 2011 Gerald McCollam
# Portions Copyright 2009-2010 Joshua Roesslein

# Please see license.txt.

class ChimpsError(Exception):
    """Infochimpy exception"""

    def __init__(self, reason, response=None):
        self.reason = str(reason)
        self.response = response

    def __str__(self):
        return self.reason