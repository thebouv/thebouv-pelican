#!/usr/bin/env python
# -*- coding: utf-8 -*- #

# This file is only used if you use `make publish` or
# explicitly specify it as your config file.

from pelicanconf import *
import os
import sys
sys.path.append(os.curdir)

# If your site is available via HTTPS, make sure SITEURL begins with https://
SITEURL = 'https://thebouv.com'
RELATIVE_URLS = False

FEED_DOMAIN = SITEURL
FEED_ATOM = 'feeds/atom.xml'
FEED_ALL_ATOM = 'feeds/all.atom.xml'
CATEGORY_FEED_ATOM = 'feeds/{slug}.atom.xml'
