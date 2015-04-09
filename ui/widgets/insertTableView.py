#!/usr/bin/env python3

# -*- coding: UTF8 -*-

from PyQt4.QtCore import *
from PyQt4.QtGui import *
import sql.insert_data
import pickle

class InsertWidget(QWidget):
    
    
    def __init__(self, parent=None):
        """
        This class supplies widgets for the form View, and reads in the validation pickle.
        """
        super(InsertWidget, self).__init__(parent)
        pass       

 
    # enumFields should be valid, enum database dict unpickled
    def read_field_checking(self, dbname):
        """
        There is one pickle per table, in the format 'dbname_tablename.pkl'.

        checks is a dictionary, 
        key: 0 (field index)
        ["validation string", ["enum", "string", "for", "a", "list"], minimum, max]
        """
        cleanDbname = os.path.basename(dbname)
        try:
            picklename = shortDbname[:-7] + "_" + settings.tablename + ".pkl"
            print(picklename)
            read_checks = open(picklename, "rb")
        finally:
            validationDict = None
        try:
            validationDict = pickle.load(read_checks)
        finally:
            read_checks.close()
        return validationDict


    def field_objects(self, tablename, tableinfo, dbname):
        """

        """
        if not tableinfo:
            return False
        self.tableinfo = tableinfo
        self.tablename = tablename
        validationDict = self.read_field_checking(dbname)
        colNum = len(tableinfo)
        self.fieldInputs = []; field = 0
        while field < colNum:
            if "char" in tableinfo[field][1] or "CHAR" in tableinfo[field][1]:
                try:
                    enumFields = validationDict[field][1] # get enum list
                except:
                    enumFields = []
                if enumFields:
                    # Create cute little enumerated list drop down
                    fieldObj = QComboBox()
                    fieldLine = tableinfo[field][0] + "Combo"
                    fieldObj.addItems(enumFields)
                    fieldObj.setObjectName(fieldLine)
                    self.fieldInputs.append(fieldObj)
                else:
                    self.widgetSetup(tableinfo[field][0], "string")
            elif "int" in tableinfo[field][1] or "INT" in tableinfo[field][1]:
                if tableinfo[field][3] != '':
                    pass
                    # field is a key, foreign or primary
                self.widgetSetup(tableinfo[field][1], "integer")
            elif "float FLOAT double DOUBLE numeric real REAL NUMERIC" in tableinfo[field][1]:
                self.widgetSetup(tableinfo[field][0], "double")
            elif "text" in tableinfo[field][1]:
                self.widgetSetup(tableinfo[field][0], "longtext")
            elif "date" in tableinfo[field][1]:
                self.widgetSetup(tableinfo[field][0], "date")
            elif "datetime" in tableinfo[field][1]:
                self.widgetSetup(tableinfo[field][0], "datetime")
                # no time field data type in sqlite3
            elif "bool" in tableinfo[field][1]:
                self.widgetSetup(tableinfo[field][0], "bool")
            else:
                self.widgetSetup(tableinfo[field][0], "string")
            field += 1
        #print("Have created some widgets")
        
        
       
    def showDlg(self):
        self.layoutFields()
        


    def widgetSetup(self, fieldname, widget):
        """

        """
        fieldLine = fieldname + widget[:-2]
        if widget == "string":
            fieldObj = QLineEdit()
        elif widget == "integer":
            fieldObj = QSpinBox()
        elif widget == "double":
            fieldObj = QDoubleSpinBox()
        elif widget == "longtext":
            fieldObj = QPlainTextEdit()
        elif widget == "date":
            fieldObj = QDateEdit()
        elif widget == "datetime":
            fieldObj = QDateTimeEdit()
        elif widget == "bool":
            fieldObj = QHBoxLayout()
            radio1 = QRadioButton("Y")
            radio2 = QRadioButton("N")
            fieldObj.addWidget(radio1)
            fieldObj.addWidget(radio2)
        # set a validator for fieldObj here, if on the strings, grab validators.py
        fieldObj.setObjectName(fieldLine)
        self.fieldInputs.append(fieldObj)


    def layoutFields(self):
        """

        """
        self.mainLayout = QGridLayout()
        #fieldTotal = len(self.fieldInputs)
        #row = 0
        #col = 0 
        #for num in range(fieldTotal):
            #if  isinstance( self.fieldInputs[num], QWidget):
                #self.mainLayout.addWidget(self.fieldInputs[num], row, col)
            #else:
                #self.mainLayout.addLayout(self.fieldInputs[num])
            #col += 1
            #if col > 2:
                #row += 1
                #col = 0
        #row += 1
        self.addRow = QPushButton("&Add Record")
        spacer = QLabel()
        self.mainLayout.addWidget(self.addRow, 0, 0 ) 
        #self.mainLayout.addWidget(self.addRow, row, 1)
        self.setLayout(self.mainLayout)
        self.connect(self.addRow, SIGNAL("clicked()"), self.updateValues)


    def updateValues(self, fieldValues):
        """

        """
        # add validation
        #self.fieldValues = []
        """
        for obj in self.fieldInputs:
            # get values
            if isinstance(obj, QLineEdit):
                self.fieldValues.append(obj.text())
            elif isinstance(obj, QSpinBox):
                self.fieldValues.append(obj.value()) 
            elif isinstance(obj, QDoubleSpinBox):
                self.fieldValues.append(obj.value()) 
            elif isinstance(obj, QPlainTextEdit):
                self.fieldValues.append(obj.toPlainText()) 
            elif isinstance(obj, QDateEdit):
                self.fieldValues.append(obj.date()) 
            elif isinstance(obj, QDateTimeEdit):
                self.fieldValues.append(obj.dateTime()) 
            elif isinstance(obj, QComboBox):
                self.fieldValues.append(obj.currentItem().text()) 
        """
        sqlInsert = sql.insert_data.InsertData()
        sqlInsert.insert_data(self.tablename, self.tableinfo, fieldValues)
        return True

