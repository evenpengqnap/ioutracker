__version__ = "1.2.1"

import os, sys

filePath = os.path.abspath(__file__)
currentFolder = os.path.dirname(filePath)
sys.path.append(currentFolder)

from .src import *
