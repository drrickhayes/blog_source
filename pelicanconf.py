#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'DrRickHayes'
SITENAME = 'Newman\'s Dream'
SITEURL = ''

PATH = 'content'
OUTPUT_PATH = '../output'
TIMEZONE = 'Australia/Melbourne'
DEFAULT_LANG = 'en'


THEME = 'theme'
BOOTSTRAP_THEME = 'shamrock'
PLUGIN_PATHS = ['plugins/', ]
PLUGINS = ['i18n_subsites', ]
JINJA_ENVIRONMENT = {
    'extensions': ['jinja2.ext.i18n'],
}

ARTICLE_PATHS = ['articles']
PAGE_PATHS = ['pages']
STATIC_PATHS = ['img', 'pdf']

ARTICLE_URL = 'articles/{date:%Y}/{date:%m}/{date:%d}/{slug}/'
ARTICLE_SAVE_AS = 'articles/{date:%Y}/{date:%m}/{date:%d}/{slug}/index.html'

PAGE_URL = 'pages/{slug}/'
PAGE_SAVE_AS = 'pages/{slug}/index.html'
CATEGORY_URL = 'category/{slug}'
CATEGORY_SAVE_AS = 'category/{slug}/index.html'
TAG_URL = 'tag/{slug}'
TAG_SAVE_AS = 'tag/{slug}/index.html'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('The Dream of Gerontius', 'http://newmanreader.org/works/verses/gerontius.html'),
         ('Elgar: The Dream of Gerontius, Part 1', 'https://youtu.be/pHS7MwAjN-E'),
         ('Elgar: The Dream of Gerontius, Part 2', 'https://youtu.be/gU8Oz6nGTZA'),
         ('Newman Canonisation', 'https://www.newmancanonisation.com/blog/thejourneybegins'),
         ('The Newman Reader', 'http://newmanreader.org/index.html'),
         ('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),)

# Social widget
#SOCIAL = (('You can add links in your config file', '#'),
#          ('Another social link', '#'),)

DEFAULT_PAGINATION = False

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
