# infochimpy
# Please see LICENSE

class ChimpsError(Exception):
    """Infochimpy exception"""

    def __init__(self, reason, response=None):
        self.reason = str(reason)
        self.response = response

    def __str__(self):
        return self.reason
        
class AuthError(ChimpsError):
    """
        Raised when you try to access a protected resource.
    """
    def __init__(self, msg):
        self.msg = msg

    def __str__(self):
        return repr(self.msg)