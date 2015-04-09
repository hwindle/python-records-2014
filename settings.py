#!/usr/bin/env python3

tablename = ""
picklesDir = ".records"
dbname = ""

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

"""
