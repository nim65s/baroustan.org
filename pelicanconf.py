#!/usr/bin/env python

import os

DOMAIN_NAME = os.environ.get('DOMAIN_NAME', 'localhost')
HTTP = 'http' if DOMAIN_NAME == 'localhost' else 'https'

AUTHOR = 'Guilhem Saurel'
SITENAME = 'Baroustan'
SITEURL = f'{HTTP}://baroustan.{DOMAIN_NAME}'

PATH = 'content'

TIMEZONE = 'Europe/Paris'

DEFAULT_LANG = 'fr'

FEED_DOMAIN = SITEURL

DEFAULT_PAGINATION = 3

THEME = 'attila'
HEADER_COVER = 'images/header.jpg'
STATIC_PATHS = ['images', 'css', 'js']

PLUGIN_PATHS = ['plugins', 'pelican-plugins']
PLUGINS = ['nim_gallery', 'filetime_from_git']
CSS_OVERRIDE = ['css/baroustan.css', 'css/magnific-popup.css']
JS_OVERRIDE = ['js/jquery.magnific-popup.js', 'js/gallery.js']
