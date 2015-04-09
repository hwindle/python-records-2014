# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'new_db.ui'
#
# Created: Fri Dec  5 21:40:38 2014
#      by: PyQt4 UI code generator 4.10.4
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
        Dialog.resize(381, 274)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/images/win/records.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Dialog.setWindowIcon(icon)
        self.buttonBox = QtGui.QDialogButtonBox(Dialog)
        self.buttonBox.setGeometry(QtCore.QRect(30, 240, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.layoutWidget = QtGui.QWidget(Dialog)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 10, 366, 191))
        self.layoutWidget.setObjectName(_fromUtf8("layoutWidget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setMargin(0)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.helpLabel = QtGui.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.helpLabel.setFont(font)
        self.helpLabel.setWordWrap(True)
        self.helpLabel.setObjectName(_fromUtf8("helpLabel"))
        self.verticalLayout.addWidget(self.helpLabel)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.fileLabel = QtGui.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.fileLabel.setFont(font)
        self.fileLabel.setObjectName(_fromUtf8("fileLabel"))
        self.horizontalLayout_2.addWidget(self.fileLabel)
        self.filenameLineEdit = QtGui.QLineEdit(self.layoutWidget)
        self.filenameLineEdit.setMinimumSize(QtCore.QSize(200, 0))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.filenameLineEdit.setFont(font)
        self.filenameLineEdit.setObjectName(_fromUtf8("filenameLineEdit"))
        self.horizontalLayout_2.addWidget(self.filenameLineEdit)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.pathLabel = QtGui.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.pathLabel.setFont(font)
        self.pathLabel.setObjectName(_fromUtf8("pathLabel"))
        self.horizontalLayout.addWidget(self.pathLabel)
        self.pathLineEdit = QtGui.QLineEdit(self.layoutWidget)
        self.pathLineEdit.setMinimumSize(QtCore.QSize(300, 0))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.pathLineEdit.setFont(font)
        self.pathLineEdit.setObjectName(_fromUtf8("pathLineEdit"))
        self.horizontalLayout.addWidget(self.pathLineEdit)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem)
        self.browseBtn = QtGui.QPushButton(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.browseBtn.setFont(font)
        self.browseBtn.setObjectName(_fromUtf8("browseBtn"))
        self.horizontalLayout_3.addWidget(self.browseBtn)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.fileLabel.setBuddy(self.filenameLineEdit)
        self.pathLabel.setBuddy(self.pathLineEdit)

        self.retranslateUi(Dialog)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), Dialog.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        Dialog.setTabOrder(self.filenameLineEdit, self.pathLineEdit)
        Dialog.setTabOrder(self.pathLineEdit, self.browseBtn)
        Dialog.setTabOrder(self.browseBtn, self.buttonBox)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Records - New Database", None))
        self.helpLabel.setText(_translate("Dialog", "This sets up a new database file ending in .sqlite, in the selected folder. The database is saved there.", None))
        self.fileLabel.setText(_translate("Dialog", "Database Name", None))
        self.pathLabel.setText(_translate("Dialog", "Save In", None))
        self.browseBtn.setText(_translate("Dialog", "&Browse", None))

#import records_rc
