# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
# import os
# import sys
# sys.path.insert(0, os.path.abspath('.'))


# -- Project information -----------------------------------------------------

project = 'Teoría de la Computación - Criptografía'
copyright = '2020, Alejandro Mantilla,\n Camilo Gutierrez,\n Federico Galvez\n'
author = 'Alejandro Mantilla, Camilo Gutierrez, Federico Galvez'
show_sphinx = False


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    "myst_nb",
    # "nbsphinx",
    # "myst_parser",
    "sphinx_copybutton",
    # "IPython.sphinxext.ipython_console_highlighting",
    "sphinx_thebe",
]

# MySt - Markdown Config.

myst_admonition_enable = True

myst_heading_anchors = 3

myst_dmath_enable=True

myst_dmath_allow_labels=True

myst_amsmath_enable = True

myst_update_mathjax=False

# MySt - Notebook Config.

# source_suffix = {
#     '.rst': 'restructuredtext',
#     '.ipynb': 'myst-nb',
#     '.myst': 'myst-nb',
# }

jupyter_execute_notebooks = "force"

# Thebe Config

thebe_config = {
    "repository_url": "https://github.com/MantiMantilla/Theory-of-Computation-Encryption",
    "path_to_docs": "criptografia-book",
    "repository_branch": "main",
    "selector": "div.section",
    "selector_input": "div.cell_input",
    "selector_output": "div.cell_output",
    "codemirror-theme": "monokai"  # Doesn't currently work
}


# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#
# This is also used if you do content translation via gettext catalogs.
# Usually you set "language" from the command line for these cases.
language = 'es'

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store', '**.ipynb_checkpoints']


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'furo'
html_title = "T. de la Computación - Criptografía"

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

html_css_files = [
    'css/custom.css',
]

html_theme_options = {
    "light_logo": "logo_uniandes.png",
    "dark_logo": "logo_uniandes_dark_mode.png",

}