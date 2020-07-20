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

# SITE INFO

AUTHOR = 'Dali Kewara'
AUTHOR_NICKNAME = 'Dali'
SITENAME = 'An unexpected journey'
BIO = 'Written by Dali Kewara who lives and works as Backend Developer—building useful and unexpected things—in Indonesia. He also runs for art, writing, and journey. His life motto is \'Make it simple but Spectacular!\''
KEYWORDS = 'dalikewara, dali kewara, blog, personal, website, programmer, developer, daily, work, person, journey, art, writing, business'
SITEURL = ''
SITE_LOGO = 'https://lh3.googleusercontent.com/pw/ACtC-3dBME0xNP8kojcslSG6fOJxYTgQ_30vbVGvWb2DIz0M6GFQ1DdEl7fUhruizL0uuSjQpx_3j3htACAV92-EYtbrj5bkr0zdfiWOa6z87OXt_zr9T1OkXQXoIOu2Gx3AJcAtSl7ZVbNKkTo36LJYmE9v=w900-h300-no'

# TIMEZONE

TIMEZONE = 'Asia/Jakarta'

# LANG

DEFAULT_LANG = 'en'

# PATHS

PATH = 'content'
ARTICLE_PATHS = ['articles']
PAGE_PATHS = ['pages']

# EXTRA PATH METADATA

EXTRA_PATH_METADATA = {
  'extra/robots.txt': {'path': 'robots.txt'},
  'extra/favicon.ico': {'path': 'favicon.ico'}
}

# PAGE LINKS

PAGE_LINK = {
  'about': 'about-me',
  'categories': 'categories',
  'tags': 'tags',
  'archives': 'archives',
}

# NAVBAR MENU

NAVBAR_MENU = [
  ('item', 'Overview', 'yellow', SITEURL + '/'),
  ('item', 'About', 'yellow', SITEURL + '/' + PAGE_LINK['about']),
  ('dropdown', 'More...', 'black', [
    ('item', 'Categories', 'black', SITEURL + '/' + PAGE_LINK['categories']),
    ('item', 'Tags', 'black', SITEURL + '/' + PAGE_LINK['tags']),
    ('item', 'Archives', 'black', SITEURL + '/' + PAGE_LINK['archives']),
    ('separator', '', '', ''),
    ('item', 'Report an issue', 'red', GITHUB_SITE_ISSUE_URL)
  ])
]

# STATIC PATHS

STATIC_PATHS = [
  'images', 
  'articles', 
  'extra/robots.txt', 
  'extra/favicon.ico', 
  'enter-root/index.html', 
  'enter-root/config.yml'
]

# DIRECT TEMPLATES

DIRECT_TEMPLATES = ('index', 'tags', 'categories', 'archives', 'sitemap')

# SITEMAP

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
      'use_pygments': False
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
  (
    'blog', 
    'Things to write in daily life&mdash;depends on my mood actually.', 
    'https://lh3.googleusercontent.com/pw/ACtC-3ff9c2NDer_YX06s8mu3kvLF8crc3XhqfPFrgUum4hyaORHr65PmdFb851Vq9FmAOorka9QTJ0s78iHJWDIwx9XiwMJTOd-8OY1LNxSRfUNcEcxqTsDuaHEMBpQuj1Yve94U7Cs_sv2lH12Ohq2pWz5=w1440-h952-no'
  ),
  (
    'status', 
    'This is basicly my daily activities&mdash;can be cases that I met while working or just something that need to solve.', 
    'https://lh3.googleusercontent.com/pw/ACtC-3cgG2xl7VxpdaIJBawQZY0STRjSiw7xE-4JsOIOZW1F3ebvmW3ERaIfHAfoIoVkEyp4BwmrL2x1z_tDB6dQanr2pu1cD-yTfQYPJppHj_VhWnUXxpqEs_bMrBP-UoIoE3Cd-Ih6p8eTA1MCsqWLWSzI=w1698-h514-no'
  ),
  (
    'js', 
    'Articles about Javascript and NodeJS. Many of them are information about my JS modules and the documentation.', 
    'https://lh3.googleusercontent.com/pw/ACtC-3cqQHa1FMrGyydG9XrSsaNZI-s2A4kincR_hoC8pPZEwDMrY4pPjJw0ULFXE3LhJ-s4MOKm-nN_y2CyBAKYiM_JdRVtRj8jYkX7EqsOFVvVN6Up9lHY5LrrdfJDNgVjBS1si8kHg3WFjPT5pQ-Yz9qU=w1150-h524-no'
  ),
  (
    'php', 
    'Articles about PHP. Many of them are information about my PHP modules and the documentation.', 
    'https://lh3.googleusercontent.com/pw/ACtC-3cDS4OSTV1ntDVgXxdX-yYJAPLeDuXFYBsTZGl22-mlkvZWXM7_76xoCTA-JkRVtybEZarfvn2sZvkghAu-1kc4fkPjwN3in8xStMzpgnMqG-XGzOQzcw7835_FDoTE3I5tw7jeEIME8BmBId4xDPG8=w1130-h486-no'
  ),
  (
    'python', 
    'Articles about Python. Many of them are information about my Python modules and the documentation.', 
    'https://lh3.googleusercontent.com/pw/ACtC-3dq2uWImDux39myT4O4FsuuadAxkCy0OlcKb8e_OyCjK5yTWF1t0jQYZ3kXHGuNW4YOexNc2N2XORE0eLFluH-KRzCuao1ZoNdw_GxQwYx_I4hvvqX7HpaVcNRixxG9JOU3sIrue4XtEL8Nilwg055F=w1040-h510-no'
  )
]

# OVERVIEW INFO

OVERVIEW_INFO = [
  'Code in ' +
      '<span class="icon"><i class="fab fa-node" style="color:#82c920"></i></span> ' +
    'NodeJS, ' +
      '<span class="icon"><i class="fab fa-python" style="color:#fd7e16"></i></span> ' +
    'Python and ' +
      '<span class="icon"><i class="fab fa-php" style="color:#be4bdb"></i></span> ' +
    'PHP',
  'Play ' + 
      '<img src="https://lh3.googleusercontent.com/pw/ACtC-3fvWy52TJnpM_p1y_KMF_w-IrtsFrgyxjEJfZ8WIMu8BA6jP99Dyen4gwWqAIsvQNxbypmsuJiSxzpJaE0SlxRuf-BgazELzO4N8BL52y5Z00id31IA5gqZB6VuSPOEOXx-BdpIYnvubTV3FQxyZ0zz=w1024-h1029-no" width="15" height="15"/> ' + 
    'DOTA 2 turbo mode (have fun only) & ' +
      '<img src="https://lh3.googleusercontent.com/pw/ACtC-3eMSz_QJ95soGFabO6XNFoeZzdCDUD_OVVu6Q55sxA4UMEla4I9ZBs_e8LiQOnFZN5vwwTc-5dEKLxWg5Wn9m50P6aMJ7hQzVvb9LDL5RixXdz0yMbKS0TKEmSxR5KY6ncjQ1x2GyKTVK5czjXh7_zm=w1397-h810-no" width="30" height="30"/> ' +
    'STORY OF SEASONS: Friends of Mineral Town',
  '<a href="' + SITEURL + '/' + PAGE_LINK['about'] + '">Learn more about ' + AUTHOR_NICKNAME + ' >></a>'
]

# OVERVIEW INTEREST

OVERVIEW_INTEREST = [
  (
    '"vcmrefunc" version 1.0.1 - The right way to repeat a process', 
    'vcmrefunc-this-is-how-to-repeat-a-process-correctly'
  ),
  (
    '"pangsitpy" version 0.0.13 - My starter pack framework represented in Python to deal with learning computing such as Machine/Deep Learning, Data Science, etc', 
    'pangsitpy-python-my-starter-pack-framework-in-deep-learning'
  ),
  (
    '"vcmcemtex" version 1.0.0 - An universal & customable cemtext generator for batch transactions', 
    'vcmcemtex-deal-with-banks-transaction-file-format'
  ),
  (
    '"vcmloop" version 1.0.4 - An interval-based looping method for massive data', 
    'vcmloop-loop-massive-data-with-no-worry'
  ),
  (
    '"vcmpad" version 1.0.5 - Fast, lightweight, and customable string padding generator', 
    'vcmpad-a-string-padding-generator'
  ),
]

# OVERVIEW NOW

OVERVIEW_NOW = [
  'He\'s writing a paper from his research about toxic speech detection.',
  'He\'s creating AyaPingPing v3 and will make it has first public release.'
]