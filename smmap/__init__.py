"""Intialize the smmap package"""

__author__ = "Sebastian Thiel"
__contact__ = "byronimo@gmail.com"
__homepage__ = "https://github.com/gitpython-developers/smmap"
version_info = (5, 0, 0)
__version__ = ".".join(str(i) for i in version_info)

from .buf import *

# make everything available in root package for convenience
from .mman import *
