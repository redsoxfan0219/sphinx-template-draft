# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'Templates Demo'
copyright = '2023, Ben Barksdale'
author = 'Ben Barksdale'


# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = ["myst_parser",
"sphinxcontrib.datatemplates",
"sphinx_jinja"]

templates_path = ['_templates']
exclude_patterns = []

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'furo'
html_static_path = ['_static']

# -- Loading Data for Documentation ------

# This system uses Jinja2 to use data files to create
# parts of the documentation. You can learn basic Jinja2
# syntax here: https://documentation.bloomreach.com/engagement/docs/jinja-syntax


## General procedure:
## 1. Add .csv or .json file to _static/ folder
## 2. Load file into Python via one of the processes below
## 3. Add data variable to html_context, following the
##    syntax:
##    html_context {
##    'data_dictionary' = data_dictionary_data,
##    'json_data_text' = json_data
##    }
## 4. In the doc files, access the data using the value
##    of the string variable. For example:  
##    {{ data_dictionary[1] }}
##    You can also use conditional logic, for loops, etc.
##    See the link above for further syntax details.

# CSV

import pandas as pd
names = pd.read_csv('names.csv')

# JSON

# import json
# file = open('_static/file.json')
# data = json.load(file)

html_context = {
    'names': names
}

# -- Jinja2 templating ------

# Don't touch this section

def rstjinja(app, docname, source):
    """
    Render our pages as a jinja template for fancy templating goodness.
    """
    # Make sure we're outputting HTML
    if app.builder.format != 'html':
        return
    src = source[0]
    rendered = app.builder.templates.render_string(
        src, app.config.html_context
    )
    source[0] = rendered

def setup(app):
    app.connect("source-read", rstjinja)




