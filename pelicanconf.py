#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

# disable caching when changing settings
LOAD_CONTENT_CACHE = False

AUTHOR = u'Dragos Stanciu'
SITENAME = u'Dragos Stanciu'
SITEURL = ''

##########################
### Flex theme options ###
##########################
SITETITLE = AUTHOR
SITESUBTITLE = u'Software Developer'
SITEDESCRIPTION = u'Dragos Stanciu\'s website'
SITELOGO = u'/images/profile.png'
#MAIN_MENU = True
MAIN_MENU = False

# Times and dates
DEFAULT_DATE_FORMAT = '%d %b, %Y'
TIMEZONE = 'Europe/Paris'
DEFAULT_LANG = u'en'

PATH = 'content'

#######################
### Static homepage ###
#######################
# found in content/pages/home.md
# Uncomment the 2 liens below to use a static page as home page
INDEX_SAVE_AS = 'blog/index.html'
LINKS = (('Dragon Programmer blog', 'https://dragonprogrammer.com/'),) # add link to blog

# Set article URL
ARTICLE_URL = 'blog/{date:%Y}/{date:%m}/{slug}/'
ARTICLE_SAVE_AS = 'blog/{date:%Y}/{date:%m}/{slug}/index.html'

# Set page URL
PAGE_URL = '{slug}/'
PAGE_SAVE_AS = '{slug}/index.html'

CATEGORY_URL = 'blog/category/{slug}/'
CATEGORY_SAVE_AS = 'blog/category/{slug}/index.html'

TAG_URL = 'blog/tag/{slug}/'
TAG_SAVE_AS = 'blog/tag/{slug}/index.html'

# don't need author pages, as I'm the only author
AUTHOR_URL = ''
AUTHOR_SAVE_AS = ''

# create per year and per month archives
YEAR_ARCHIVE_SAVE_AS = 'blog/{date:%Y}/index.html'
MONTH_ARCHIVE_SAVE_AS = 'blog/{date:%Y}/{date:%m}/index.html'
ARCHIVES_SAVE_AS = 'blog/archives.html'
CATEGORIES_SAVE_AS = 'blog/categories.html'
TAGS_SAVE_AS = 'blog/tags.html'


DEFAULT_PAGINATION = 10


STATIC_PATHS = ['images', 'figures', 'downloads', 'extra/CNAME', 'extra/robots.txt', 'extra/favicon.ico']

EXTRA_PATH_METADATA = {
    'extra/CNAME': {'path': 'CNAME'},
    'extra/robots.txt': {'path': 'robots.txt'},
    'extra/favicon.ico': {'path': 'favicon.ico'}
}


THEME = '/home/dragos/src/pelican-themes/Flex'

PLUGIN_PATHS = ['/home/dragos/src/pelican-plugins']

PLUGINS = ['sitemap']

# Sitemap
SITEMAP = {
    'format': 'xml',
    'priorities': {
        'articles': 0.6,
        'indexes': 0.5,
        'pages': 0.5
    },
    'changefreqs': {
        'articles': 'monthly',
        'indexes': 'daily',
        'pages': 'monthly'
    },
    'exclude': ['tag/', 'category/'],
}




# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None


# Social widget
SOCIAL = (('linkedin', 'https://www.linkedin.com/in/dragosstanciu'),
          ('github', 'https://github.com/dnstanciu'),
          ('twitter', 'https://twitter.com/dnstanciu'),)

# MENUITEMS = (('Archives', '/blog/archives.html'),
#              ('Categories', '/blog/categories.html'))#,
             #('Tags', '/blog/tags.html'),)

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
