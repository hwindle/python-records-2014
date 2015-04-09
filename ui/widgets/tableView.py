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


class TableWidget(QTableWidget):

    def __init__(self, resultHash, tablename, parent=None):
        super(TableWidget, self).__init__(parent)
        self.tableView(resultHash, tablename)


    # for row in result_set: for field in row:
    def tableView(self, resultSet, tablename):
        """
        Initialises a tab with a table view widget inside of it.

        Create a QAbstractTableModel with delegate parts for 
        enumerated lists and boolean values later on.
        """
        if not resultSet: return False
        #self.model = QSqlRelationalTableModel()
        #self.model.setTable(tablename) 
        #self.setModel(self.model) # private method call
        #self.model.select() 
        #self.setSelectionMode(QTableWidget.SingleSelection)
        totalRows = len(resultSet)
        totalCols = len(resultSet[totalRows - 1])
        self.setRowCount(totalRows)
        self.setColumnCount(totalCols)
        #self.resizeColumnsToContents()
        self.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        horizHeadings = self.horizontalHeader()      
        rowHeadings = self.verticalHeader()
        self.tableViewRefresh(resultSet)    

   
    def tableViewRefresh(self, resultSet):
        """

        """
        colNum = 0
        recordNum = 0
        
        for row in resultSet:
            print("No of records in set: ", recordNum)
            for field in row:
                newcell = QTableWidgetItem(field)
                #newcell.setSizeHint(QSize(200, 30))
                self.setItem(recordNum, colNum, newcell)
                colNum += 1
            recordNum += 1
        self.resizeColumnsToContents()
        print("newcell: ", newcell, "\ncol: ", colNum, "row: ", recordNum)


    """         
    def insertRefresh(self):
        rowNum = self.model.rowCount()
        index = self.model.index(rowNum, 0)
        self.tableview.setCurrentIndex(index)
        self.model.insertRow(rowNum)
        self.tableview.edit(rowNum) 
        self.tableview.showRow(rowNum)
        self.tableview.editTriggers(QAbstractItemView.AllEditTriggers)
        self.connect(self.insertWidget.addRow, SIGNAL("triggered()"), self.savedb)


    def updateTable(self):
        # Updates the tablename variable in settings, on button press "Show Table".
        row = self.tableListBox.currentRow()
        settings.tablename = self.tableListBox.item(row).text()
        print("settings.tablename: ", settings.tablename)
        self.tableView()


    def tableInfo(self, tablename):
        if tablename is None:
            return
        query2 = QSqlQuery(self.dbase)
        descr_tables = "PRAGMA table_info(" + tablename + ")"
        query2.exec_(descr_tables)
        schema = {}
        columns = 0
        while query2.next():
            row = query2.record() 
            key = row.value(0) # should be an int, 0 for first column
            field_info = []
            field_info.append(row.value(1)) # fieldname
            field_info.append(row.value(2)) # data type (varchar etc)
            field_info.append(row.value(3)) # not null flag
            field_info.append(row.value(4)) # column default value
            field_info.append(row.value(5)) # primary key or not?
            schema.update({ key: field_info })
            columns += 1
        QApplication.processEvents()
        return schema, columns
    """
