#!/usr/bin/env python
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.
#
# Copyright (c) 2021-present Kaleidos Ventures SL

# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

DEBUG=1

AUTHOR = 'Taiga'
AUTHOR_EMAIL = 'support@taiga.io'
SITENAME = 'Taiga Blog'
#SITEURL = 'https://blog.taiga.io'
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
         ('Kaleidos', 'https://www.kaleidos.net/'),
         ('Penpot', 'https://penpot.app/'),
)

# Social widget
SOCIAL = (('Twitter', 'https://twitter.com/taigaio'),
          ('Github', 'https://github.com/taigaio'),
)

# Social metatags plugin settings
TWITTER_META_SITE = "@taigaio"


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
PLUGINS = ['gravatar', 'sitemap', 'open_graph', 'twitter_meta']


PRIVACY_POLICY_URL = "https://taiga.io/privacy-policy"

SITEMAP = {
    "format": "xml",
    "priorities": {
        "home": 1.0,
        "articles": 0.8,
        "indexes": 0.5,
        "authors": 0.6,
    }
}
