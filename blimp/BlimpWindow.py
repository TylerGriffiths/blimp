# -*- Mode: Python; coding: utf-8; indent-tabs-mode: nil; tab-width: 4 -*-
### BEGIN LICENSE
# This file is in the public domain
### END LICENSE

from locale import gettext as _

from gi.repository import Gtk # pylint: disable=E0611
import logging
logger = logging.getLogger('blimp')

from blimp_lib import Window
from blimp.AboutBlimpDialog import AboutBlimpDialog
from blimp.PreferencesBlimpDialog import PreferencesBlimpDialog

# See blimp_lib.Window.py for more details about how this class works
class BlimpWindow(Window):
    __gtype_name__ = "BlimpWindow"
    
    def finish_initializing(self, builder): # pylint: disable=E1002
        """Set up the main window"""
        super(BlimpWindow, self).finish_initializing(builder)

        self.AboutDialog = AboutBlimpDialog
        self.PreferencesDialog = PreferencesBlimpDialog

        # Code for other initialization actions should be added here.

