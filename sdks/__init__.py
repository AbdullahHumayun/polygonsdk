import sys
import os

# Get the directory path of the polygonsdkmaster package
package_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(package_dir)

# Now you can import modules from the polygonsdkmaster package
from sdks import *