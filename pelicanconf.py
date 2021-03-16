#!/usr/bin/env python
# -*- coding: utf-8 -*- #

AUTHOR = 'Anthony Bouvier'
SITENAME = 'thebouv'
SITEURL = ''
PATH = 'content'
TIMEZONE = 'America/Chicago'
DEFAULT_LANG = 'en'

# theme specific items -- begin
THEME = 'theme/brutalist-theme'
SITESUBTITLE = 'Geek of All Trades. Maker and Breaker. Tinkerer and Thinker-er.'
SITEIMAGE = 'site-cover.jpg'
DISPLAY_CATEGORIES_ON_MENU = False
SITEDESCRIPTION = 'Geek of All Trades. Maker and Breaker. Tinkerer and Thinker-er.'
FAVICON = 'thebouv.jpg'
LOGO = 'thebouv.jpg'
FIRST_NAME = 'Anthony'
## google analytics (fake code commented out)
GOOGLE_ANALYTICS = 'UA-55712845-1'
## Twitter username for Twitter Card data
TWITTER_USERNAME = '@thebouv'
## Toggle display of theme attribution in the footer (scroll down and see)
## Attribution is appreciated but totally fine to turn off!
ATTRIBUTION = False
## Add a link to the tags page to the menu
## Other links can be added following the same tuple pattern 
MENUITEMS = [('tags', '/tags')]
## Social icons for footer
## Set these to whatever your unique public URL is for that platform
## I've left mine here as a example
TWITTER = 'https://twitter.com/thebouv'
GITHUB = 'https://github.com/thebouv'

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
SOCIAL = ()

DEFAULT_PAGINATION = 10

# MARKDOWN = ['fenced_code', 'codehilite(css_class=highlight, guess_lang=False)']

MARKDOWN = {
    'extension_configs': {
        'markdown.extensions.codehilite': {'css_class': 'highlight', 'guess_lang': False},
        'markdown.extensions.fenced_code': {},
    },
    'output_format': 'html5',
}

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True