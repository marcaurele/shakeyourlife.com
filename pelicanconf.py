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

SUMMARY_MAX_LENGTH = 50

PAGE_DIR = 'pages'
PAGE_EXCLUDES = ('articles',)
PAGE_URL = 'content/{slug}.html'
PAGE_SAVE_AS = PAGE_URL
PAGE_LANG_URL = 'content/{slug}-{lang}.html'
PAGE_LANG_SAVE_AS = PAGE_LANG_URL

ARTICLE_DIR = 'articles'
ARTICLE_EXCLUDES = ('pages',)
ARTICLE_URL = 'blog/{date:%Y}/{date:%m}/{date:%d}/{slug}.html'
ARTICLE_SAVE_AS = ARTICLE_URL
ARTICLE_LANG_URL = 'blog/{date:%Y}/{date:%m}/{date:%d}/{slug}-{lang}.html'
ARTICLE_LANG_SAVE_AS = ARTICLE_LANG_URL
YEAR_ARCHIVE_SAVE_AS = 'blog/{date:%Y}/index.html'
MONTH_ARCHIVE_SAVE_AS = 'blog/{date:%Y}/{date:%m}/index.html'

TAG_URL = 'tag/{slug}.html'
TAG_SAVE_AS = TAG_URL
TAGS_URL = False
TAGS_SAVE_AS = TAGS_URL

AUTHOR_URL = False
AUTHOR_SAVE_AS = AUTHOR_URL
AUTHORS_URL = False
AUTHORS_SAVE_AS = AUTHORS_URL

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

STATIC_PATHS = ['images','calendar-web']

# A list of files to copy from the source to the destination
FILES_TO_COPY = (
	('extra/robots.txt', 'robots.txt'),
)
# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True
