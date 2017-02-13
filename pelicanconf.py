#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Евгений Загородний'
SITENAME = 'Евгений Загородний'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'Europe/Kiev'

DEFAULT_LANG = 'ru'
DEFAULT_DATE_FORMAT = '%Y-%m-%d'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

AUTHORS_SAVE_AS = None
CATEGORIES_SAVE_AS = None
TAGS_SAVE_AS = None
ARCHIVES_SAVE_AS = None

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),
         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = ((
        'BitBucket',
        'https://bitbucket.org/ezag/',
    ), (
        'CodinGame',
        'https://www.codingame.com'
        '/profile/35bede9fa9bcc51d0a3449206cfbe675779671',
    ), (
        'Coursera',
        'https://www.coursera.org/user/i/61c141a4b3a5d44868479a8073424dd0',
    ), (
        'GitHub',
        'https://github.com/ezag',
    ), (
        'GitLab',
        'https://gitlab.com/e.zag',
    ), (
        'Google+',
        'https://plus.google.com/u/0/102533519110366328367',
    ), (
        'HackerRank',
        'https://www.hackerrank.com/e_zag',
    ), (
        'Instagram',
        'https://www.instagram.com/e.zag/',
    ), (
        'Kaggle',
        'https://www.kaggle.com/ezagorodniy',
    ), (
        'LinkedIn',
        'https://www.linkedin.com/in/e-zag/',
    ), (
        'LiveJournal',
        'http://zag87.livejournal.com/',
    ), (
        'Quora',
        'https://www.quora.com/profile/Eugen-Zagorodniy',
    ), (
        'StackExchange',
        'http://stackexchange.com/users/198746/zag',
    ), (
        'Twitter',
        'https://twitter.com/e4zag',
    ), (
        'YouTube',
        'https://www.youtube.com/channel/UCiqZm9vM8SjcOt80mdttgxg',
    ), (
        'ВКонтакте',
        'https://vk.com/e.zagorodniy',
))

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

THEME = 'zag'

STATIC_PATHS = (
    'images',
    'extra/CNAME',
)
EXTRA_PATH_METADATA = {
    'extra/CNAME': {
        'path': 'CNAME',
    },
}

WITH_FUTURE_DATES = False
SUMMARY_MAX_LENGTH = 200
USE_FOLDER_AS_CATEGORY = False

ARTICLE_URL = '{date:%Y}/{date:%m}/{date:%d}/{page_order}/{slug}/'
ARTICLE_SAVE_AS = ARTICLE_URL + 'index.html'
PAGE_URL = ARTICLE_URL
PAGE_SAVE_AS = ARTICLE_SAVE_AS
PATH_METADATA = (
    '(?P<date>\d{4}[-/]\d{2}[-/]\d{2})[\./]'
    '(?P<page_order>\d{1})\.'
    '(?P<slug>.*)\.rst'
)
