from __future__ import unicode_literals
import os
import sys
sys.path.append(os.curdir)
from pelicanconf import *

SITEURL = 'https://www.dalikewara.com'
RELATIVE_URLS = False

FEED_ALL_ATOM = 'feeds/all.atom.xml'
FEED_ALL_RSS = 'feeds/all.rss.xml'
CATEGORY_FEED_ATOM = 'feeds/category.{slug}.atom.xml'
CATEGORY_FEED_RSS = 'feeds/category.{slug}.rss.xml'
TAG_FEED_ATOM = 'feeds/tag.{slug}.atom.xml'
TAG_FEED_RSS = 'feeds/tag.{slug}.rss.xml'

DELETE_OUTPUT_DIRECTORY = True

DISQUS_SITENAME = 'dalikewara'
GOOGLE_ANALYTICS = 'UA-68907511-1'