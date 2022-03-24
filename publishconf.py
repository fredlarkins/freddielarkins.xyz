# This file is only used if you use `make publish` or
# explicitly specify it as your config file.

import os
import sys
sys.path.append(os.curdir)
from pelicanconf import *

# If your site is available via HTTPS, make sure SITEURL begins with https://
SITEURL = 'https://freddielarkins.xyz'
RELATIVE_URLS = False

FEED_ALL_ATOM = 'feeds/all.atom.xml'
CATEGORY_FEED_ATOM = 'feeds/{slug}.atom.xml'

#DELETE_OUTPUT_DIRECTORY = False

# Following items are often useful when publishing

#DISQUS_SITENAME = ""

# Removed because I think it's conflicting with my own injection of the script tag in base.html
#GOOGLE_ANALYTICS = 'G-7XLXLD52JM'