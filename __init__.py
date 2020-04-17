# make sure this folder is in your python path so that you can import it really easily :
import sys
from os import path
realpath = path.dirname(path.abspath(__file__))
# we use sys.path.insert(1, realpath) to avoid some errors with paths
# sys.path.append(realpath)
sys.path.insert(1, realpath)