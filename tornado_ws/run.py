import os
import sys

root_dir = os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir, os.pardir, ))
sys.path.insert(0, root_dir)
from tornado_ws.app import main

if __name__ == "__main__":
    main()
