#!/usr/bin/env python
# -*- coding: utf-8 -*- #

AUTHOR = u'Marc-Aurèle Brothier'
SITENAME = u'Shake Your Life'
SITESUBTITLE = u'Dream it & make it real!'
SITEURL = 'http://shakeyourlife.com'
TIMEZONE = 'Europe/Zurich'

DEFAULT_LANG = u'en'
DEFAULT_PAGINATION = 10

MENUITEMS = (('Home', 'http://shakeyourlife.com'),
)

DEFAULT_CATEGORY = ('Articles')
FILES_TO_COPY = (('extra/.htaccess', '.htaccess'), ('extra/robots.txt', 'robots.txt'),)
STATIC_PATHS = ['css', 'images', 'js']

MD_EXTENSIONS = ['codehilite','extra']
MARKUP = ('rst', 'md')

#THEME = 'themes/moparx'

#PLUGINS = ['pelican.plugins.sitemap',]


# ----------------------------------------------------------------------
# EXTERNAL LINKS
# ----------------------------------------------------------------------

# Recommended Sites
LINKS =  (('Biking the Great Divide \'09', 'http://bikingthegreatdivide.com/'),)


# ----------------------------------------------------------------------
# URL PATHS
# ----------------------------------------------------------------------

# Configure Pelican to output Clean URLs
ARTICLE_URL = '{slug}'
AUTHOR_URL = 'author/{slug}'
CATEGORY_URL = 'category/{slug}'
PAGE_URL =  '{slug}'
TAG_URL = 'tags/{slug}'

# Adjust save location to match previous files.
PAGE_SAVE_AS = '{slug}.html'
TAG_SAVE_AS = 'tags/{slug}.html'

# Atom and RSS feeds
CATEGORY_FEED_ATOM = ''
FEED_ALL_ATOM = 'atom.xml'
FEED_ALL_RSS = 'rss.xml'
FEED_MAX_ITEMS = 30


# ----------------------------------------------------------------------
# PLUGINS
# ----------------------------------------------------------------------

SITEMAP = {
    'format': 'xml',
    'priorities': {
        'articles': 0.5,
        'indexes': 0.5,
        'pages': 0.5
    },
        'changefreqs': {
        'articles': 'monthly',
        'indexes': 'monthly',
        'pages': 'monthly'
    }
}