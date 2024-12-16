# Sphinx config

extensions = [
    # first-party
    "sphinx.ext.autodoc",
    "sphinx.ext.todo",
    "sphinx.ext.extlinks",
    "sphinx.ext.intersphinx",
    # third-party
    "sphinx_copybutton",
]

language = "es"
project = "Negociador"
author = "Diego Ramirez"
copyright = "2024-present, Diego Ramirez"

# version = ...
# release = version

html_theme = "furo"
