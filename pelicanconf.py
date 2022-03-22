from datetime import datetime

AUTHOR = 'Freddie Larkins'
SITENAME = "Freddie's SEO Blog ://"

# -- testing the below -- #
SITETITLE = "Freddie Larkins" 
SITEDESCRIPTION = 'Home of the ramblings of an SEO currently working for Zoopla.'
SITESUBTITLE = 'SEO, Python and other stuff.'
#-- end test -- #

SITEURL = ''

DISPLAY_PAGES_ON_MENU = False

PATH = 'content'

STATIC_PATHS = ['images', 'pdfs']

TIMEZONE = 'Europe/London'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('cv', '/pdfs/freddie-larkins-cv.pdf'),
         ('about me', '/pages/about-me.html'),
         ('archives', '/archives.html'))

# Social widget
SOCIAL = (('github', 'https://www.github.com/fredlarkins/'),
          ('linkedin', 'https://www.linkedin.com/in/freddielarkins/'),)

DEFAULT_PAGINATION = 3

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True

# theme specific stuff: Flex
THEME = 'themes/Flex-modified'
# THEME_COLOR_AUTO_DETECT_BROWSER_PREFERENCE = True
THEME_COLOR_ENABLE_USER_OVERRIDE = True

# MAIN_MENU = False

# from https://github.com/pelican-plugins/sitemap
SITEMAP = {
    "format": "xml",
    "priorities": {
        "articles": 0.5,
        "indexes": 0.5,
        "pages": 0.5
    },
    "changefreqs": {
        "articles": "yearly",
        "indexes": "monthly",
        "pages": "yearly"
    }
}

CC_LICENSE = {
    "name": "Creative Commons Attribution-ShareAlike 4.0 International License",
    "version": "4.0",
    "slug": "by-sa",
    "icon": True,
    "language": "en_GB",
}

COPYRIGHT_YEAR = datetime.now().strftime('%B %Y') # and month, technically