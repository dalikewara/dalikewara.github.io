from __future__ import unicode_literals
from datetime import date

# URLS

PELICAN_URL = 'https://blog.getpelican.com/'
GITHUB_SITE_URL = 'https://github.com/dalikewara/dalikewara.github.io/'
GITHUB_SITE_ISSUE_URL = 'https://github.com/dalikewara/dalikewara.github.io/issues'
GITHUB_URL = 'https://github.com/'
BULMA_URL = 'https://bulma.io/'
NETLIFY_URL = 'https://www.netlify.com/'

# ACTIVE THEME

THEME = 'themes/rujak-cingur'

AUTHOR = 'Dali Kewara'
SITENAME = 'An unexpected journey'
BIO = 'Written by Dali Kewara who lives and works as Backend Developer—building useful and unexpected things—in Indonesia. He also runs for art, writing, and journey.'
KEYWORDS = 'dalikewara, dali kewara, blog, personal, website, programmer, developer, daily, work, person, journey, art, writing, business'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'Asia/Jakarta'

DEFAULT_LANG = 'en'

ARTICLE_PATHS = ['articles']
PAGE_PATHS = ['pages']
STATIC_PATHS = ['images', 'articles', 'extra/robots.txt', 'extra/favicon.ico']
EXTRA_PATH_METADATA = {
    'extra/robots.txt': {'path': 'robots.txt'},
    'extra/favicon.ico': {'path': 'favicon.ico'}
}

# DIRECT TEMPLATES

DIRECT_TEMPLATES = ('index', 'tags', 'categories', 'archives', 'sitemap')

SITEMAP_SAVE_AS = 'sitemap.xml'

# RSS FEED

FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# COVER IMAGE

DEFAULT_COVER_IMAGE = "https://lh3.googleusercontent.com/t-hryOxzsaAKrfhedprLLmAc2sSeErMEAIX740NjiAwhGwJyzWkqPt_izjy13Ji3ItrZOyS0NO5ngqWX3zutNFKveO9iIvzuXikvMQ-XdHUitQ4B_gIMfh0nZsAYnH-UUwmpXbO0nA=s261-no"
COVER_IMAGE_DEFAULT = "https://lh3.googleusercontent.com/t-hryOxzsaAKrfhedprLLmAc2sSeErMEAIX740NjiAwhGwJyzWkqPt_izjy13Ji3ItrZOyS0NO5ngqWX3zutNFKveO9iIvzuXikvMQ-XdHUitQ4B_gIMfh0nZsAYnH-UUwmpXbO0nA=s261-no"

# BLOGROLL

LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),
         ('You can modify those links in your config file', '#'))

# SOCIAL

SOCIAL = (('instagram', 'Instagram', 'https://instagram.com/harukii_kun'),
          ('github', 'GitHub', 'https://github.com/dalikewara'),
          ('envelope', 'Email', 'mailto:dalikewara@gmail.com'),
          ('feed', 'RSS Feed', ''))

# PLUGIN

PLUGIN_PATHS = ['plugins']
PLUGINS = [
    'minify',
    'pelican_precompress',
    'related_posts',
    'readtime',
    'post_revision',
    'simple_footnotes',
    'pelican-cover-image',
    'ipynb.markup'
]

# MARKDOWN

MARKDOWN = {
  'extension_configs': {
    'markdown.extensions.codehilite': {
      'css_class': 'highlight'
    },
    'markdown.extensions.extra': {},
    'markdown.extensions.meta': {},
    'markdown.extensions.toc': {
      'title': 'Table of Contents',
    },
  },
  'output_format': 'html5',
}

# MARKUP

MARKUP = ('md', 'ipynb')

# IGNORE FILES

IGNORE_FILES = ['.ipynb_checkpoints']

# MINIFY

MINIFY = {
  'remove_comments': True,
  'remove_all_empty_space': True,
  'remove_optional_attribute_quotes': False
}

# PRECOMPRESS

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

# PAGINATION

DEFAULT_PAGINATION = 10

# DISQUS

DISQUS_SITENAME = 'dalikewara'

# CATEGORY DESCRIPTION

CATEGORY_DESCRIPTION = [
  ('blog', 'Things in daily life I wanna write&mdash;depends on my mood actually.', 'https://lh3.googleusercontent.com/pw/ACtC-3ff9c2NDer_YX06s8mu3kvLF8crc3XhqfPFrgUum4hyaORHr65PmdFb851Vq9FmAOorka9QTJ0s78iHJWDIwx9XiwMJTOd-8OY1LNxSRfUNcEcxqTsDuaHEMBpQuj1Yve94U7Cs_sv2lH12Ohq2pWz5=w1440-h952-no'),
  ('js', 'Articles about Javascript and NodeJS. Many of them are information about my JS modules and the documentations.', 'https://lh3.googleusercontent.com/pw/ACtC-3cqQHa1FMrGyydG9XrSsaNZI-s2A4kincR_hoC8pPZEwDMrY4pPjJw0ULFXE3LhJ-s4MOKm-nN_y2CyBAKYiM_JdRVtRj8jYkX7EqsOFVvVN6Up9lHY5LrrdfJDNgVjBS1si8kHg3WFjPT5pQ-Yz9qU=w1150-h524-no'),
  ('php', 'Articles about PHP. Many of them are information about my PHP modules and the documentations.', 'https://lh3.googleusercontent.com/pw/ACtC-3cDS4OSTV1ntDVgXxdX-yYJAPLeDuXFYBsTZGl22-mlkvZWXM7_76xoCTA-JkRVtybEZarfvn2sZvkghAu-1kc4fkPjwN3in8xStMzpgnMqG-XGzOQzcw7835_FDoTE3I5tw7jeEIME8BmBId4xDPG8=w1130-h486-no'),
  ('python', 'Articles about Python. Many of them are information about my Python modules and the documentations.', 'https://lh3.googleusercontent.com/pw/ACtC-3dq2uWImDux39myT4O4FsuuadAxkCy0OlcKb8e_OyCjK5yTWF1t0jQYZ3kXHGuNW4YOexNc2N2XORE0eLFluH-KRzCuao1ZoNdw_GxQwYx_I4hvvqX7HpaVcNRixxG9JOU3sIrue4XtEL8Nilwg055F=w1040-h510-no')
]