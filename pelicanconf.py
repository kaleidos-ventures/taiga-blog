#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

DEBUG=1

AUTHOR = 'Taiga'
AUTHOR_EMAIL = 'support@taiga.io'
SITENAME = 'Taiga Blog'
SITEURL = 'https://blog.taiga.io'
SITESUBTITLE = 'Taiga is a project management platform for startups and agile developers & designers'

PATH = 'content'

TIMEZONE = 'Europe/Paris'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ATOM = 'feeds/atom.xml'
FEED_ALL_ATOM = 'feeds/all.atom.xml'
CATEGORY_FEED_ATOM = 'feeds/%s.atom.xml'

FEED_RSS = 'feeds/rss.xml'
FEED_ALL_RSS = 'feeds/all.rss.xml'
CATEGORY_FEED_RSS = 'feeds/%s.rss.xml'

# Blogroll
LINKS = (('Taiga.io', 'https://taiga.io'),
         ('Mailing list', 'https://groups.google.com/forum/#!forum/taigaio'),
         ('Kaleidos', 'http://www.kaleidos.net/'),
         ('ΠWEEK', 'http://piweek.com/'),
)

# Social widget
SOCIAL = (('Twitter', 'http://twitter.com/taigaio'),
          ('Github', 'https://github.com/taigaio'),
)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

# Extra files to copy
STATIC_PATHS = [
    'images',
    'extra/robots.txt',
    'extra/humans.txt',
    'extra/favicon.ico'
]

EXTRA_PATH_METADATA = {
    'extra/robots.txt': {'path': 'robots.txt'},
    'extra/humans.txt': {'path': 'humans.txt'},
    'extra/favicon.ico': {'path': 'favicon.ico'},
}

#settings for Pelican
DEFAULT_CATEGORY = 'General'
THEME = 'theme/taiga'
DISQUS_SITENAME = "taiga-blog"

#Plugins
PLUGIN_PATHS = ['plugins']
PLUGINS = ['gravatar', 'sitemap', 'open_graph']


PRIVACY_POLICY_URL = "http://taiga.io/privacy-policy"

SITEMAP = {
    "format": "xml",
    "priorities": {
        "home": 1.0,
        "articles": 0.8,
        "indexes": 0.5,
        "authors": 0.6,
    }
}
