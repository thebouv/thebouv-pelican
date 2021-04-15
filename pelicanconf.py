from datetime import date
CURRENT_YEAR = date.today().year

AUTHOR = 'Anthony Bouvier'
SITENAME = 'thebouv'
SITEURL = ''
PATH = 'content'
TIMEZONE = 'America/Chicago'
DEFAULT_LANG = 'en'

# theme specific items -- begin
THEME = '/Users/thebouv/Documents/development/pelican-paper'
SITEDESCRIPTION = 'Geek of All Trades. Maker and Breaker. Tinkerer and Thinker-er.'
FAVICON = 'thebouv.jpg'
LOGO = 'thebouv.jpg'
TWITTER = 'https://twitter.com/thebouv'
GITHUB = 'https://github.com/thebouv'
GOOGLE_ANALYTICS = 'UA-55712845-1'
# theme specific items -- end

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None
DEFAULT_PAGINATION = 10
DELETE_OUTPUT_DIRECTORY = False

MARKDOWN = {
    'extension_configs': {
        'markdown.extensions.codehilite': {'css_class': 'highlight', 'guess_lang': False},
        'markdown.extensions.fenced_code': {},
    },
    'output_format': 'html5',
}