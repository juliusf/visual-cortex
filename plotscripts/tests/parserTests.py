__author__ = 'jules'

import nose
from visualCortex.resultParser import *

def test_basic_file_io():
    file = "cc.data"
    result = parseResultFile(file)
    