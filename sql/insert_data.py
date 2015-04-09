#!/usr/bin/env python3

# -*- coding: UTF8 -*-

from PyQt4.QtCore import *
from PyQt4.QtSql import *


class InsertData():

    def __init__(self):
        """
        This class inserts the data in datalist into a table, on the currently opened database.
       
        The validation and data cleansing is done in the form UI, and the validation settings
        are loaded from a separate file. TODO: add extra checking for bad chars in datalist in
        case of table view insertions like 'DROP tables;' or double quotes.
        """
        pass


    def insert_data(self, tablename, tableinfo, datalist):
        query = QSqlQuery()
        # data sanitation
        #if datalist:  [self.clean_field(x) for x in datalist]

        #QSqlDatabase.database().transaction() # uncomment for transactions
        bindstring = "" 
        colNum = len(tableinfo)
        for x in range(colNum):
            bindstring += "?" + ", "
        columnNames = ""
        for num in range(colNum):
            columnNames += tableinfo[num][0] 
            columnNames += ", "
        insertQuery = 'INSERT INTO ' + tablename + '(' + columnNames[:-2] + ')' + ' VALUES (' + bindstring[:-2] + ')'
        query.prepare(insertQuery)
        for i in range(colNum):
            query.addBindValue(datalist[i])
        if query.exec_(): 
            print("Insert query success")
        
        return True


