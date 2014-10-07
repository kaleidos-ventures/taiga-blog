#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Taiga'
SITENAME = 'Taiga Blog'
SITEURL = ''
SITESUBTITLE = 'Taiga is a project management platform for startups and agile developers & designers'

PATH = 'content'

TIMEZONE = 'Europe/Paris'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),
         ('You can modify those links in your config file', '#'),)

# Social widget
# Social widget
SOCIAL = (('Twitter', 'http://twitter.com/taigaio'),
          ('Git hub', 'https://github.com/taigaio')
)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

#settings for Pelican
DEFAULT_CATEGORY = 'General'
THEME = 'theme/taiga'
