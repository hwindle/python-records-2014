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

import os
#from ui.dialogs import ui_create_table
from PyQt4.QtCore import *
from PyQt4.QtGui import *

class CreateTableDialog(QDialog):

    def __init__(self, parent=None):
        super(CreateTableDialog, self).__init__(parent)
        self.tableTable = QTableWidget()
        self.tableTable.setMinimumSize(500, 370)
        self.tableTable.setColumnCount(5)
        self.tableTable.setRowCount(1)
        tableHeaders = ["Field Name", "Data Type", "Required", "Default Value", "Key"]
        self.tableTable.setHorizontalHeaderLabels(tableHeaders)
        	
        self.makeFieldRow(0)
        self.noOfFields = 0
        templateLabel = QLabel("Template: ")
        self.templateCombo = QComboBox()
        self.templateList = ["blank database"]
        self.templateCombo.addItems(self.templateList)
        noOfFieldsLabel = QLabel(str(self.noOfFields) + " fields")
        topLayout = QHBoxLayout()
        topLayout.addWidget(templateLabel)
        topLayout.addWidget(self.templateCombo)
        topLayout.addStretch(1)
        topLayout.addWidget(noOfFieldsLabel)
        # side bit
        insertFieldBtn = QPushButton(self.tr("&Insert Field"))
        deleteFieldBtn = QPushButton(self.tr("&Delete Field"))
        tableLabel = QLabel(self.tr("Table Name"))
        self.tablenameEdit = QLineEdit()
        self.tablenameEdit.setText("Tablename1")
        self.tablenameEdit.setFocus(True)
        sideLayout = QVBoxLayout()
        sideLayout.addWidget(tableLabel)
        sideLayout.addWidget(self.tablenameEdit)
        sideLayout.addStretch(1)
        sideLayout.addWidget(insertFieldBtn)
        sideLayout.addWidget(deleteFieldBtn)
        sideLayout.addStretch(1)
        # table and top layout
        leftBit = QVBoxLayout()
        leftBit.addLayout(topLayout)
        leftBit.addWidget(self.tableTable)
        # OK and Cancel
        self.buttonBox = QDialogButtonBox(QDialogButtonBox.Ok|QDialogButtonBox.Cancel)
        # main Layout
        mainLayout = QGridLayout()
        mainLayout.addLayout(leftBit, 0, 0)
        mainLayout.addLayout(sideLayout, 0, 1)
        mainLayout.addWidget(self.buttonBox, 1, 0)
        # connections
        self.connect(insertFieldBtn, SIGNAL("clicked()"), self.newField)
        self.connect(deleteFieldBtn, SIGNAL("clicked()"), self.deleteField)
        #self.connect(self.tableTable, SIGNAL("currentCellChanged(int)"), self.updateFieldName)
        self.connect(self.buttonBox, SIGNAL("accepted()"), self.accept)
        self.connect(self.buttonBox, SIGNAL("rejected()"), self.reject)
        self.connect(self.buttonBox, SIGNAL("accepted()"), self.dialogAccepted)
        # final bits
        self.setWindowTitle("Create Table")
        self.setLayout(mainLayout)
        

    def newField(self):
        # get rows in table table
        rows = self.tableTable.currentRow()
        rows += 1
        self.tableTable.insertRow(rows)
        # call makeFieldRow, with rows + 1
        self.makeFieldRow(rows)
        self.noOfFields += 1


    def deleteField(self):
        current = self.tableTable.currentRow()
        self.tableTable.removeRow(current)
        self.noOfFields -= 1
        

    def makeFieldRow(self, row):
        self.fieldNameEdit = QLineEdit()
        self.tableTable.setCellWidget(row, 0, self.fieldNameEdit)
        dataTypeList = ["text", "decimal", "whole number", "long number", "notes", "date", "timestamp", "date time", "True or False", "Data blob"]
        self.dataTypeCombo = QComboBox()
        self.dataTypeCombo.addItems(dataTypeList)
        self.dataTypeCombo.setMinimumSize(100, 20)
        self.tableTable.setCellWidget(row, 1, self.dataTypeCombo)
        keyTypeList = ["None", "Primary", "Index"]
        self.keyTypeCombo = QComboBox()
        self.keyTypeCombo.addItems(keyTypeList)
        self.keyTypeCombo.setMinimumSize(80, 20)
        self.tableTable.setCellWidget(row, 4, self.keyTypeCombo)
        self.nullCheckBox = QCheckBox()
        self.nullCheckBox.setChecked(False)
        self.tableTable.setCellWidget(row, 2, self.nullCheckBox)
        self.defaultEdit = QLineEdit()
        self.tableTable.setCellWidget(row, 3, self.defaultEdit)
        # focus policy for row, 0 of table table.
        #self.connect(self.dataTypeCombo, SIGNAL("currentIndexChanged(int)"), self.refreshDialog)
        #self.connect(self.keyTypeCombo, SIGNAL("currentIndexChanged(int)"), self.refreshDialog)
        #self.connect(self.nullCheckBox, SIGNAL("stateChanged(int)"), self.refreshDialog)
		
	
    def refreshDialog(self):
        dataType = self.dataTypeCombo.currentText()
        keyType = self.keyTypeCombo.currentText()
        nullValue = self.nullCheckBox.isChecked()

    
    def valid_sql_fieldnames(self, string):
        cleanString1 = string.replace(" ", "_")
        for char in "!\"£$%^&*()+=#~@?\'|":
            cleanString2 = cleanString1.replace(char, "")
        return cleanString2 

    def dialogAccepted(self):
        #fieldnames = []
        #fdataTypes = []
        #nulls = []
        #defaultValues = []
        table = self.tablenameEdit.text()
        sql = "CREATE TABLE " + table
        info = []
        tableStruct = []        
        i = 0
        rows = self.tableTable.rowCount()
        while i < rows:
            fieldstrings = ""
            widgetArray = []
            cols = self.tableTable.columnCount()
            info.append([])
            for j in range(cols):
                widgetArray.append(self.tableTable.cellWidget(i, j))
            if not info[i].append(widgetArray[0].text()):
                #QMessageBox.warning(self, 'Field Names Missing', \
                #        "You have forgot to include a field name.")
                pass
            fieldstrings += info[i][0]
            # Data Types
            info[i].append(widgetArray[1].currentText())
            if "whole number" in info[i][1]:
                fieldstrings += " INTEGER"
            elif "long number" in info[i][1]:
                fieldstrings += " UNSIGNED INTEGER"
            elif "text" in info[i][1]:
                fieldstrings += " VARCHAR(200)"
            elif "notes" in info[i][1]:
                fieldstrings += " VARCHAR(10000)"
            elif "decimal" in info[i][1]:
                fieldstrings += " REAL"
            elif info[i][1] == "date":
                fieldstrings += " DATE"
            elif "timestamp" in info[i][1]:
                fieldstrings += " TIMESTAMP"
            elif "date time" in info[i][1]:
                fieldstrings += " DATETIME"
            elif "True" in info[i][1]:
                fieldstrings += " CHAR(1)"
            elif "Data blob" in info[i][1]:
                fieldstrings += " BINARY"
            else:
                fieldstrings += " VARCHAR(200)"
            # Null ?
            info[i].append(widgetArray[2].isChecked())
            if info[i][2]:
                fieldstrings += " NOT NULL"
            # default values
            info[i].append(widgetArray[3].text())
            if not info[i][3]:
                pass
            else:
                fieldstrings += " DEFAULT "
                nums = ["whole number", "long number"]
                if info[i][1] in nums:
                    fieldstrings += int(info[i][3])
                elif "decimal" in info[i][1]:
                    fieldstrings += float(info[i][3])
                else:
                    fieldstrings += "'" + str(info[i][3]) + "'"
            # keys
            info[i].append(widgetArray[4].currentText())
            if info[i][4]:
                if "ndex" in info[i][4]:
                    fieldstrings = info[i][0] + " INTEGER NOT NULL"
                elif "rimary" in info[i][4]:
                    fieldstrings = info[i][0] + " INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE NOT NULL"
            tableStruct.append(fieldstrings)
            i += 1
        #print("(", tableStruct, ",")
        sql += " ("
        middle = ""
        for item in tableStruct:
            middle += item + ", "
        sql += middle[:-2] + ")"
        print(sql)
        from sql import create_table
        if create_table.create_table(table, sql):
            print("OK at dialog end")
        else:
            print("Mistake in 228 of create edit table")

if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    form = CreateTableDialog()
    form.show()
    app.exec_()

    
