# Configuration file for Sphinx documentation

import os
import sys

sys.path.insert(0, os.path.abspath('../..'))

extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.viewcode',
    'sphinx.ext.napoleon',
]

templates_path = ['_templates']

source_suffix = '.rst'

master_doc = 'index'

project = 'pManager'
copyright = '2025, Qwantman'
author = 'Qwantman'

version = '1'
release = ''

language = 'en'

exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

html_theme = 'alabaster'

html_static_path = ['_static']