# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'comparison_adder.ui'
#
# Created: Tue Mar 24 16:12:53 2015
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
        Dialog.resize(420, 251)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("../../images/win/records.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Dialog.setWindowIcon(icon)
        self.widget = QtGui.QWidget(Dialog)
        self.widget.setGeometry(QtCore.QRect(10, 10, 401, 231))
        self.widget.setObjectName(_fromUtf8("widget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.widget)
        self.verticalLayout.setMargin(0)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.tableLabel = QtGui.QLabel(self.widget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tableLabel.sizePolicy().hasHeightForWidth())
        self.tableLabel.setSizePolicy(sizePolicy)
        self.tableLabel.setMinimumSize(QtCore.QSize(40, 0))
        self.tableLabel.setObjectName(_fromUtf8("tableLabel"))
        self.horizontalLayout_2.addWidget(self.tableLabel)
        self.tableCombo = QtGui.QComboBox(self.widget)
        self.tableCombo.setObjectName(_fromUtf8("tableCombo"))
        self.horizontalLayout_2.addWidget(self.tableCombo)
        self.fieldLabel = QtGui.QLabel(self.widget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.fieldLabel.sizePolicy().hasHeightForWidth())
        self.fieldLabel.setSizePolicy(sizePolicy)
        self.fieldLabel.setMinimumSize(QtCore.QSize(40, 0))
        self.fieldLabel.setObjectName(_fromUtf8("fieldLabel"))
        self.horizontalLayout_2.addWidget(self.fieldLabel)
        self.fieldCombo = QtGui.QComboBox(self.widget)
        self.fieldCombo.setObjectName(_fromUtf8("fieldCombo"))
        self.horizontalLayout_2.addWidget(self.fieldCombo)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.andButton = QtGui.QRadioButton(self.widget)
        self.andButton.setObjectName(_fromUtf8("andButton"))
        self.horizontalLayout.addWidget(self.andButton)
        self.orButton = QtGui.QRadioButton(self.widget)
        self.orButton.setObjectName(_fromUtf8("orButton"))
        self.horizontalLayout.addWidget(self.orButton)
        self.verticalLayout.addLayout(self.horizontalLayout)
        spacerItem = QtGui.QSpacerItem(20, 18, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.comparelabel = QtGui.QLabel(self.widget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comparelabel.sizePolicy().hasHeightForWidth())
        self.comparelabel.setSizePolicy(sizePolicy)
        self.comparelabel.setMinimumSize(QtCore.QSize(120, 0))
        self.comparelabel.setObjectName(_fromUtf8("comparelabel"))
        self.horizontalLayout_3.addWidget(self.comparelabel)
        self.compareCombo = QtGui.QComboBox(self.widget)
        self.compareCombo.setObjectName(_fromUtf8("compareCombo"))
        self.horizontalLayout_3.addWidget(self.compareCombo)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.valueLabel = QtGui.QLabel(self.widget)
        self.valueLabel.setMinimumSize(QtCore.QSize(120, 0))
        self.valueLabel.setObjectName(_fromUtf8("valueLabel"))
        self.horizontalLayout_4.addWidget(self.valueLabel)
        self.valueLineEdit = QtGui.QLineEdit(self.widget)
        self.valueLineEdit.setObjectName(_fromUtf8("valueLineEdit"))
        self.horizontalLayout_4.addWidget(self.valueLineEdit)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.buttonBox = QtGui.QDialogButtonBox(self.widget)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.verticalLayout.addWidget(self.buttonBox)
        self.tableLabel.setBuddy(self.tableCombo)
        self.fieldLabel.setBuddy(self.fieldCombo)
        self.comparelabel.setBuddy(self.compareCombo)
        self.valueLabel.setBuddy(self.valueLineEdit)

        self.retranslateUi(Dialog)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), Dialog.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        Dialog.setTabOrder(self.tableCombo, self.fieldCombo)
        Dialog.setTabOrder(self.fieldCombo, self.andButton)
        Dialog.setTabOrder(self.andButton, self.orButton)
        Dialog.setTabOrder(self.orButton, self.compareCombo)
        Dialog.setTabOrder(self.compareCombo, self.valueLineEdit)
        Dialog.setTabOrder(self.valueLineEdit, self.buttonBox)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Add A Comparison", None))
        self.tableLabel.setText(_translate("Dialog", "&Table:", None))
        self.fieldLabel.setText(_translate("Dialog", "&Field:", None))
        self.andButton.setText(_translate("Dialog", "&And (less results)", None))
        self.orButton.setText(_translate("Dialog", "&Or (more results)", None))
        self.comparelabel.setText(_translate("Dialog", "Compare &By:", None))
        self.valueLabel.setText(_translate("Dialog", "&Value:", None))

