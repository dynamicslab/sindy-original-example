# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

from pathlib import Path
from shutil import copy, rmtree, copytree

from sphinx.application import Sphinx

project = 'pysindy-example'
copyright = '2024, Jacob Stevens-Haas'
author = 'Jacob Stevens-Haas'
release = '0.1'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    "nbsphinx",
    "IPython.sphinxext.ipython_console_highlighting",
]

templates_path = ['_templates']
exclude_patterns = []



# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = "sphinx_rtd_theme"

def setup(app: Sphinx):
    """Copy files from repo/examples to repo/docs/_sources/examples"""
    docs = Path(__file__).absolute().parents[1]
    examples_from =  docs.parent / "examples"
    examples_to = docs / "source" / "examples"
    if examples_to.exists():
        rmtree(examples_to)
    copytree(examples_from, examples_to)
