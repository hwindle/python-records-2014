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
from ui.dialogs import ui_report_new_dlg
sys.path.append("../../sql")
from sql import utils


class NewReportDialog(QDialog, ui_report_new_dlg.Ui_Dialog):

    def __init__(self, fieldslist, parent=None):
        """

        """
        super(NewReportDialog, self).__init__(parent)
        self.setupUi(self)
        self.setWindowTitle(self.tr("New Report"))
        if not fieldslist:
            fieldslist = []
        self.fieldslist = fieldslist
        self.titleLineEdit.setFocus()
        tableList = []
        self.dbutils = utils.SQLutils()
        tableList = self.dbutils.get_tables()
        self.tableCombo.addItems(tableList)
        viewList = self.dbutils.get_views()
        self.viewCombo.addItems(viewList)
        self.curTableOrView = self.tableCombo.currentText()
        fieldsList = self.dbutils.get_fieldnames(self.curTableOrView)
        # self.fieldsListBox is a QScrollArea
        self.fieldsListRefresh(fieldsList)
        self.sortFieldCombo.addItems(fieldsList)
        # connections
        self.connect(self.tableCombo, SIGNAL("activated(int)"), self.updateTableField)
        self.connect(self.viewCombo, SIGNAL("activated(int)"), self.updateViewField)
        self.connect(self.browseBtn, SIGNAL("clicked()"), self.browsePath)


    def updateTableField(self):
        currentTable = self.tableCombo.currentText()
        fieldsList = self.dbutils.get_fieldnames(currentTable)        
        self.fieldsListRefresh(fieldsList)
        self.sortFieldCombo.clear()
        self.sortFieldCombo.addItems(fieldsList)
        self.curTableOrView = currentTable


    def updateViewField(self):
        currentView = self.viewCombo.currentText()
        fieldsList = self.dbutils.get_fieldnames(currentView)
        self.fieldsListRefresh(fieldsList)
        self.sortFieldCombo.clear()
        self.sortFieldCombo.addItems(fieldsList)
        self.curTableOrView = currentView


    def fieldsListRefresh(self, fieldsList):
        """

        """
        colCount = len(fieldsList)
        fieldsLayout = QVBoxLayout()
        self.fieldCheckList = []
        for i in range(colCount):        
            self.fieldCheckList.append(QCheckBox(fieldsList[i]))
            fieldsLayout.addWidget(self.fieldCheckList[i])
        innerWidget = QWidget()           
        innerWidget.setLayout(fieldsLayout)
        self.fieldsListBox.setWidget(innerWidget)


    def browsePath(self):
        """

        """
        path = QFileDialog.getExistingDirectory(self, "Records - Save Report In")
        self.pathLineEdit.setText(path)


    def fetchData(self):
        """

        """
        titleDirty = self.titleLineEdit.text()
        wrongChars = ":;~#*.+=%^\"/\\"
        titleClean = ""
        for char in titleDirty:
            if char not in wrongChars:
                titleClean += char
        reportFPath = self.cleanFileName(titleClean)
        print(reportFPath)
        columns = ""
        for i in range(len(self.fieldCheckList)):
            if self.fieldCheckList[i].isChecked():
                columns += self.fieldCheckList[i].text() + ","
        #print(columns[:-1])
        reportSQL = "SELECT " + columns[:-1] + " FROM "
        if not self.tableCombo.currentText() and not self.viewCombo.currentText():
            print("Please put stuff into your database before making a report")
        if self.curTableOrView:
            reportSQL += self.curTableOrView
        sortField = self.sortFieldCombo.currentText()
        reportSQL += " ORDER BY " + sortField
        if self.ascRadioBtn.isChecked():
            reportSQL += " ASC"
        elif self.descRadioBtn.isChecked():
            reportSQL += " DESC"
        #print(reportSQL)
        themeNum = self.themesListWidget.currentRow() + 1
        print(themeNum)
        from sql import select
        resulthash = select.select_query(self.curTableOrView, reportSQL)
        from reports import  css_js_changer, html_generator       
        css_js_changer.update_css(themeNum)
        columnsList = columns.split(",")
        middleTable = html_generator.tabular_html(titleClean, resulthash, columnsList)
        if html_generator.construct_page(reportFPath, middleTable):
            return reportFPath 
        else:
            return reportFPath


    def cleanFileName(self, title):
        """

        """
        if not title: return False
        for char in title:
            if char in " ": title.replace(char, "_")
        title += ".html"
        pathDirty = self.pathLineEdit.text()
        if os.path.isdir(pathDirty):
            fullPath = os.path.join(pathDirty, title.replace(" ", "_"))
            return fullPath
        return False

