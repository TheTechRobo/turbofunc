from .clearscreen import *
from .pressanykey import *
from .standtextout import *
from .multiprint import *
from .sanitiseinput import *

import warnings
warnings.warn("Importing turbofunc by itself is deprecated and not recommended. It will be removed in turbofunc 2.0. Run help(turbofunc) to see the possible imports.", DeprecationWarning, stacklevel=2) #https://stackoverflow.com/a/30093619/9654083
"""
    For documentation, please import the corresponding module first and then run help() on IT.
    There are:
      - turbofunc.clearscreen
      - turbofunc.pressanykey
      - turbofunc.standtextout
      - turbofunc.multiprint
      - turbofunc.sanitiseinput
    This __init__.py is ONLY still provided for backwards compatibility.
"""
