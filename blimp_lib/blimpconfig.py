# -*- Mode: Python; coding: utf-8; indent-tabs-mode: nil; tab-width: 4 -*-
### BEGIN LICENSE
# This file is in the public domain
### END LICENSE

### DO NOT EDIT THIS FILE ###

__all__ = [
    'project_path_not_found',
    'get_data_file',
    'get_data_path',
    ]

# Where your project will look for your data (for instance, images and ui
# files). By default, this is ../data, relative your trunk layout
__blimp_data_directory__ = '../data/'
__license__ = ''
__version__ = 'VERSION'

import os

from locale import gettext as _

class project_path_not_found(Exception):
    """Raised when we can't find the project directory."""


def get_data_file(*path_segments):
    """Get the full path to a data file.

    Returns the path to a file underneath the data directory (as defined by
    `get_data_path`). Equivalent to os.path.join(get_data_path(),
    *path_segments).
    """
    return os.path.join(get_data_path(), *path_segments)


def get_data_path():
    """Retrieve blimp data path

    This path is by default <blimp_lib_path>/../data/ in trunk
    and /usr/share/blimp in an installed version but this path
    is specified at installation time.
    """

    # Get pathname absolute or relative.
    path = os.path.join(
        os.path.dirname(__file__), __blimp_data_directory__)

    abs_data_path = os.path.abspath(path)
    if not os.path.exists(abs_data_path):
        raise project_path_not_found

    return abs_data_path


def get_version():
    return __version__
