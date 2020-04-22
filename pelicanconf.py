#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals

AUTHOR = "Talha Mansoor"
SITENAME = """<span style="color:black;">onCrash</span> <span style="color:darkblue;">=</span> <span style="color:#AA1032;">'reboot();'</span>"""
SITEURL = ""
SITESUBTITLE = "You can, you should, and if you're brave enough to start, you will."

PATH = "content"

# Regional Settings
TIMEZONE = "Asia/Karachi"
DATE_FORMATS = {"en": "%b %d, %Y"}

# Plugins and extensions
MARKDOWN = {
    "extension_configs": {
        "markdown.extensions.admonition": {},
        "markdown.extensions.codehilite": {"css_class": "highlight"},
        "markdown.extensions.extra": {},
        "markdown.extensions.meta": {},
        "markdown.extensions.sane_lists": {},
        "markdown.extensions.toc": {"permalink": " "},
    }
}
PLUGIN_PATHS = ["plugins"]
PLUGINS = [
    "assets",
    "extract_toc",
    "liquid_tags.include_code",
    "neighbors",
    "related_posts",
    "series",
    "share_post",
    "tipue_search",
]
SITEMAP = {
    "format": "xml",
    "priorities": {"articles": 0.5, "indexes": 0.5, "pages": 0.5},
    "changefreqs": {"articles": "monthly", "indexes": "daily", "pages": "monthly"},
}

# Appearance
TYPOGRIFY = True
THEME = "themes/elegant"
DEFAULT_PAGINATION = False

# Defaults
DEFAULT_CATEGORY = "Miscellaneous"
USE_FOLDER_AS_CATEGORY = False
ARTICLE_URL = "{slug}"
PAGE_URL = "{slug}"
PAGE_SAVE_AS = "{slug}.html"
TAGS_URL = "tags"
CATEGORIES_URL = "categories"
ARCHIVES_URL = "archives"
SEARCH_URL = "search"

# Feeds
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None
CATEGORY_FEED_ATOM = None
CATEGORY_FEED_RSS = None

# Social
SOCIAL = (
    ("Email", "mailto:talha131@gmail.com", "My Emaill Address"),
    ("Github", "https://github.com/talha131/", "My Github Profile"),
    ("GoodReads", "https://www.goodreads.com/talha131"),
    ("Keybase", "https://keybase.io/talha131"),
    ("RSS", SITEURL + "/feeds/all.atom.xml"),
)

STATIC_PATHS = [
    "theme/images",
    "images",
    "extra/_redirects",
    "extra/robots.txt",
    "extra/keybase.txt",
    "code",
]
EXTRA_PATH_METADATA = {
    "extra/_redirects": {"path": "_redirects"},
    "extra/robots.txt": {"path": "robots.txt"},
    "extra/keybase.txt": {"path": "keybase.txt"},
}

DIRECT_TEMPLATES = ("index", "tags", "categories", "archives", "search", "404")
TAG_SAVE_AS = ""
AUTHOR_SAVE_AS = ""
CATEGORY_SAVE_AS = ""
USE_SHORTCUT_ICONS = True

# Elegant Labels
SOCIAL_PROFILE_LABEL = "Stay in Touch"
RELATED_POSTS_LABEL = "Keep Reading"
SHARE_POST_INTRO = "Like this post? Share on:"
COMMENTS_INTRO = """So what do you think? Did I miss something? Is any part unclear?
            Leave your comments below.
        """

# Mailchimp
EMAIL_SUBSCRIPTION_LABEL = "Get New Posts In Your Inbox"
EMAIL_FIELD_PLACEHOLDER = "Enter your email..."
SUBSCRIBE_BUTTON_TITLE = "Subscribe Me"
MAILCHIMP_FORM_ACTION = "empty"

# SMO
TWITTER_USERNAME = "talham_"
FEATURED_IMAGE = SITEURL + "/theme/images/apple-touch-icon-152x152.png"

# Legal
SITE_LICENSE = """Content licensed under <a rel="license nofollow noopener noreferrer"
    href="http://creativecommons.org/licenses/by/4.0/" target="_blank">
    Creative Commons Attribution 4.0 International License</a>."""
HOSTED_ON = {"name": "Netlify", "url": "https://www.netlify.com/"}

# SEO
SITE_DESCRIPTION = "My name is Talha Mansoor \u2015 a software engineer who gets things done. I am talha131 at Github and @talham_ at twitter. I design and build software products for iOS and OSX. I work on Jump Desktop which is a remote desktop application for iOS, OSX and Android. This is my personal blog."

# Landing Page
PROJECTS = [
    {
        "name": "Coding School",
        "url": "https://www.codingschool.pk/",
        "description": "A project to teach programming using C#",
    },
    {
        "name": "Elegant",
        "url": "http://oncrashreboot.com/pelican-elegant",
        "description": "A clean and distraction free Pelican theme, with"
        " search and a"
        " lot more unique features. Built with Jinja2 and Bootstrap",
    },
    {
        "name": "extract_toc",
        "url": "https://github.com/getpelican/pelican-plugins/tree/master/extract_toc",
        "description": "A Pelican plugin to extract table of contents",
    },
    {
        "name": "tipue_search",
        "url": "https://github.com/getpelican/pelican-plugins/tree/master/tipue_search",
        "description": "A Pelican plugin to serialize generated HTML to a JavaScript variable that can be used by jQuery plugin - Tipue Search",
    },
    {
        "name": "share_post",
        "url": "https://github.com/getpelican/pelican-plugins/tree/master/share_post",
        "description": "A Pelican plugin to create share URLs of article",
    },
    {
        "name": "goodreads_activity",
        "url": "https://github.com/getpelican/pelican-plugins/tree/master/goodreads_activity",
        "description": "A Pelican plugin to lists books from your GoodReads shelves",
    },
    {
        "name": "TiddlyWiki",
        "url": "https://github.com/Jermolene/TiddlyWiki5/commits?author=talha131",
        "description": "My contributions to TiddlyWiki, a self-contained JavaScript wiki",
    },
    {
        "name": "Pelican Plugins",
        "url": "https://github.com/getpelican/pelican-plugins/commits?author=talha131",
        "description": "My contributions to plugins for Pelican blog engine",
    },
    {
        "name": "Pelican",
        "url": "https://github.com/getpelican/pelican/commits?author=talha131",
        "description": "Static site generator that supports Markdown and"
        " reST syntax",
    },
    {
        "name": "coc-lists",
        "url": "https://github.com/neoclide/coc-lists/commits?author=talha131",
        "description": "Common lists extension for coc.nvim",
    },
    {
        "name": "Logpad + Duration",
        "url": "https://github.com/talha131/logpad-plus-duration#logpad--duration",
        "description": "Vim plugin to emulate Windows Notepad logging feature,"
        " and log duration of each entry",
    },
    {
        "name": "Asana to Github Issues",
        "url": "https://github.com/talha131/AsanaToGithub#asana-to-github",
        "description": "Command-line program to move your tasks from Asana"
        " projects to Github issues",
    },
    {
        "name": "Asana",
        "url": "https://github.com/pandemicsyn/asana/commits?author=talha131",
        "description": "Python Asana API bindings",
    },
    {
        "name": "Ctags",
        "url": "https://github.com/fishman/ctags/commits?author=talha131",
        "description": "Exuberant Ctags clone with ObjectiveC and CSS support",
    },
    {
        "name": "Wasavi",
        "url": "https://github.com/akahuku/wasavi/commits?author=talha131",
        "description": "A browser extension that changes textarea element to"
        " Vi editor",
    },
]

LANDING_PAGE_TITLE = "I am a Polyglot Seasoned Software Engineer"
