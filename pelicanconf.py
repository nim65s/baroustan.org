#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Guilhem Saurel'
SITENAME = 'Baroustan'
# SITEURL = 'https://baroustan.org'

PATH = 'content'

TIMEZONE = 'Europe/Paris'

DEFAULT_LANG = 'fr'

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
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = 3

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

THEME = 'attila'
HEADER_COVER = 'images/header.jpg'
STATIC_PATHS = ['images', 'css']

# PLUGIN_PATHS = ['pelican-plugins']
# PLUGINS = ['liquid_tags.img']
PLUGIN_PATHS = ['plugins', 'pelican-plugins']
PLUGINS = ['nim_gallery', 'filetime_from_git']
CSS_OVERRIDE = ['css/baroustan.css']
