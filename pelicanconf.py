#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals
from datetime import date

CURRENTYEAR = date.today().year

PELICAN_URL = 'https://blog.getpelican.com/'
GITHUB_SITE_URL = 'https://github.com/dalikewara/dalikewara.github.io'

THEME = 'themes/pelican-hyde'

AUTHOR = 'Dali Kewara'
SITENAME = 'An unexpected journey'
BIO = 'Written by Dali Kewara who lives and works as Backend Developer—building useful and unexpected things—in Indonesia. He also runs for art, writing, and journey.'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'Asia/Jakarta'

DEFAULT_LANG = 'en'

ARTICLE_PATHS = ['articles']
STATIC_PATHS = ['images', 'articles']

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),
         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('instagram', 'https://instagram.com/harukii_kun'),
          ('github', 'https://github.com/dalikewara'),
          ('email', 'dalikewara@gmail.com'),)

DEFAULT_PAGINATION = 10

DISQUS_SITENAME = 'dalikewara'

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True