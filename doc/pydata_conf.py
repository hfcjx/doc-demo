# -*- coding: utf-8 -*-
#
# wslay documentation build configuration file, created by
# sphinx-quickstart on Sun Jan  8 22:37:36 2012.
#
# This file is execfile()d with the current directory set to its containing dir.
#
# Note that not all possible configuration values are present in this
# autogenerated file.
#
# All configuration values have a default; values that are commented out
# serve to show the default.

import sys, os

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#sys.path.insert(0, os.path.abspath('.'))

# -- General configuration -----------------------------------------------------

# If your documentation needs a minimal Sphinx version, state it here.
#needs_sphinx = '1.0'

# Add any Sphinx extension module names here, as strings. They can be extensions
# coming with Sphinx (named 'sphinx.ext.*') or your custom ones.
extensions = [] 

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# The suffix of source filenames.
source_suffix = '.rst'

# The encoding of source files.
#source_encoding = 'utf-8-sig'

# The master toctree document.
master_doc = 'index'

# General information about the project.
project = u'wslay'
copyright = u'2012, 2015, Tatsuhiro Tsujikawa'

# The version info for the project you're documenting, acts as replacement for
# |version| and |release|, also used in various other places throughout the
# built documents.
#
# The short X.Y version.
version = '@PACKAGE_VERSION@'
# The full version, including alpha/beta/rc tags.
release = '@PACKAGE_VERSION@'

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#language = None

# There are two options for replacing |today|: either, you set today to some
# non-false value, then it is used:
#today = ''
# Else, today_fmt is used as the format for a strftime call.
#today_fmt = '%B %d, %Y'

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
exclude_patterns = ['_build']

# The reST default role (used for this markup: `text`) to use for all documents.
#default_role = None

# If true, '()' will be appended to :func: etc. cross-reference text.
#add_function_parentheses = True

# If true, the current module name will be prepended to all description
# unit titles (such as .. function::).
#add_module_names = True

# If true, sectionauthor and moduleauthor directives will be shown in the
# output. They are ignored by default.
#show_authors = False

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'sphinx'

# A list of ignored prefixes for module index sorting.
#modindex_common_prefix = []


# -- Options for HTML output ---------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#html_theme = 'agogo'
#html_theme = 'sphinx_rtd_theme'
#import sphinx_bootstrap_theme
#html_theme = 'pydata_sphinx_theme'
html_theme = 'pydata_sphinx_theme'

# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.
html_theme_options = {'bodyfont':'roboto, sans-serif',
                      'headfont':'roboto, "Trebuchet MS", sans-serif'}

# Add any paths that contain custom themes here, relative to this directory.
#html_theme_path = []

# The name for this set of Sphinx documents.  If None, it defaults to
# "<project> v<release> documentation".
#html_title = None

# A shorter title for the navigation bar.  Default is the same as html_title.
#html_short_title = None

# The name of an image file (relative to this directory) to place at the top
# of the sidebar.
#html_logo = None

# The name of an image file (within the static path) to use as favicon of the
# docs.  This file should be a Windows icon file (.ico) being 16x16 or 32x32
# pixels large.
#html_favicon = None

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static/default2.css']

# If not '', a 'Last updated on:' timestamp is inserted at every page bottom,
# using the given strftime format.
#html_last_updated_fmt = '%b %d, %Y'

# If true, SmartyPants will be used to convert quotes and dashes to
# typographically correct entities.
#html_use_smartypants = True

# Custom sidebar templates, maps document names to template names.
#html_sidebars = {}

# Additional templates that should be rendered to pages, maps page names to
# template names.
#html_additional_pages = {}

# If false, no module index is generated.
#html_domain_indices = True

# If false, no index is generated.
#html_use_index = True

# If true, the index is split into individual pages for each letter.
#html_split_index = False

# If true, links to the reST sources are added to the pages.
#html_show_sourcelink = True

# If true, "Created using Sphinx" is shown in the HTML footer. Default is True.
#html_show_sphinx = True

# If true, "(C) Copyright ..." is shown in the HTML footer. Default is True.
#html_show_copyright = True

# If true, an OpenSearch description file will be output, and all pages will
# contain a <link> tag referring to it.  The value of this option must be the
# base URL from which the finished HTML is served.
#html_use_opensearch = ''

# This is the file name suffix for HTML files (e.g. ".xhtml").
#html_file_suffix = None

# Output file base name for HTML help builder.
htmlhelp_basename = 'wslaydoc'


# -- Options for LaTeX output --------------------------------------------------

# The paper size ('letter' or 'a4').
#latex_paper_size = 'letter'

# The font size ('10pt', '11pt' or '12pt').
#latex_font_size = '10pt'

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title, author, documentclass [howto/manual]).
latex_documents = [
  ('index', 'wslay.tex', u'wslay Documentation',
   u'Tatsuhiro Tsujikawa', 'manual'),
]

# The name of an image file (relative to this directory) to place at the top of
# the title page.
#latex_logo = None

# For "manual" documents, if this is true, then toplevel headings are parts,
# not chapters.
#latex_use_parts = False

# If true, show page references after internal links.
#latex_show_pagerefs = False

# If true, show URL addresses after external links.
#latex_show_urls = False

# Additional stuff for the LaTeX preamble.
#latex_preamble = ''

# Documents to append as an appendix to all manuals.
#latex_appendices = []

# If false, no module index is generated.
#latex_domain_indices = True


# -- Options for manual page output --------------------------------------------

# One entry per manual page. List of tuples
# (source start file, name, description, authors, manual section).
man_pages = [
    ('man/wslay_event_context_server_init', 'wslay_event_context_server_init',
     u'Initialize an event-based API context', [u'Tatsuhiro Tsujikawa'], 3),
    ('man/wslay_event_context_server_init', 'wslay_event_context_client_init',
     u'Initialize an event-based API context', [u'Tatsuhiro Tsujikawa'], 3),
    ('man/wslay_event_context_server_init', 'wslay_event_context_free',
     u'Initialize an event-based API context', [u'Tatsuhiro Tsujikawa'], 3),

    ('man/wslay_event_config_set_no_buffering',
     'wslay_event_config_set_no_buffering',
     u'Enable or disable buffering of an entire message for non-control frames',
     [u'Tatsuhiro Tsujikawa'], 3),
    ('man/wslay_event_config_set_max_recv_msg_length',
     'wslay_event_config_set_max_recv_msg_length',
     u'Set maximum length of a message that can be received',
     [u'Tatsuhiro Tsujikawa'], 3),
    ('man/wslay_event_config_set_callbacks',
     'wslay_event_config_set_callbacks',
     u'Set callback functions',
     [u'Tatsuhiro Tsujikawa'], 3),
    ('man/wslay_event_config_set_allowed_rsv_bits',
     'wslay_event_config_set_allowed_rsv_bits',
     u'Set allowed reserved bits',
     [u'Tatsuhiro Tsujikawa'], 3),

    ('man/wslay_event_queue_close', 'wslay_event_queue_close',
     u'Queue a close control frame', [u'Tatsuhiro Tsujikawa'], 3),
    ('man/wslay_event_queue_fragmented_msg', 'wslay_event_queue_fragmented_msg',
     u'Queue a fragmented message for future transmission',
     [u'Tatsuhiro Tsujikawa'], 3),
    ('man/wslay_event_queue_fragmented_msg',
     'wslay_event_queue_fragmented_msg_ex',
     u'Queue a fragmented message for future transmission',
     [u'Tatsuhiro Tsujikawa'], 3),
    ('man/wslay_event_queue_msg', 'wslay_event_queue_msg',
     u'Queue a message for future transmission', [u'Tatsuhiro Tsujikawa'], 3),
    ('man/wslay_event_queue_msg', 'wslay_event_queue_msg_ex',
     u'Queue a message for future transmission', [u'Tatsuhiro Tsujikawa'], 3),

    ('man/wslay_event_recv', 'wslay_event_recv',
     u'Receive messages', [u'Tatsuhiro Tsujikawa'], 3),
    ('man/wslay_event_send', 'wslay_event_send',
     u'Send any pending messages', [u'Tatsuhiro Tsujikawa'], 3),
    ('man/wslay_event_write', 'wslay_event_write',
     u'Write any pending messages to a buffer', [u'Tatsuhiro Tsujikawa'], 3),

    ('man/wslay_event_set_error', 'wslay_event_set_error',
     u'Set error code', [u'Tatsuhiro Tsujikawa'], 3),
    ('man/wslay_event_want_read', 'wslay_event_want_read',
     u'Tell whether the library wants to read more data',
     [u'Tatsuhiro Tsujikawa'], 3),
    ('man/wslay_event_want_write', 'wslay_event_want_write',
     u'Tell whether the library wants to send more data',
     [u'Tatsuhiro Tsujikawa'], 3),

    ('man/wslay_event_get_read_enabled', 'wslay_event_get_read_enabled',
     u'Query whether the event-based API context allows read operation',
     [u'Tatsuhiro Tsujikawa'], 3),
    ('man/wslay_event_get_write_enabled', 'wslay_event_get_write_enabled',
     u'Query whether the event-based API context allows write operation',
     [u'Tatsuhiro Tsujikawa'], 3),

    ('man/wslay_event_shutdown_read', 'wslay_event_shutdown_read',
     u'Disable read operation',
     [u'Tatsuhiro Tsujikawa'], 3),
    ('man/wslay_event_shutdown_write', 'wslay_event_shutdown_write',
     u'Disable write operation',
     [u'Tatsuhiro Tsujikawa'], 3),

    ('man/wslay_event_get_close_received', 'wslay_event_get_close_received',
     u'Query whether a close control frame has been received',
     [u'Tatsuhiro Tsujikawa'], 3),
    ('man/wslay_event_get_close_sent', 'wslay_event_get_close_sent',
     u'Query whether a close control frame has been sent',
     [u'Tatsuhiro Tsujikawa'], 3),

    ('man/wslay_event_get_status_code_received',
     'wslay_event_get_status_code_received',
     u'Return status code received in close control frame',
     [u'Tatsuhiro Tsujikawa'], 3),
    ('man/wslay_event_get_status_code_sent',
     'wslay_event_get_status_code_sent',
     u'Return status code sent in close control frame',
     [u'Tatsuhiro Tsujikawa'], 3),

    ('man/wslay_event_get_queued_msg_count', 'wslay_event_get_queued_msg_count',
     u'Get the number of queued messages', [u'Tatsuhiro Tsujikawa'], 3),
    ('man/wslay_event_get_queued_msg_length',
     'wslay_event_get_queued_msg_length',
     u'Get the sum of queued message length', [u'Tatsuhiro Tsujikawa'], 3),
    ]

def setup(app):
    app.add_css_file('default2.css')
