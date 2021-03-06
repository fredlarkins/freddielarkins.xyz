from datetime import datetime

AUTHOR = 'Freddie Larkins'
SITENAME = "Freddie's SEO Blog ://"

# -- testing the below -- #
SITETITLE = "Freddie Larkins" 
SITEDESCRIPTION = 'Home of the ramblings of an SEO currently working for Zoopla.'
SITESUBTITLE = 'SEO, Python and other stuff.'
SITELOGO = '/images/webp/freddie-larkins-mugshot.webp'
#-- end test -- #

SITEURL = 'https://freddielarkins.xyz'

DISPLAY_PAGES_ON_MENU = False

PATH = 'content'

STATIC_PATHS = ['images', 'pdfs', 'excel-files']

PAGE_PATHS = ['pages', 'errors']

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Side nav
LINKS = (   ('home', '/'),
            ('cv', '/pdfs/freddie-larkins-cv.pdf'),
            ('about me', '/pages/about-me.html'),)

SOCIAL = (('github', 'https://www.github.com/fredlarkins/'),
          ('linkedin', 'https://www.linkedin.com/in/freddielarkins/'),)

DEFAULT_PAGINATION = 3

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True

# theme specific stuff: Flex
THEME = 'themes/Flex-fredlarkins-modified'
THEME_COLOR_AUTO_DETECT_BROWSER_PREFERENCE = True
THEME_COLOR_ENABLE_USER_OVERRIDE = True


# Top nav
MAIN_MENU = True
MENUITEMS = (
    ("Archives", "/archives.html"),
    ("Python", "/category/python.html"),
    ("SEO", "/category/seo.html"),
)

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
    },
    "exclude": {
        "/pages/403-access-denied.html",
        "/pages/404-not-found.html"
    }
}

PLUGIN_PATHS = ['plugins']

PLUGINS = ['post_stats', 'sitemap', 'seo']

# the settings for the SEO plugin
SEO_REPORT = False
SEO_ENHANCER = True # the only setting I want
SEO_ENHANCER_OPEN_GRAPH = False
SEO_ENHANCER_TWITTER_CARDS = False

# CC_LICENSE = {
#     "name": "Creative Commons Attribution-ShareAlike 4.0 International License",
#     "version": "4.0",
#     "slug": "by-sa",
#     "icon": True,
#     "language": "en_GB",
# }

COPYRIGHT_YEAR = f"Freddie Larkins {datetime.now().strftime('%B %Y')}" # and month, technically

'''
Settings taken from from https://cloudbytes.dev/snippets/add-a-table-of-contents-using-markdown-in-pelican
NOTE: keep an eye on this extension - a load of stuff broke when I commented out stuff
Docs for extension: https://python-markdown.github.io/extensions/toc/
'''

MARKDOWN = {
    "extension_configs": {
        # Needed for code syntax highlighting
        "markdown.extensions.codehilite": {"css_class": "highlight"},
        "markdown.extensions.extra": {},
        "markdown.extensions.meta": {},
        # This is for enabling the TOC generation
        "markdown.extensions.toc": {"title": None},
    },
    "output_format": "html5",
}

# language and timezone stuff
TIMEZONE = 'Europe/London'
I18N_TEMPLATES_LANG = "en"
DEFAULT_LANG = "en"
OG_LOCALE = "en_GB"
#LOCALE = "en_GB"