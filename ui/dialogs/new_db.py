#!/usr/bin/env python3

# -*- coding: UTF8 -*-

"""
/********************************************************
* Records - an easy to use database client, opens sqlite3 databases. 
* You can also search, create queries and reports easily.
* Part of Paradise Office
* Copyright (c) Hazel Windle
* 
*
* This program is free  software; you can redistribute it and/or
* modify it under the terms of the GNU General Public License
* as published by the Free Software Foundation; either version 2
* of the License, or (at your option) any later version.
*
* This program is distributed in the hope that it will be useful,
* but WITHOUT ANY WARRANTY; without even the implied warranty of
* MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
* GNU General Public License for more details.
*
* You should have received a copy of the GNU General Public License
* along with this program; if not, write to the Free Software
* Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301, USA.
* Also add information on how to contact you by electronic and paper mail.
*
**********************************************************/
"""

from PyQt4.QtCore import *
from PyQt4.QtGui import *
from ui.dialogs import ui_newdb
import os

class NewdbDialog(QDialog, ui_newdb.Ui_Dialog): 
    
    def __init__(self, parent=None):
        super(NewdbDialog, self).__init__(parent)
        self.setupUi(self)
        self.connect(self.browseBtn, SIGNAL("clicked()"), self.getPath)
        
        
    def validateStuff(self):
        path = self.pathLineEdit.text()
        if path[:-1] != "/":
            path += "/"
        filenameDirty = self.filenameLineEdit.text()

        if os.path.isdir(path):
            badChars = ":;~# .+=*%^\"/\\"
            # make sure the filename doesn't contain spaces, or weird characters like ;, strip these.
            for char in badChars:
                if char is " ":
                    filenameDirty.replace(char, "_")
                filenameDirty.replace(char, "")
            # add a .sqlite file ending to the filename to denote it as a SQLite database.
            if filenameDirty[:-7] != ".sqlite":
                filenameDirty += ".sqlite"
            
            filename = os.path.join(path, filenameDirty)
        return filename
    
    def getPath(self):
        filepath = QFileDialog.getExistingDirectory(self, "Records - Choose Folder")
        self.pathLineEdit.setText(filepath)

