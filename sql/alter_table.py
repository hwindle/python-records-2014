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
from PyQt4.QtSql import *


def alter_table(tablename, fields):
    if not fields:
        print("You did not enter any fields!")
        return False
    query = QSqlQuery()
    if tablename:      
        sql = "ALTER " + tablename + "(" + fields + ")"
        if query.exec_(sql):
            print("Hooray you've created a table")
            return True
        else:
            print("Table creation failed at SQL level")
    else:
        print("No tablename given")
        return False

