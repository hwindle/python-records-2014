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

import settings # Records configuration file, has tablename, data directories.
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from PyQt4.QtSql import *
import ui.widgets.insertTableView

__version__ = "0.1"

class TableViewTab():

    def __init__(self):
        """

        Create a QAbstractTableModel with delegate parts for 
        enumerated lists and boolean values later on.
        """
        tablesAvail = []
        self.query = QSqlQuery(self.dbase)
        self.query.exec_("SELECT name FROM sqlite_master WHERE type='table'")
        while self.query.next():
            tablename = self.query.record()
            tablesAvail.append(tablename.value(0))
        QApplication.processEvents()
        self.model = QSqlRelationalTableModel()
        self.tableListBox = QListWidget()
        self.tableListBox.setMaximumWidth(200)
        self.tableview = QTableView() # or custom table class
        self.insertWidget = ui.widgets.insertTableView.InsertWidget()
        self.insertWidget.setMaximumHeight(40)
        self.insertWidget.showDlg()
        self.connect(self.insertWidget.addRow, SIGNAL("clicked()"), self.insertRefresh)
        tableLayout = QHBoxLayout()
        tableViewPage = QWidget()
        updateTableBtn = QPushButton(self.tr("Show &Table"))
        delButton = QPushButton(self.tr("Delete Row"))
        rightLayout = QVBoxLayout()
        rightLayout.addWidget(self.tableListBox)
        rightLayout.addWidget(updateTableBtn)
        rightLayout.addWidget(self.insertWidget)
        rightLayout.addWidget(delButton)
        tableLayout.addWidget(self.tableview, 3)
        tableLayout.addLayout(rightLayout, 1)
        self.connect(updateTableBtn, SIGNAL("clicked()"), self.updateTable)
        self.connect(delButton, SIGNAL("clicked()"), self.deleteRecord)

        self.tableListBox.addItems(tablesAvail)
        if settings.tablename == "":
            settings.tablename = str(tablesAvail[0])
        self.model.setTable(settings.tablename) # create updateTable function, find cur index in listbox
        self.tableview.setModel(self.model)
        self.model.select()
        self.tableview.setSelectionMode(QTableView.SingleSelection)
        self.tableview.resizeColumnsToContents()
        self.tableview.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        horizHeadings = self.tableview.horizontalHeader()
        rowHeadings = self.tableview.verticalHeader()

        tableDescr, self.colNum = self.tableInfo(settings.tablename)  # goes in form view
        tableViewPage.setLayout(tableLayout)
        tableViewPage.setFocus()
        QApplication.processEvents()
        self.tableViewRefresh() 
 
