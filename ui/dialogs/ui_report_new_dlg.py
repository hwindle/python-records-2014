# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'new_report_dialog.ui'
#
# Created: Fri Feb 27 10:36:05 2015
#      by: PyQt4 UI code generator 4.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(760, 600)
        self.buttonBox = QtGui.QDialogButtonBox(Dialog)
        self.buttonBox.setGeometry(QtCore.QRect(400, 560, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.tabWidget = QtGui.QTabWidget(Dialog)
        self.tabWidget.setGeometry(QtCore.QRect(10, 10, 741, 541))
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.dataTab = QtGui.QWidget()
        self.dataTab.setObjectName(_fromUtf8("dataTab"))
        self.fieldsGroup = QtGui.QGroupBox(self.dataTab)
        self.fieldsGroup.setGeometry(QtCore.QRect(10, 170, 351, 331))
        self.fieldsGroup.setObjectName(_fromUtf8("fieldsGroup"))
        self.fieldsListBox = QtGui.QScrollArea(self.fieldsGroup)
        self.fieldsListBox.setGeometry(QtCore.QRect(9, 20, 331, 301))
        self.fieldsListBox.setMinimumSize(QtCore.QSize(300, 300))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.fieldsListBox.setFont(font)
        self.fieldsListBox.setLineWidth(0)
        self.fieldsListBox.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.fieldsListBox.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.fieldsListBox.setWidgetResizable(False)
        self.fieldsListBox.setObjectName(_fromUtf8("fieldsListBox"))
        self.scrollAreaWidgetContents = QtGui.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 327, 297))
        self.scrollAreaWidgetContents.setObjectName(_fromUtf8("scrollAreaWidgetContents"))
        self.fieldsListBox.setWidget(self.scrollAreaWidgetContents)
        self.sortGroup = QtGui.QGroupBox(self.dataTab)
        self.sortGroup.setGeometry(QtCore.QRect(360, 170, 351, 331))
        self.sortGroup.setObjectName(_fromUtf8("sortGroup"))
        self.layoutWidget = QtGui.QWidget(self.sortGroup)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 20, 331, 301))
        self.layoutWidget.setObjectName(_fromUtf8("layoutWidget"))
        self.gridLayout_2 = QtGui.QGridLayout(self.layoutWidget)
        self.gridLayout_2.setMargin(0)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.sortFieldLabel = QtGui.QLabel(self.layoutWidget)
        self.sortFieldLabel.setObjectName(_fromUtf8("sortFieldLabel"))
        self.horizontalLayout_4.addWidget(self.sortFieldLabel)
        self.sortFieldCombo = QtGui.QComboBox(self.layoutWidget)
        self.sortFieldCombo.setMinimumSize(QtCore.QSize(200, 0))
        self.sortFieldCombo.setObjectName(_fromUtf8("sortFieldCombo"))
        self.horizontalLayout_4.addWidget(self.sortFieldCombo)
        self.gridLayout_2.addLayout(self.horizontalLayout_4, 0, 0, 1, 1)
        spacerItem = QtGui.QSpacerItem(10, 20, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        self.gridLayout_2.addItem(spacerItem, 1, 0, 1, 1)
        self.sortdirGroup = QtGui.QGroupBox(self.layoutWidget)
        self.sortdirGroup.setFlat(True)
        self.sortdirGroup.setObjectName(_fromUtf8("sortdirGroup"))
        self.layoutWidget1 = QtGui.QWidget(self.sortdirGroup)
        self.layoutWidget1.setGeometry(QtCore.QRect(20, 20, 271, 111))
        self.layoutWidget1.setObjectName(_fromUtf8("layoutWidget1"))
        self.verticalLayout = QtGui.QVBoxLayout(self.layoutWidget1)
        self.verticalLayout.setMargin(0)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.ascRadioBtn = QtGui.QRadioButton(self.layoutWidget1)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.ascRadioBtn.setFont(font)
        self.ascRadioBtn.setObjectName(_fromUtf8("ascRadioBtn"))
        self.verticalLayout.addWidget(self.ascRadioBtn)
        self.descRadioBtn = QtGui.QRadioButton(self.layoutWidget1)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.descRadioBtn.setFont(font)
        self.descRadioBtn.setObjectName(_fromUtf8("descRadioBtn"))
        self.verticalLayout.addWidget(self.descRadioBtn)
        self.gridLayout_2.addWidget(self.sortdirGroup, 2, 0, 1, 1)
        self.layoutWidget2 = QtGui.QWidget(self.dataTab)
        self.layoutWidget2.setGeometry(QtCore.QRect(10, 10, 711, 111))
        self.layoutWidget2.setObjectName(_fromUtf8("layoutWidget2"))
        self.gridLayout = QtGui.QGridLayout(self.layoutWidget2)
        self.gridLayout.setMargin(0)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.titleLabel = QtGui.QLabel(self.layoutWidget2)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.titleLabel.setFont(font)
        self.titleLabel.setObjectName(_fromUtf8("titleLabel"))
        self.horizontalLayout_3.addWidget(self.titleLabel)
        self.titleLineEdit = QtGui.QLineEdit(self.layoutWidget2)
        self.titleLineEdit.setMinimumSize(QtCore.QSize(200, 0))
        self.titleLineEdit.setMaxLength(40)
        self.titleLineEdit.setObjectName(_fromUtf8("titleLineEdit"))
        self.horizontalLayout_3.addWidget(self.titleLineEdit)
        self.gridLayout.addLayout(self.horizontalLayout_3, 0, 0, 2, 1)
        spacerItem1 = QtGui.QSpacerItem(100, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 0, 1, 2, 2)
        spacerItem2 = QtGui.QSpacerItem(300, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem2, 0, 3, 2, 1)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.tableLabel = QtGui.QLabel(self.layoutWidget2)
        self.tableLabel.setObjectName(_fromUtf8("tableLabel"))
        self.horizontalLayout_2.addWidget(self.tableLabel)
        self.tableCombo = QtGui.QComboBox(self.layoutWidget2)
        self.tableCombo.setMinimumSize(QtCore.QSize(200, 0))
        self.tableCombo.setMaxVisibleItems(30)
        self.tableCombo.setObjectName(_fromUtf8("tableCombo"))
        self.horizontalLayout_2.addWidget(self.tableCombo)
        self.gridLayout.addLayout(self.horizontalLayout_2, 2, 0, 1, 1)
        spacerItem3 = QtGui.QSpacerItem(100, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem3, 2, 1, 1, 2)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.viewLabel = QtGui.QLabel(self.layoutWidget2)
        self.viewLabel.setObjectName(_fromUtf8("viewLabel"))
        self.horizontalLayout.addWidget(self.viewLabel)
        self.viewCombo = QtGui.QComboBox(self.layoutWidget2)
        self.viewCombo.setMinimumSize(QtCore.QSize(200, 0))
        self.viewCombo.setMaxVisibleItems(30)
        self.viewCombo.setObjectName(_fromUtf8("viewCombo"))
        self.horizontalLayout.addWidget(self.viewCombo)
        self.gridLayout.addLayout(self.horizontalLayout, 2, 3, 1, 1)
        self.layoutWidget3 = QtGui.QWidget(self.dataTab)
        self.layoutWidget3.setGeometry(QtCore.QRect(20, 140, 701, 31))
        self.layoutWidget3.setObjectName(_fromUtf8("layoutWidget3"))
        self.horizontalLayout_5 = QtGui.QHBoxLayout(self.layoutWidget3)
        self.horizontalLayout_5.setMargin(0)
        self.horizontalLayout_5.setObjectName(_fromUtf8("horizontalLayout_5"))
        self.saveLabel = QtGui.QLabel(self.layoutWidget3)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.saveLabel.setFont(font)
        self.saveLabel.setObjectName(_fromUtf8("saveLabel"))
        self.horizontalLayout_5.addWidget(self.saveLabel)
        self.pathLineEdit = QtGui.QLineEdit(self.layoutWidget3)
        self.pathLineEdit.setObjectName(_fromUtf8("pathLineEdit"))
        self.horizontalLayout_5.addWidget(self.pathLineEdit)
        self.browseBtn = QtGui.QPushButton(self.layoutWidget3)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.browseBtn.setFont(font)
        self.browseBtn.setObjectName(_fromUtf8("browseBtn"))
        self.horizontalLayout_5.addWidget(self.browseBtn)
        self.tabWidget.addTab(self.dataTab, _fromUtf8(""))
        self.themeTab = QtGui.QWidget()
        self.themeTab.setObjectName(_fromUtf8("themeTab"))
        self.themesLabel = QtGui.QLabel(self.themeTab)
        self.themesLabel.setGeometry(QtCore.QRect(20, 10, 631, 21))
        self.themesLabel.setObjectName(_fromUtf8("themesLabel"))
        self.themesListWidget = QtGui.QListWidget(self.themeTab)
        self.themesListWidget.setGeometry(QtCore.QRect(10, 30, 721, 481))
        self.themesListWidget.setMinimumSize(QtCore.QSize(600, 400))
        self.themesListWidget.setFrameShape(QtGui.QFrame.NoFrame)
        self.themesListWidget.setFrameShadow(QtGui.QFrame.Sunken)
        self.themesListWidget.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.themesListWidget.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.themesListWidget.setEditTriggers(QtGui.QAbstractItemView.DoubleClicked|QtGui.QAbstractItemView.EditKeyPressed|QtGui.QAbstractItemView.SelectedClicked)
        self.themesListWidget.setTabKeyNavigation(False)
        self.themesListWidget.setIconSize(QtCore.QSize(650, 350))
        self.themesListWidget.setResizeMode(QtGui.QListView.Adjust)
        self.themesListWidget.setGridSize(QtCore.QSize(650, 350))
        self.themesListWidget.setViewMode(QtGui.QListView.IconMode)
        self.themesListWidget.setUniformItemSizes(False)
        self.themesListWidget.setObjectName(_fromUtf8("themesListWidget"))
        item = QtGui.QListWidgetItem()
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/images/01_grey_brown.png")), QtGui.QIcon.Selected, QtGui.QIcon.Off)
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/images/01_grey_brown.png")), QtGui.QIcon.Normal, QtGui.QIcon.On)
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/images/01_grey_brown.png")), QtGui.QIcon.Selected, QtGui.QIcon.On)
        item.setIcon(icon)
        self.themesListWidget.addItem(item)
        item = QtGui.QListWidgetItem()
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8(":/images/02_large_bw.png")), QtGui.QIcon.Selected, QtGui.QIcon.Off)
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8(":/images/02_large_bw.png")), QtGui.QIcon.Normal, QtGui.QIcon.On)
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8(":/images/02_large_bw.png")), QtGui.QIcon.Selected, QtGui.QIcon.On)
        item.setIcon(icon1)
        self.themesListWidget.addItem(item)
        item = QtGui.QListWidgetItem()
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(_fromUtf8(":/images/03_navy_steel_blue.png")), QtGui.QIcon.Selected, QtGui.QIcon.Off)
        icon2.addPixmap(QtGui.QPixmap(_fromUtf8(":/images/03_navy_steel_blue.png")), QtGui.QIcon.Normal, QtGui.QIcon.On)
        icon2.addPixmap(QtGui.QPixmap(_fromUtf8(":/images/03_navy_steel_blue.png")), QtGui.QIcon.Selected, QtGui.QIcon.On)
        item.setIcon(icon2)
        self.themesListWidget.addItem(item)
        item = QtGui.QListWidgetItem()
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(_fromUtf8(":/images/04_sans_blue.png")), QtGui.QIcon.Selected, QtGui.QIcon.Off)
        icon3.addPixmap(QtGui.QPixmap(_fromUtf8(":/images/04_sans_blue.png")), QtGui.QIcon.Normal, QtGui.QIcon.On)
        icon3.addPixmap(QtGui.QPixmap(_fromUtf8(":/images/04_sans_blue.png")), QtGui.QIcon.Selected, QtGui.QIcon.On)
        item.setIcon(icon3)
        self.themesListWidget.addItem(item)
        item = QtGui.QListWidgetItem()
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(_fromUtf8(":/images/05_warm_yellows.png")), QtGui.QIcon.Selected, QtGui.QIcon.Off)
        icon4.addPixmap(QtGui.QPixmap(_fromUtf8(":/images/05_warm_yellows.png")), QtGui.QIcon.Normal, QtGui.QIcon.On)
        icon4.addPixmap(QtGui.QPixmap(_fromUtf8(":/images/05_warm_yellows.png")), QtGui.QIcon.Selected, QtGui.QIcon.On)
        item.setIcon(icon4)
        self.themesListWidget.addItem(item)
        self.tabWidget.addTab(self.themeTab, _fromUtf8(""))
        self.sortFieldLabel.setBuddy(self.sortFieldCombo)
        self.titleLabel.setBuddy(self.titleLineEdit)
        self.tableLabel.setBuddy(self.tableCombo)
        self.viewLabel.setBuddy(self.viewCombo)
        self.themesLabel.setBuddy(self.themesListWidget)

        self.retranslateUi(Dialog)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), Dialog.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), Dialog.reject)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), Dialog.accept)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        Dialog.setTabOrder(self.titleLineEdit, self.tableCombo)
        Dialog.setTabOrder(self.tableCombo, self.viewCombo)
        Dialog.setTabOrder(self.viewCombo, self.sortFieldCombo)
        Dialog.setTabOrder(self.sortFieldCombo, self.ascRadioBtn)
        Dialog.setTabOrder(self.ascRadioBtn, self.descRadioBtn)
        Dialog.setTabOrder(self.descRadioBtn, self.buttonBox)
        Dialog.setTabOrder(self.buttonBox, self.tabWidget)
        Dialog.setTabOrder(self.tabWidget, self.themesListWidget)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Dialog", None))
        self.fieldsGroup.setTitle(_translate("Dialog", "Fields", None))
        self.sortGroup.setTitle(_translate("Dialog", "Sort By", None))
        self.sortFieldLabel.setText(_translate("Dialog", "Field:", None))
        self.sortdirGroup.setTitle(_translate("Dialog", "Di&rection", None))
        self.ascRadioBtn.setText(_translate("Dialog", "Ascending (A-Z)", None))
        self.descRadioBtn.setText(_translate("Dialog", "Descending (Z-A)", None))
        self.titleLabel.setText(_translate("Dialog", "Title", None))
        self.tableLabel.setText(_translate("Dialog", "Table", None))
        self.viewLabel.setText(_translate("Dialog", "View", None))
        self.saveLabel.setText(_translate("Dialog", "Save in folder:", None))
        self.browseBtn.setText(_translate("Dialog", "&Browse", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.dataTab), _translate("Dialog", "&Data", None))
        self.themesLabel.setText(_translate("Dialog", "Please select a colour scheme for your report:", None))
        __sortingEnabled = self.themesListWidget.isSortingEnabled()
        self.themesListWidget.setSortingEnabled(False)
        item = self.themesListWidget.item(0)
        item.setText(_translate("Dialog", "grey brown", None))
        item.setToolTip(_translate("Dialog", "grey brown", None))
        item = self.themesListWidget.item(1)
        item.setText(_translate("Dialog", "large black & white", None))
        item = self.themesListWidget.item(2)
        item.setText(_translate("Dialog", "navy steel blue", None))
        item = self.themesListWidget.item(3)
        item.setText(_translate("Dialog", "sans blue", None))
        item = self.themesListWidget.item(4)
        item.setText(_translate("Dialog", "warm yellows", None))
        self.themesListWidget.setSortingEnabled(__sortingEnabled)
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.themeTab), _translate("Dialog", "&Themes", None))

from ui.dialogs import dialog_rc