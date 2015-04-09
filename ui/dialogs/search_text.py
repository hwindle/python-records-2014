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
from PyQt4.QtSql import *
sys.path.append("../../sql")
from sql import utils, select


class SearchDlg(QDialog):

    def __init__(self, parent=None):
        """

        """
        super(SearchDlg, self).__init__(parent)
        dbutils = utils.SQLutils()

        label1 = QLabel("Search in: ")
        self.tableCombo = QComboBox()
        tableList = dbutils.get_tables()
        viewList = dbutils.get_views()
        tableList.append(viewList)
        #self.tableLabel = QLabel()
        # get tables for combo
        i = 0
        for name in tableList:
            self.tableCombo.addItem(tableList[i])
        label2 = QLabel("In the field: ")
        self.tablename = tableList[0]
        self.fieldCombo = QComboBox()
        # get fields for combo
        self.fieldList = dbutils.get_fieldnames(self.tablename)
        self.fieldCombo.addItems(self.fieldList)
        self.fieldCombo.setCurrentIndex(1)
        self.searchOptionList = QListWidget()
        self.searchOptionList.setMinimumWidth(160)
        self.searchOptionList.setMinimumWidth(200)
        searchList = ["Contains", "Less than", "Greater than", "Equals"]
        self.searchOptionList.addItems(searchList)
        # search term (string)
        self.stringLineEdit = QLineEdit()

        buttonBox = QDialogButtonBox(QDialogButtonBox.Ok|QDialogButtonBox.Cancel)
        self.connect(buttonBox, SIGNAL("accepted()"), self.accept)
        self.connect(buttonBox, SIGNAL("rejected()"), self.reject)
        self.connect(self.tableCombo, SIGNAL("activated(int)"), self.updateCombo)
        self.connect(self.fieldCombo, SIGNAL("activated(int)"), self.updateCombo)        
        self.connect(self.searchOptionList, SIGNAL("activated(int)"), self.updateCombo)

        self.setWindowTitle("Records - Search")
        layout = QGridLayout()
        layout.addWidget(label1, 0, 0)
        layout.addWidget(self.tableCombo, 0, 1)
        layout.addWidget(label2, 1, 0)
        layout.addWidget(self.fieldCombo, 1, 1)
        layout.addWidget(self.searchOptionList, 2, 0)
        layout.addWidget(self.stringLineEdit, 3, 0)
        layout.addWidget(buttonBox, 4, 0)
        self.setLayout(layout)


    def fetchData(self):
        """

        """
        self.updateCombo()
        searchType = ""
        if "Contains" in self.searchOpt:
            cleanedTerm = self.cleanSearchTerm(self.stringLineEdit.text())
            searchType = "LIKE"
        elif "Equals" in self.searchOpt:
            cleanedTerm = self.cleanSearchTerm(self.stringLineEdit.text(), type_="num")
            searchType = "="
        elif "Less than" in self.searchOpt:
            cleanedTerm = self.cleanSearchTerm(self.stringLineEdit.text(), type_="num")
            searchType = "<"
        elif "Greater than" in self.searchOpt:
            cleanedTerm = self.cleanSearchTerm(self.stringLineEdit.text(), type_="num")
            searchType = ">"
        # build up the statement
        sqlString = "SELECT * FROM " + self.tablename + " WHERE " + self.fieldSelected + " " + searchType + " " + cleanedTerm
        print(sqlString)
        results = select.select_query(self.tablename, sqlString)
        print(results)
        return results


    def updateCombo(self):
        """

        """
        self.tablename = self.tableCombo.currentText()
        self.fieldSelected = self.fieldCombo.currentText()
        searchRow = self.searchOptionList.currentRow()
        searchItem = self.searchOptionList.item(searchRow)
        self.searchOpt = searchItem.text()


    def cleanSearchTerm(self, string=None, type_="text"):
        """

        """
        import re
        if "num" in type_:
            if not string: return False
            string = re.sub(r"[^0-9]*", "", string)
            print("num: ", string)
            return string
        else:
            if not string: return False
            string = re.sub(r"[;\"=]*", "", string)
            string = string.strip()
            newstring = "'%" + string 
            newstring += "%'"
            print("string: ", newstring)
            return newstring

