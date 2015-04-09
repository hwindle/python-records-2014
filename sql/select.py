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

def select_query(table, full_sql=None, search_sql=None, ordering=None, joins=None):
    """
    Search SQL is the optional search parameters to narrow down the 
    number of records.
    Both ordering and joins should also be in valid SQL.
 
    A list of lists is returned.
    """
    result_hash = []
    query = QSqlQuery()
    statement = "SELECT * FROM " + table
    if not full_sql:
        if search_sql:
            statement += search_sql
        if ordering:
            statement += ordering
        if joins:
            statement += joins
    statement = full_sql # plonk error checking here...
    if query.exec_(statement):
        i = 0  # row number
        while query.next():
            row = query.record()
            cols = row.count()
            j = 0
            result_hash.append([])
            while j < cols:
                result_hash[i].append(row.value(j))
                j += 1
            i += 1
        #print(result_hash) # debug
        return result_hash
    else:
        print("You entered the wrong SQL: ", statement)

def create_view(viewname, full_sql):
    sql = "CREATE VIEW " + viewname + " AS " + full_sql
    query = QSqlQuery()
    if query.exec_(statement):
        searchView = "SELECT * FROM " + viewname   
        results = select_query(viewname, searchView)
        return results
    else:
        print("View not created!")
        return False


