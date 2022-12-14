# Configuration file for the Sphinx documentation builder.

# -- Project information

project = 'Counter Social'
copyright = '2022, Counter Social'
author = 'Counter Social'

release = '1.0'
version = '0.1.0'

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

templates_path = ['_templates']

# -- Options for HTML output

html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']
html_logo = '_images/html_logo.png'
html_theme_options = {
    'logo_only': True,
    'display_version': False,
    }
html_css_files = ['css/custom.css',
                  ('print.css', {'media': 'print'})]

# -- Add custom stylesheet
def setup(app):
    app.add_stylesheet('css/custom.css')

# -- Options for EPUB output
epub_show_urls = 'footnote'