# vim: fileencoding=utf-8
import sys
import getpass
# 'raw_input' was renamed to 'input' in Python 3.x
from six.moves import input

from .colorcodes import _c

def prompt_auth():
    """
    Prompt user for authentication username/password and return them as a
    tuple. Do not echo the password to the screen.
    """
    defuser = getpass.getuser().lower()
    print(_c.bold + _c.blue + "CCHMC username " + _c.reset +
          "[ENTER for default '%s']: " % (defuser), file=sys.stderr, end='')
    user = input()
    user = user if user else defuser
    passwd = getpass.getpass(_c.bold + _c.blue + "Password" + _c.reset + ": ")
    return (user, passwd)

