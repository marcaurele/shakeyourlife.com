#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals
import os

AUTHOR = u'Marc-Aurèle Brothier'

SITENAME = u'Shake Your Life'
SITESUBTITLE = u'Dream it & make it real!'
SITEURL = 'http://shakeyourlife.com'

TIMEZONE = 'Europe/Paris'

LOCALE = "C"

THEME = os.path.join(os.path.dirname(os.path.abspath(__file__)),'theme_syl')

DELETE_OUTPUT_DIRECTORY = True
DEFAULT_LANG = u'en'
DEFAULT_DATE_FORMAT = '%d %B %Y'

DEFAULT_PAGINATION = 10

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
FEED_ALL_ATOM = None
FEED_ALL_RSS = None
FEED_ATOM = None
FEED_RSS = None
CATEGORY_FEED_ATOM = None
CATEGORY_FEED_RSS = None
TAG_FEED_ATOM = None
TAG_FEED_RSS = None
TRANSLATION_FEED_ATOM = None

# Blogroll
LINKS =  (('Biking the Great Divide \'09', 'http://www.bikingthegreatdivide.com'),
          )

# A list of files to copy from the source to the destination
FILES_TO_COPY = (
	('extra/robots.txt', 'robots.txt'),
)
# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True
