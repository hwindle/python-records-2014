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

import os, sys
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from PyQt4.QtWebKit import *
#import qrc_reports


class ReportsTab(QWidget):
    def __init__(self, parent=None):
        super(ReportsTab, self).__init__(parent)
        self.displayArea()


    def displayArea(self):
        #self.framewidget = QWidget()
        self.webFrame = QFrame(self)
        self.webView = QWebView()
        self.webView.setMinimumWidth(600)
        sideLayout = QWidget()
        sideLayout.setMinimumWidth(200)
        self.webLayout = QVBoxLayout()
        self.webLayout.addWidget(self.webView)
        self.webLayout.addWidget(sideLayout)
        self.setLayout(self.webLayout)
        abspath = os.path.abspath(".")
        localurl = abspath + "/reports/tests/test.html"
        #print(localurl)
        defaultPage = QUrl.fromLocalFile(localurl)
        #defaultPage = QUrl("http://www.linux-paradise.co.uk")
        #self.setCentralWidget(self.framewidget)
        self.displayUrl(defaultPage)
        #html = open(localurl).read()
        #self.displayHtml(html)


    def displayHtml(self, htmlfile):
        self.webView.setHtml(htmlfile)


    def displayUrl(self, filename):
        # display this url in the QWebKit view
        print("in display Url")
        try:
            self.webView.load(filename) # was setUrl
        except:
            print("Load didn't work")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    form = ReportsTab()
    form.show()
    app.exec_()

