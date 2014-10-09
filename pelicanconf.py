#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

DEBUG=1

AUTHOR = 'Taiga'
AUTHOR_EMAIL = 'support@taiga.io'
SITENAME = 'Taiga Blog'
SITEURL = ''
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
)

# Social widget
SOCIAL = (('Twitter', 'http://twitter.com/taigaio'),
          ('Github', 'https://github.com/taigaio'),
          ('Google+', 'https://github.com/taigaio'),
)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

#settings for Pelican
DEFAULT_CATEGORY = 'General'
THEME = 'theme/taiga'
DISQUS_SITENAME = "taiga-blog"

#Plugins
PLUGIN_PATHS = ['plugins']
PLUGINS = ['gravatar']
