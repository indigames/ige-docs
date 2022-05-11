# Configuration file for the Sphinx documentation builder.

# -- Project information

project = 'Indi Games Engine'
copyright = '2022, Indigames'
author = 'admin@indigames.net'

release = '0.0.1'
version = '0.0.1'

# -- General configuration
extensions = [
    'sphinx.ext.duration',
    'sphinx.ext.doctest',
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.intersphinx',
]

intersphinx_mapping = {
    'python': ('https://docs.python.org/3/', None),
    'sphinx': ('https://www.sphinx-doc.org/en/master/', None),
}
intersphinx_disabled_domains = ['std']

# -- Options for HTML output
html_theme = 'sphinx_rtd_theme'

# -- Options for EPUB output
epub_show_urls = 'footnote'

# -- Turn on sphinx.ext.autosummary
autosummary_generate = True 

# -- If no docstring, inherit from base class
autodoc_inherit_docstrings = True

# -- Add templates paths
templates_path = ['_templates']

# -- Add any paths that contain custom static files
html_static_path = ['_static']
