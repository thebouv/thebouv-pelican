#!/usr/bin/env python
# -*- coding: utf-8 -*- #

AUTHOR = 'Anthony Bouvier'
SITENAME = 'thebouv'
SITEURL = ''
PATH = 'content'
TIMEZONE = 'America/Chicago'
DEFAULT_LANG = 'en'

# theme specific items -- begin
THEME = 'themes/pelican-clean'
SIDEBAR_DIGEST = 'geek of all trades'
FAVICON = 'url-to-favicon'
DISPLAY_PAGES_ON_MENU = True
TWITTER_USERNAME = 'twitter-user-name'
MENUITEMS = (('Blog', SITEURL),)
# theme specific items -- end

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = ()

# Social widget
SOCIAL = (('linkedin', 'https://www.linkedin.com/in/thebouv'),
          ('github', 'https://github.com/thebouv'),
          ('twitter', 'https://twitter.com/thebouv'),
          )

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True