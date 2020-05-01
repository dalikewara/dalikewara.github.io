#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals
from datetime import date

CURRENTYEAR = date.today().year

PELICAN_URL = 'https://blog.getpelican.com/'
GITHUB_SITE_URL = 'https://github.com/dalikewara/dalikewara.github.io'
GITHUB_URL = 'https://github.com/dalikewara/dalikewara.github.io'

THEME = 'themes/pelican-hyde'

AUTHOR = 'Dali Kewara'
SITENAME = 'An unexpected journey'
BIO = 'Written by Dali Kewara who lives and works as Backend Developer—building useful and unexpected things—in Indonesia. He also runs for art, writing, and journey.'
KEYWORDS = 'dalikewara, dali kewara, blog, personal, website, programmer, developer, daily, work, person, journey, art, writing, business'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'Asia/Jakarta'

DEFAULT_LANG = 'en'

ARTICLE_PATHS = ['articles']
STATIC_PATHS = ['images', 'articles', 'extra/robots.txt', 'extra/favicon.ico']
EXTRA_PATH_METADATA = {
    'extra/robots.txt': {'path': 'robots.txt'},
    'extra/favicon.ico': {'path': 'favicon.ico'}
}

DIRECT_TEMPLATES = ('index', 'tags', 'categories', 'archives', 'sitemap')
SITEMAP_SAVE_AS = 'sitemap.xml'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

DEFAULT_COVER_IMAGE = "https://lh3.googleusercontent.com/t-hryOxzsaAKrfhedprLLmAc2sSeErMEAIX740NjiAwhGwJyzWkqPt_izjy13Ji3ItrZOyS0NO5ngqWX3zutNFKveO9iIvzuXikvMQ-XdHUitQ4B_gIMfh0nZsAYnH-UUwmpXbO0nA=s261-no"
COVER_IMAGE_DEFAULT = "https://lh3.googleusercontent.com/t-hryOxzsaAKrfhedprLLmAc2sSeErMEAIX740NjiAwhGwJyzWkqPt_izjy13Ji3ItrZOyS0NO5ngqWX3zutNFKveO9iIvzuXikvMQ-XdHUitQ4B_gIMfh0nZsAYnH-UUwmpXbO0nA=s261-no"

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),
         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('instagram', 'https://instagram.com/harukii_kun'),
          ('github', 'https://github.com/dalikewara'),
          ('email', 'dalikewara@gmail.com'),)

PLUGIN_PATHS = ['plugins']
PLUGINS = [
    'minify',
    'pelican_precompress',
    'related_posts',
    'readtime',
    'post_revision',
    'simple_footnotes',
    'pelican-cover-image'
]

MINIFY = {
  'remove_comments': True,
  'remove_all_empty_space': True,
  'remove_optional_attribute_quotes': False
}

PRECOMPRESS_GZIP = True
PRECOMPRESS_ZOPFLI = True
PRECOMPRESS_BROTLI = True
PRECOMPRESS_TEXT_EXTENSIONS = {
    '.atom',
    '.css',
    '.html',
    '.js',
    '.rss'
}

DEFAULT_PAGINATION = 10

DISQUS_SITENAME = 'dalikewara'

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True