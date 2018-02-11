#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# jdu documentation build configuration file, created by
# sphinx-quickstart on Sun Dec 10 15:22:35 2017.
#
# This file is execfile()d with the current directory set to its
# containing dir.
#
# Note that not all possible configuration values are present in this
# autogenerated file.
#
# All configuration values have a default; values that are commented out
# serve to show the default.

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
# import os
# import sys
# sys.path.insert(0, os.path.abspath('.'))


# -- General configuration ------------------------------------------------

# If your documentation needs a minimal Sphinx version, state it here.
#
# needs_sphinx = '1.0'

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.

import sys, os

print(os.path.abspath('../custombuilder'))
sys.path.append(os.path.abspath('../custombuilder'))

extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.doctest',
    'sphinx.ext.intersphinx',
    'sphinx.ext.coverage',
    'sphinx.ext.mathjax',
    'sphinx.ext.viewcode',
    'sphinx.ext.ifconfig',
    'matplotlib.sphinxext.plot_directive',
    'custombuilder'
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# The suffix(es) of source filenames.
# You can specify multiple suffix as a list of string:
#
# source_suffix = ['.rst', '.md']
source_suffix = '.rst'

# The master toctree document.
master_doc = 'index'

# General information about the project.
project = 'ML FutureIsTech'
copyright = '2017, Julien Dubiel'
author = 'Julien Dubiel'

# The version info for the project you're documenting, acts as replacement for
# |version| and |release|, also used in various other places throughout the
# built documents.
#
# The short X.Y version.
version = ''
# The full version, including alpha/beta/rc tags.
release = ''

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#
# This is also used if you do content translation via gettext catalogs.
# Usually you set "language" from the command line for these cases.
language = "fr"

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This patterns also effect to html_static_path and html_extra_path
exclude_patterns = []

# The name of the Pygments (syntax highlighting) style to use.
#pygments_style = 'monokai'

# If true, `todo` and `todoList` produce output, else they produce nothing.
todo_include_todos = True


# -- Options for HTML output ----------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'theme'
html_theme_path = ['..']

html_context = {
    'site_name': 'ML FutureIsTech',
    'site_description': 'Jdu Sphinx Template by Julien Dubiel'
}

# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.
#
# html_theme_options = {}
html_favicon = 'favicon.ico'
# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['../theme/static']

# Custom sidebar templates, must be a dictionary that maps document names
# to template names.
#
# This is required for the alabaster theme
# refs: http://alabaster.readthedocs.io/en/latest/installation.html#sidebars
#html_sidebars = {
#    '**': [
#        'relations.html',  # needs 'show_related': True theme option to display
#        'searchbox.html',
#    ]
#}


# -- Options for HTMLHelp output ------------------------------------------

# Output file base name for HTML help builder.
#htmlhelp_basename = 'jdudoc'

mathjax_path = 'https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.2/MathJax.js?config=TeX-AMS-MML_HTMLorMML'

# -- Options for LaTeX output ---------------------------------------------

latex_elements = {
    # The paper size ('letterpaper' or 'a4paper').
    #
    # 'papersize': 'letterpaper',

    # The font size ('10pt', '11pt' or '12pt').
    #
    'pointsize': '8pt',

    # Additional stuff for the LaTeX preamble.
    #
    # 'preamble': '',

    # Latex figure (float) alignment
    #
    # 'figure_align': 'htbp',
}

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title,
#  author, documentclass [howto, manual, or own class]).
# latex_documents = [
#     (master_doc, 'jdu.tex', 'jdu Documentation', 'Julien Dubiel', 'manual'),
# ]


# -- Options for manual page output ---------------------------------------

# One entry per manual page. List of tuples
# (source start file, name, description, authors, manual section).
# man_pages = [
#     (master_doc, 'jdu', 'jdu Documentation', [author], 1)
# ]


# -- Options for Texinfo output -------------------------------------------

# Grouping the document tree into Texinfo files. List of tuples
# (source start file, target name, title, author,
#  dir menu entry, description, category)
# texinfo_documents = [
#     (master_doc, 'jdu', 'jdu Documentation',
#      author, 'jdu', 'One line description of project.',
#      'Miscellaneous'),
# ]

# String included at begining of all 
rst_prolog = """
.. role:: red
.. role:: purple
.. role:: blue
.. role:: green
.. role:: yellow
.. role:: pink
.. role:: orange
.. role:: grey


.. math::

   \\definecolor{red}{RGB}{255,0,0}
   \\definecolor{purple}{RGB}{128,0,128}
   \\definecolor{blue}{RGB}{0,0,255}
   \\definecolor{green}{RGB}{0,255,0}
   \\definecolor{yellow}{RGB}{255,255,0}
   \\definecolor{pink}{RGB}{255,192,203}
   \\definecolor{orange}{RGB}{255,165,0}
   \\definecolor{grey}{RGB}{128,128,128}
   \\newcommand{\\R}{\_mathbb{R}}
   \\newcommand{\\Z}{\\mathbb{Z}}
   \\newcommand{\\N}{\\mathbb{N}}
   \\newcommand{\\P}{\\mathbb{P}}
   \\newcommand\\given[1][]{\\:#1\\vert\\:}
   \\DeclareMathOperator{\\Corr}{Corr}
   \\DeclareMathOperator{\\Cov}{Cov}

"""