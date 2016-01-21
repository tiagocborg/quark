# -*- coding: utf-8 -*-
#
# slackpack documentation build configuration file, created by Quark
extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.napoleon'
]
templates_path = ['_templates']
source_suffix = '.rst'
master_doc = 'index'
project = u'slackpack'
copyright = u'2015, slackpack authors'
author = u'slackpack authors'
version = '0.1.0'
release = '0.1.0'
language = None
exclude_patterns = ['_build']
pygments_style = 'sphinx'
todo_include_todos = False
html_theme = 'alabaster'
html_static_path = ['_static']
htmlhelp_basename = 'slackpackdoc'
latex_elements = {}
latex_documents = [
    (master_doc, 'slackpack.tex', u'slackpack Documentation',
     u'slackpack authors', 'manual'),
]
man_pages = [
    (master_doc, 'slackpack', u'slackpack Documentation',
     [author], 1)
]
texinfo_documents = [
    (master_doc, 'slackpack', u'slackpack Documentation',
     author, 'slackpack', 'One line description of slackpack.',
     'Miscellaneous'),
]
