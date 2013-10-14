#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Marc-Aurèle Brothier'

SITENAME = u'Shake Your Life'
SITESUBTITLE = u'Dream it & make it real!'
SITEURL = 'http://shakeyourlife.com'

TIMEZONE = 'Europe/Paris'

LOCALE = "C"

DEFAULT_LANG = u'en'
DEFAULT_DATE_FORMAT = '%d %B %Y'

SUMMARY_MAX_LENGTH = 30

PAGE_DIR = 'pages'
PAGE_EXCLUDES = ('articles',)
PAGE_URL = '{slug}.html'
PAGE_SAVE_AS = PAGE_URL
PAGE_LANG_URL = '{slug}-{lang}.html'
PAGE_LANG_SAVE_AS = PAGE_LANG_URL

ARTICLE_DIR = 'articles'
ARTICLE_EXCLUDES = ('pages',)
ARTICLE_URL = '{date:%Y}/{date:%B}/{slug}.html'
ARTICLE_SAVE_AS = ARTICLE_URL
ARTICLE_LANG_URL = '{date:%Y}/{date:%B}/{slug}-{lang}.html'
ARTICLE_LANG_SAVE_AS = ARTICLE_LANG_URL
YEAR_ARCHIVE_SAVE_AS = '{date:%Y}/index.html'
MONTH_ARCHIVE_SAVE_AS = '{date:%Y}/{date:%B}/index.html'

TAG_URL = False
TAG_SAVE_AS = False

TYPOGRIFY = False

#FEED_DOMAIN = SITEURL
#FEED_ALL_ATOM = 'feeds/all.atom.xml'
FEED_ALL_ATOM = None
#FEED_ALL_RSS = 'feeds/all.rss.xml'
FEED_ALL_RSS = None
FEED_ATOM = None
FEED_RSS = None
#CATEGORY_FEED_RSS = 'feeds/%s.rss.xml'
CATEGORY_FEED_ATOM = None
CATEGORY_FEED_RSS = None
TAG_FEED_ATOM = None
TAG_FEED_RSS = None

# Feed generation is usually not desired when developing
TRANSLATION_FEED_ATOM = None

# Blogroll
LINKS =  (('Pelican', 'http://getpelican.com/'),
          ('Python.org', 'http://python.org/'),
          ('Jinja2', 'http://jinja.pocoo.org/'),
          ('You can modify those links in your config file', '#'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True
