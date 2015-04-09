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
from PyQt4.QtSql import *
#import qrc_records

__version__ = "0.1"


class SQLutils():

    def __init__(self):
        """

        """
        super(SQLutils, self).__init__()
        self.utilQuery = QSqlQuery()


    def table_info(self, tablename):
        if tablename is None:
            return
        #query2 = QSqlQuery(self.dbase)
        descr_tables = "PRAGMA table_info(" + tablename + ")"
        self.utilQuery.exec_(descr_tables)
        schema = {}
        columns = 0
        while self.utilQuery.next():
            row = self.utilQuery.record()
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


    def get_fieldnames(self, tablename):
        """
        tablename may be a view name
        """
        schema, columns = self.table_info(tablename)
        fieldnames = []
        for i in range(len(schema)):
            field = schema[i]
            fieldnames.append(field[0])
        print(fieldnames)
        return fieldnames


    def get_tables(self):
        self.utilQuery.exec_("SELECT name FROM sqlite_master WHERE type='table'")
        tablesList = []
        while self.utilQuery.next():
            tablename = self.utilQuery.record()
            tablesList.append(tablename.value(0))
        QApplication.processEvents()
        return tablesList


    def get_views(self):
        self.utilQuery.exec_("SELECT name FROM sqlite_master WHERE type='view'")
        viewsList = []
        while self.utilQuery.next():
            viewname = self.utilQuery.record()
            viewsList.append(viewname.value(0))
        QApplication.processEvents()
        return viewsList


