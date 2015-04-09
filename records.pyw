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

import settings # Records configuration file, has tablename, data directories.
import os, sys, platform, shutil
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from PyQt4.QtSql import *
import qrc_records
import ui.widgets.insertTableView

__version__ = "0.1"

class MainWindow(QMainWindow):
    

    def __init__(self, parent=None):
        """
        MainWindow - For setting up the menus, toolbars and the tabbed central widget as well as the status bar.
        """
        super(MainWindow, self).__init__(parent)

        self.viewsOpen = []
        self.tabArea = QTabWidget()
        self.tabArea.setTabsClosable(True)
        self.tabArea.tabCloseRequested.connect(self.closeTab)
        self.dirty = False
        self.setCentralWidget(self.tabArea)
        self.createMenus()
        self.createToolbars()
        self.createStatus()
        # load settings, win geometry
        settings = QSettings()
        self.recentDbs = settings.value("RecentDbs") or []
        self.restoreGeometry(settings.value("MainWindow/Geometry", QByteArray()))
        self.restoreState(settings.value("MainWindow/State", QByteArray()))
        self.setWindowTitle(self.tr("Records"))
        self.filename = ""
        self.dbase = QSqlDatabase.addDatabase("QSQLITE")
                
  
    def createMenus(self):
        """
        Builds the actions and menus.
        """
        
        self.fileMenu = self.menuBar().addMenu(self.tr("&File"))
        newAction = self.createAction(self.tr("&New"), self.newdb, QKeySequence.New, "win/filenew.png", self.tr("Create database"))
        self.openAction = self.createAction(self.tr("&Open"), self.opendb, QKeySequence.Open, "win/fileopen.png", self.tr("Open database"))
        saveAction = self.createAction(self.tr("&Save"), self.savedb, QKeySequence.Save, "win/filesave.png", self.tr("Save current file"))
        self.saveAsAction = self.createAction(self.tr("Save &As"), self.saveas, self.tr("Ctrl+Shift+S"), self.tr("Save database under a different name"))
        self.recentMenu = self.fileMenu.addMenu(self.tr("&Recent Files"))
        self.importAction = self.createAction(self.tr("&Import"), self.importdb, self.tr("Ctrl+Shift+I"), self.tr("Import a CSV"))
        self.exportAction = self.createAction(self.tr("&Export"), self.exportdb, self.tr("Ctrl+Shift+E"), self.tr("Export to CSV"))
        self.quitAction = self.createAction(self.tr("&Quit"), self.close, self.tr("Alt+F4"), "win/close_file_128x128.png", self.tr("Close the application"))
        self.addActions(self.fileMenu, (newAction, self.openAction, saveAction, self.saveAsAction, None,  self.importAction, self.exportAction, None, self.quitAction))
        
        editMenu = self.menuBar().addMenu(self.tr("&Edit"))
        self.cutAction = self.createAction(self.tr("Cu&t"), self.cutdata, QKeySequence.Cut, "win/editcut.png", self.tr("Move text onto the clipboard"))
        self.copyAction = self.createAction(self.tr("&Copy"), self.copydata, QKeySequence.Copy, "win/editcopy.png", self.tr("Copy data onto the clipboard"))
        self.pasteAction = self.createAction(self.tr("&Paste"), self.pastedata, QKeySequence.Paste, "win/editpaste.png", self.tr("Paste data from the clipboard"))
        self.delAction = self.createAction(self.tr("&Delete"), self.deldata, QKeySequence.Delete, "win/delete_128x128.png", self.tr("Remove selected text"))
        self.addActions(editMenu, (self.cutAction, self.copyAction, self.pasteAction, None, self.delAction ))
        
        viewMenu = self.menuBar().addMenu(self.tr("&View"))
        self.zoomOrigAction = self.createAction(self.tr("Zoom &Original"), self.zoomOrig, "win/zoom_orig_128x128.png", self.tr("Original text size in views"))
        self.zoomInAction = self.createAction(self.tr("Zoom &In"), self.zoomIn, QKeySequence.ZoomIn, "win/zoomin.png", self.tr("Larger text size"))
        self.zoomOutAction = self.createAction(self.tr("&Zoom Out"), self.zoomOut, QKeySequence.ZoomOut, "win/zoomout.png", self.tr("Smaller text size"))
        self.tableViewAction = self.createAction(self.tr("&Table"), self.tableView, self.tr("View tables in rows and columns"))
        self.formViewAction = self.createAction(self.tr("&Form"), self.formView, self.tr("View tables in a one row form"))
        self.queryViewAction = self.createAction(self.tr("&Query"), self.viewView, self.tr("View a saved query search"))
        self.searchViewAction = self.createAction(self.tr("Quick &Search"), self.searchView, self.tr("Look for information quickly"))
        self.reportAction = self.createAction(self.tr("&Report"), self.reportView, self.tr("Create a report from tables"))
        self.addActions(viewMenu, (self.zoomOrigAction, self.zoomInAction, self.zoomOutAction, None, self.tableViewAction, self.formViewAction, self.queryViewAction, self.searchViewAction, self.reportAction))
        
        insertMenu = self.menuBar().addMenu(self.tr("&Insert"))
        self.insertTableAction = self.createAction(self.tr("New &Table"), self.newTable, self.tr("Create a new table, or relationships"))
        self.modifyTableAction = self.createAction(self.tr("&Modify Table"), self.modifyTable, self.tr("Change the data fields for a table"))
        # The above action could do with a pencil icon
        self.insertReportAction = self.createAction(self.tr("New &Report"), self.reportNew, self.tr("Create a report"))
        self.insertCharAction = self.createAction(self.tr("Insert &Symbol"), self.insertChar, self.tr("Insert a special character"))
        self.addActions(insertMenu, (self.insertTableAction, self.modifyTableAction, self.insertReportAction, self.insertCharAction))
        
        optionsMenu = self.menuBar().addMenu(self.tr("&Options"))
        self.databaseOptsAction = self.createAction(self.tr("&Database"), self.dbOpts, self.tr("Database settings"))
        self.formOptsAction = self.createAction(self.tr("&Forms"), self.formOpts, self.tr("Change look of forms"))
        self.reportOptsAction = self.createAction(self.tr("&Reports"), self.reportOpts, self.tr("Report settings"))
        self.addActions(optionsMenu, (self.databaseOptsAction, self.formOptsAction, self.reportOptsAction))
        
        helpViewerAction = self.createAction(self.tr("&Handbook"), self.helpViewer, QKeySequence.HelpContents, "win/info_128x128.png", self.tr("View help files"))
        helpAboutAction = self.createAction(self.tr("&About"), self.aboutRecords, "win/records.png", self.tr("About Records"))
        helpMenu = self.menuBar().addMenu(self.tr("&Help"))
        self.addActions(helpMenu, (helpViewerAction, helpAboutAction))
        
        
    def createToolbars(self):
        self.firstRcdAction = self.createAction("", self.gotoFirstRcd, self.tr("Ctrl+1"), "win/firstrecord_128x128.png", self.tr("Go to 1st record in this table"))
        self.prevRcdAction = self.createAction("", self.prevRcd, self.tr("Ctrl+<"), "win/prevrecord_128x128.png", self.tr("Previous Record"))
        self.nextRcdAction = self.createAction("", self.nextRcd, self.tr("Ctrl+>"), "win/nextrecord_128x128.png", self.tr("Next Record"))
        self.lastRcdAction = self.createAction("", self.gotoLastRcd, self.tr("Ctrl+9"), "win/lastrecord_128x128.png", self.tr("Last record in this table"))
        editToolbar = self.addToolBar(self.tr("Edit"))
        editToolbar.setObjectName("editToolbar")
        self.addActions(editToolbar, (self.firstRcdAction, self.prevRcdAction, self.nextRcdAction, self.lastRcdAction))
        
        commonBar = self.addToolBar(self.tr("Common"))
        commonBar.setObjectName("commonBar")
        self.addActions(commonBar, (self.tableViewAction, self.formViewAction, self.queryViewAction, self.searchViewAction, None, self.exportAction, self.modifyTableAction))
        
        

    def createAction(self, text, slot=None, shortcut=None, icon=None, toolt=None, checkable=False, signal="triggered()"):
        """
        Based on a similar function in the PyQt book.

        This function speeds up the creation of QActions, shortcut is the keyboard shortcut, toolt is the tooltip on mouse hover.
        """
        action = QAction(text, self)
        if icon is not None:
            action.setIcon(QIcon(":/images/{}".format(icon)))
        if shortcut is not None:
            action.setShortcut(shortcut)
        if toolt is not None:
            action.setToolTip(toolt)
        if slot is not None:
            self.connect(action, SIGNAL(signal), slot)
        if checkable:
            action.setCheckable(True)
        return action


    def addActions(self, target, actions):
        """
        Add actions (in a tuple) to a QToolBar or QMenu
        """
        for action in actions:
            if action is None:
                target.addSeparator()
            else:
                target.addAction(action)


    def createStatus(self):
        """
        Input: To update, use updateStatus("msg") or updateRowLabel()
        Output: An area for error messages to the left, row number in the right hand corner.
        """
        status = self.statusBar()
        status.setSizeGripEnabled(False)
        self.helpMsg = QLabel()
        self.helpMsg.setMinimumSize(300, 12)
        self.rowLabel = QLabel()
        status.addWidget(self.helpMsg)
        status.addWidget(self.rowLabel)


    def updateRecentFMenu(self):
        """
        Input: a list of recently opened files

        Output: Adds a recent files submenu to the file menu.
        """
        current = self.filename
        recentDbs = []
        for fname in self.recentDbs:
            if fname != current and QFile.exists(fname):
                recentDbs.append(fname)
        if recentDbs:
            for i, fname in enumerate(recentDbs):
                if i < 8:
                     action = QAction("&{}".format(QFileInfo(fname).fileName()), self)
                     action.setData(fname)
                     self.connect(action, SIGNAL("triggered()"), self.opendb)
                     self.recentMenu.addAction(action)
        
    def gotoFirstRcd(self):
        pass

    def gotoLastRcd(self):
        pass

    def prevRcd(self):
        pass

    def nextRcd(self):
        pass

    # Functions from the file menu, needs fileio import.
    
    
    def newdb(self):
        """
        Input: the database filename and the file path to save it to.

        Output: An empty database file at the chosen path.
        """
        from ui.dialogs import new_db
        dialog = new_db.NewdbDialog()
        if dialog.exec_() == QDialog.Accepted:
            filename = dialog.validateStuff()
            self.opendb(filename)

    
    def opendb(self, filename=None):
        """
        Input: A database sqlite filename
        Output: The first database table in table view
        """
        if filename is None:
            filename = QFileDialog.getOpenFileName(self, self.tr("Records - Open a Database"))
        self.dbase.setDatabaseName(filename)
        if self.dbase.open():
            self.dbname = self.dbase.databaseName()
            settings.dbname = self.dbname   # set up the file variable for other functions
            self.filename = filename
            # this needs to go in create/edit table dialog
            self.tableView()
        else:
            print("Wrong URI")
            #if not sqlite mimetype (magic num)
            # Give wrong type of file warning.

    
    def savedb(self):
        """
        Saves any row or other changes to the SQL file.
        """
        self.model.submitAll()
        # QSqlDatabase.database().commit()
        
    
    def saveas(self):
        """
        Saves the database SQLite file to a different name.
        """
        if self.filename:
            self.savedb()
            newfilename = QFileDialog.getSaveFileName(self, self.tr("Records - Save As"))
            if newfilename:
                
                for tab in range(self.tabArea.count()):
                    # close any previous tabs
                    self.tabArea.removeTab(tab)
                    self.tabArea.setCurrentIndex(tab)
                    curPage = self.tabArea.currentWidget()
                    del curPage
                self.dbase.close()
                shutil.copy2(self.filename, newfilename) 
                self.opendb(newfilename)
                
    
    def importdb(self):
        """
        Imports CSV files to a table
        The user also has to provide the table name and delimiter.
        """
        pass
    
    
    def exportdb(self):
        """
        Saves a selected table to CSV format, with a choice of delimiters.
        """
        import sql.select
        import reports.export_csv
        if self.dbase:
            printout = sql.select.select_query(settings.tablename)
            if printout:
                if reports.export_csv.export_csv(settings.tablename, printout):
                    QMessageBox.information(self, self.tr("Export CSV - Success"), self.tr("The CSV file was created in the same folder as the current database file. "), QMessageBox.Close)
   
    

    def closeEvent(self, event):
        """
        Closes the entire application
        """
        settings = QSettings()
        settings.setValue("MainWindow/Geometry", self.saveGeometry())
        settings.setValue("MainWindow/State", self.saveState())
        self.viewsOpen = []
        # Close all open tabs
        
    
    def closeTab(self, currentIndex):
        curPageWidget = self.tabArea.widget(currentIndex)
        curPageWidget.deleteLater()
        self.tabArea.removeTab(currentIndex)

    
    # Functions from the edit menu

    def cutdata(self):
        """
        Move data to clipboard when entering data in table or form view.
        """
        pass
    
    
    def copydata(self):
        """
        Copy data to clipboard, table or form view.
        """
        pass
    
    
    def pastedata(self):
        """
        Paste data from clipboard, table or form view.
        """
        pass
    
    
    def deldata(self):
        """
        Deletes all data in the selected field.
        """
        pass
    
    
    
    
    # Functions from the view menu
    def zoomOrig(self):
        """
        Zoom is for table views, queries and report tabs.
        """
        pass
    
    
    def zoomIn(self):
        pass
    
    
    def zoomOut(self):
        pass
    
    
    def tableView(self):
        """
        Initialises a tab with a table view widget inside of it.

        Create a QAbstractTableModel with delegate parts for 
        enumerated lists and boolean values later on.
        """
        tablesAvail = []
        self.query = QSqlQuery(self.dbase)    
        self.query.exec_("SELECT name FROM sqlite_master WHERE type='table'") 
        while self.query.next():
            tablename = self.query.record()
            tablesAvail.append(tablename.value(0))
        QApplication.processEvents()
        self.model = QSqlRelationalTableModel()
        self.tableListBox = QListWidget()
        self.tableListBox.setMaximumWidth(200)
        self.tableview = QTableView() # or custom table class
        self.insertWidget = ui.widgets.insertTableView.InsertWidget()
        self.insertWidget.setMaximumHeight(40)
        self.insertWidget.showDlg()
        self.connect(self.insertWidget.addRow, SIGNAL("clicked()"), self.insertRefresh)
        tableLayout = QHBoxLayout()
        tableViewPage = QWidget()
        updateTableBtn = QPushButton(self.tr("Show &Table"))
        delButton = QPushButton(self.tr("Delete Row"))
        rightLayout = QVBoxLayout()
        rightLayout.addWidget(self.tableListBox)
        rightLayout.addWidget(updateTableBtn)
        rightLayout.addWidget(self.insertWidget)
        rightLayout.addWidget(delButton)
        tableLayout.addWidget(self.tableview, 3)
        tableLayout.addLayout(rightLayout, 1)
        self.connect(updateTableBtn, SIGNAL("clicked()"), self.updateTable)  
        self.connect(delButton, SIGNAL("clicked()"), self.deleteRecord)

        self.tableListBox.addItems(tablesAvail)
        if settings.tablename == "": 
            settings.tablename = str(tablesAvail[0])
        self.model.setTable(settings.tablename) # create updateTable function, find cur index in listbox
        self.tableview.setModel(self.model)
        self.model.select() 
        self.tableview.setSelectionMode(QTableView.SingleSelection)
        self.tableview.resizeColumnsToContents()
        self.tableview.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        horizHeadings = self.tableview.horizontalHeader()      
        rowHeadings = self.tableview.verticalHeader()
        
        tableDescr, self.colNum = self.tableInfo(settings.tablename)  # goes in form view
        tableViewPage.setLayout(tableLayout)
        tableViewPage.setFocus()
        QApplication.processEvents()       

        self.tabArea.addTab(tableViewPage, self.tr("{} Table".format(settings.tablename)))
        self.tabArea.setCurrentWidget(tableViewPage)
         
        self.tableViewRefresh() 
    
   
    def tableViewRefresh(self):
        select = "SELECT * FROM " + settings.tablename
        if self.query.exec_(select): 
            rowString = ""
            while self.query.next():
                while self.colNum > 0:
                    row = self.query.record()
                    rowString += row.value(self.colNum)
        
         
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
        """
        Updates the tablename variable in settings, on button press "Show Table".
        """
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


    def formView(self):
        """
        A tab with a form view object instance in it.
        """
        pass
    
    
    def viewView(self):
        """
        For saved query views - in table view.
        """
        from ui.widgets import tableView
        from ui.dialogs import query_view_dlg
        dialog = query_view_dlg.QueryViewDlg()
        if dialog.exec_() == QDialog.Accepted:
            resultView = dialog.fetchData()
            tableForView = tableView.TableWidget(resultView, settings.tablename)
            self.tabArea.addTab(tableForView, self.tr("Query"))
            self.tabArea.setCurrentWidget(tableForView)
        else:
            print("Query view form exec failed ")
    
    
    def searchView(self):
        """
        A simple text or number based query - the query isn't saved
        """
        from ui.widgets import tableView
        from ui.dialogs import search_text
        dialog = search_text.SearchDlg()
        if dialog.exec_() == QDialog.Accepted:
            resultSet = dialog.fetchData()
            tableForQuery = tableView.TableWidget(resultSet, settings.tablename)
            self.tabArea.addTab(tableForQuery, self.tr("Search"))
            self.tabArea.setCurrentWidget(tableForQuery)
        else:
            print("Search widget failed")
    

    def reportNew(self):
        import sql.utils
        utils = sql.utils.SQLutils()
        fieldList = utils.get_fieldnames(settings.tablename)
        import ui.dialogs.reports_new
        dialog = ui.dialogs.reports_new.NewReportDialog(fieldList)
        if dialog.exec_() == QDialog.Accepted:
            report = dialog.fetchData()
            #print(report)
            self.reportView(report)
    

    def reportView(self, reportname):
        """
        A tab with report creation options in it.
        """
        import ui.tab_pages.reports_tab
        reportsPage = ui.tab_pages.reports_tab.ReportsTab()
        #print(reportname)
        reportsPage.displayUrl(reportname)
        self.tabArea.addTab(reportsPage, self.tr("Report"))
        self.tabArea.setCurrentWidget(reportsPage)
 
    
    def deleteRecord(self):
        """
        For the table View tabs.
        """
        index = self.tableview.currentIndex()
        if not index.isValid():
            print("index is False in delete Record")
            return False
        record = self.model.record(index.row())
        # Check ids aren't linked to foreign tables.
        self.model.removeRow(index.row())
        self.model.submitAll()

    
    
    # Functions from the Insert menu
    def newTable(self):
        """
        Calls the ui.dialogs.create_edit_table.py dialog,
        which sets up field names and extra validation outside
        of SQL constraints.
        """
        settings.table = ""
        import ui.dialogs.create_edit_table
        createTable = ui.dialogs.create_edit_table.CreateTableDialog() 
        if createTable.exec_() == QDialog.Accepted:
            print("Showing create table")
            createTable.dialogAccepted() # fires off the relevent SQL
        else:
            print("Create table boo boo in records.pyw")        
        self.tableView()    
    

    def modifyTable(self):
        """
        Input: the current table's fields and types.
        Output: Any changes are made to the table
        """
        pass
    
    
    def insertChar(self):
        """
        Inserts special characters like yen, or Euro symbols. Does SQLite3 support UTF-8?
        """
        pass
    

    # Functions from the Options menu
    def dbOpts(self):
        """
        Options for changing database server - or using SQLite again.
        """
        pass
    
    
    def formOpts(self):
        """
        Form related display settings
        """
        pass
    
    
    def reportOpts(self):
        """
        Change whether reports use XHTML or HTML5
        """
        pass
    
        
    # Functions from the help menu
    def helpViewer(self):
        """
        Displays help pages in HTML, from the docs directory.
        """
        pass
    
    
    def aboutRecords(self):
        QMessageBox.about(self, "About Records", 
        """
        <h2>Records</h2> version {}
        <p>Create, modify and update databases simply using Records. This program saves to SQLite database files, which can be used 
        on a variety of platforms. You can also create reports in web page format, for easy distribution. </p>
        <p>&copy; 2014 Copyright Hazel Windle, with some ideas taken from various computer books and online sources. <br />
        This software is licensed under the GNU GPL version 2. Please see the LICENSE file included with this program for the full details, or visit
        <a href='http://www.gnu.org/licenses/old-licenses/gpl-2.0.html'>the Free Software Foundation</a> for more information.
        </p>
        <hr />
        <p>Python version: {} Qt {} running on: {}</p>"""\
        .format(__version__, platform.python_version(), QT_VERSION_STR, platform.system()))
    
    
def main():
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon(":/images/win/records.png"))
    app.setOrganizationName("Paradise Office")
    app.setOrganizationDomain("linux-paradise.co.uk")
    app.setApplicationName("Records")
    win = MainWindow()
    win.resize(1024, 768)
    win.show()
    app.exec_()

main()
