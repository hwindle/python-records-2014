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
from ui.dialogs import ui_add_comparison, ui_query_view


class QueryViewDlg(QDialog, ui_query_view.Ui_Dialog):

    def __init__(self, parent=None):
        """

        """
        super(QueryViewDlg, self).__init__(parent)
        self.setupUi(self)

        self.dbutils = utils.SQLutils()
        self.tableList = self.dbutils.get_tables()
        self.queryList = self.dbutils.get_views()
        # self.newQueryBtn # radiobutton (isChecked())
        self.viewName = cleanSearchTerm(self.newQueryName.text())
        # self.editQueryBtn # radiobutton (isChecked())
        for item in self.queryList:
            self.currentViewsList.addItem(item)
        # self.typeListWidget # for different pre built queries like duplicate rows.
        self.connect(self.typeListWidget, SIGNAL("activated(int)"), self.presetQueries)
        # self.descrLabelTab1 # description at bottom
        i = 0
        for name in self.tableList:
            self.tableCombo.addItem(self.tableList[i])
            self.tableSortCombo.addItem(self.tableList[i])
        self.tablename = self.tableList[0]
        self.fieldList = self.dbutils.get_fieldnames(self.tablename)
        self.fieldsListTab2.addItems(self.fieldList)
        self.compareList = ["Contains text", "Equals", "Less than", "Less than or equal", "Greater than", "Greater than or equal"]

        self.compareListTab2.addItems(self.compareList)
        #self.extraSql = []
        self.fields = []
        self.sortfields = []
        self.tables = []
        #self.comparison = ""
        # for fetchData method...
        self.sqltables = []
        self.sqlwheres = []
        # self.addCondBtn # calls other smaller dialog class
        self.term1 = cleanSearchTerm( self.value1LineEdit.text())
        # self.searchText # QTextBrowser, self.descrLabelTab2
        self.availFieldsList.addItems(self.fieldList)
        # self.addFieldBtn  self.delFieldBtn self.clearFieldsBtn
        self.connect(self.addFieldBtn, SIGNAL("clicked()"), self.addSortField)
        self.connect(self.delFieldBtn, SIGNAL("clicked()"), self.delSortField)
        self.connect(self.clearFieldsBtn, SIGNAL("clicked()"), self.clearSortFields)
        # self.ascBtn self.desBtn
        # self.sortedFieldsList # fields added here ascBtn and sorted, ascending default 
        self.connect(self.ascBtn, SIGNAL("clicked()"), self.ascFieldSort)
        self.connect(self.desBtn, SIGNAL("clicked()"), self.desFieldSort)
        self.connect(self.tableCombo, SIGNAL("activated(int)"), self.updateFields)
        self.connect(self.tableSortCombo, SIGNAL("activated(int)"), self.updateSortFields)
        self.connect(self.fieldsListTab2, SIGNAL("activated(int)"), self.getField)
        #self.connect(self.sortedFieldsList, SIGNAL("activated(int)"), self.getSortField)
        self.connect(self.compareListTab2, SIGNAL("activated(int)"), self.getComparison)
        self.connect(self.addCondBtn, SIGNAL("clicked()"),  self.add_other_term)
        self.updateFields()
        self.updateSortFields()



    def fetchData(self):
        """

        """
        # self.viewName
        # compare if structure
        if "Contains text" in self.comparison:
            compare = " LIKE "
        elif "Equals" in self.comparison:
            compare = " = "
        elif self.comparison == "Less than":
            compare = " < "
        elif self.comparison == "Less than or equal":
            compare = " <= "
        elif self.comparison == "Greater than":
            compare = " > "
        elif self.comparison == "Greater than or equal":
            compare = " >= "
        self.sqltables.append(self.tablename)
        sqlfields = [] # later on use in two table queries
        sqltables = list(set(sqltables)) # remove duplicates
        # self.tablename, self.field[0], self.sortfields[0], self.comparison, self.term1
        cols = " "
        for table in sqltables:
            tmpfields = self.dbutils.get_fieldnames(table)
            for field in tmpfields:
                cols += table + "." + field + ", "
        columns = cols[:-2] + " "
        cleanTerm = cleanSearchTerm(self.term1, type_="sqlstring")
        tmpwhere = self.field[-1] + compare + cleanTerm
        self.sqlwheres.append(tmpwhere)
        self.sqlsorts = []
        # ORDER BY tablename.col1 ASC, tablename.col2 DESC
        for sort in self.sortfields:
            if "(A - Z)" in sort:
                tmpSortField = str(sort[:-7].strip())
                tmpSortField += " ASC,"
            else:
                tmpSortField = str(sort[:-7].strip())
                tmpSortField += " DESC," 
            self.sqlsorts.append(tmpSortField)
        wholeSql = "SELECT " + columns + " FROM " + self.tablename + " WHERE " # + sqlwheres[0] + sqlsorts[0]
        for string in sqlwheres:
            wholeSql += string + ", "
        wholeSql += wholeSql[:-1]
        if self.sqlsorts:
            wholeSql += " ORDER BY "
        for string in self.sqlsorts:
            wholeSql += string 
        wholeSql += wholeSql[:-1]
        print(wholeSql)
        # CREATE VIEW v AS SELECT qty, price, qty*price AS value FROM t; # read only



    def updateFields(self):
        """

        """
        self.tablename = self.tableCombo.currentText()
        self.fieldsListTab2.addItems(self.dbutils.get_fieldnames(self.tablename))


    def updateSortFields(self):
        self.tablename = self.tableSortCombo.currentText()
        self.availFieldsList.addItems(self.dbutils.get_fieldnames(self.tablename))


    def getField(self):
        searchRow = self.fieldsListTab2.currentRow()
        searchItem = self.fieldsListTab2.item(searchRow)
        self.field.append(searchItem.text())


    def getSortField(self):
        rowcount = self.sortedFieldsList.count()
        i = 0
        while i <= rowcount:
            searchItem = self.sortedFieldsList.item(i)
            self.sortfields.append(searchItem.text())
            i += 1
        print("sort fields from getSortField: ", self.sortfields)    


    def getComparison(self):
        row = self.compareListTab2.currentRow()
        item = self.compareListTab2.item(row)
        self.comparison = item.text()



    def presetQueries(self):
        """
        row = self.typeListWidget.currentRow()
        item = self.typeListWidget.item(row)
        runThis = item.text()
        """
        # if to choose runThis sql, pass to fetch data...
        pass


    def addSortField(self):
        row = self.availFieldsList.currentRow()
        item = self.availFieldsList.item(row)
        self.sortedFieldsList.addItem(item.text() + " (A - Z)")


    def delSortField(self):
        row = self.sortedFieldsList.currentRow()
        item = self.sortedFieldsList.item(row)
        takenField = self.sortedFieldsList.takeItem(item)
        del takenField


    def clearSortFields(self):
        self.sortedFieldsList.clear()


    def ascFieldSort(self):
        row = self.sortedFieldsList.currentRow()
        item = self.sortedFieldsList.item(row)
        oldtext = item.text()
        field = oldtext[:-7].strip()
        item.setText(field + " (A - Z)")


    def desFieldSort(self):
        row = self.sortedFieldsList.currentRow()
        item = self.sortedFieldsList.item(row)
        oldtext = item.text()
        field = oldtext[:-7].strip()
        item.setText(field + " (Z - A)")


    def add_other_term(self):
        dialog = AddCompDialog()
        if dialog.exec_() == QDialog.Accepted:
            tmptable, tmpwheres = dialog.fetchData()
            self.sqltables.append(tmptable)
            self.sqlwheres.append(tmpwheres)
        else:
            print("Problem with adding that term, did you press cancel?")    




class AddCompDialog(QDialog, ui_add_comparison.Ui_Dialog):

    def __init__(self, parent=None):
        """

        """
        super(AddCompDialog, self).__init__(parent)
        self.setupUi(self)
        self.setWindowTitle("Records - Add another Term")
        # self.compareCombo self.tableCombo self.fieldCombo self.andButton self.orButton
        # self.valueLineEdit
        self.connect(self.andButton, SIGNAL("clicked()"), self.updateThings)
        self.connect(self.orButton, SIGNAL("clicked()"), self.updateThings)
        self.connect(self.tableCombo, SIGNAL("activated(int)"), self.updateThings)
        self.connect(self.fieldCombo, SIGNAL("activated(int)"), self.updateThings)
        self.connect(self.compareCombo, SIGNAL("activated(int)"), self.updateThings)



    def updateThings(self):
        if self.andButton.isChecked():
            self.logicaltype = " AND "
        elif self.orButton.isChecked():
            self.logicaltype = " OR "
        else:
            self.logicaltype = " AND "
        self.tablename = self.tableCombo.currentText()
        self.fieldname = self.fieldCombo.currentText()
        self.comparison = self.compareCombo.currentText()

    
    def fetchData(self):
        # returns tablename (goes in sqltables), where string (added to sqlwheres)
        # wherestr = "AND|OR " + field + compare + term
        dirtyTerm = self.valueLineEdit.text()
        cleanTerm = cleanSearchTerm(dirtyTerm, type_="sqlstring")
        wherestr = self.logicaltype
        wherestr += self.fieldname + " "
        wherestr += self.comparison + " "
        wherestr += self.searchterm + " "
        return self.tablename, wherestr



def cleanSearchTerm(string=None, type_="string"):
    """

    """
    import re
    if not string: return False
    string = re.sub(r"[';\"=]*", "", string)
    string = string.strip()
    if "sqlstring" in type_:
        if re.search(r"[0-9]*[.]?[0-9]*", string):
            # string is a number
            newstring = string
            return newstring
        else:
            # string gets %'s round it for SQL pattern matching.
            newstring = "'%" + string 
            newstring += "%'"
            return newstring
    else:
        return newstring

