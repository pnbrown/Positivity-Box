# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Designer Gui.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(754, 851)
        Dialog.setStyleSheet("background-image: url(:/kanye_holding2.jpg)")
        self.textBrowser = QtWidgets.QTextBrowser(Dialog)
        self.textBrowser.setGeometry(QtCore.QRect(130, 180, 491, 201))
        self.textBrowser.setObjectName("textBrowser")
        self.NewQuote = QtWidgets.QPushButton(Dialog)
        self.NewQuote.setGeometry(QtCore.QRect(630, 180, 113, 32))
        self.NewQuote.setObjectName("NewQuote")
        self.Exit = QtWidgets.QPushButton(Dialog)
        self.Exit.setGeometry(QtCore.QRect(630, 220, 113, 32))
        self.Exit.setObjectName("Exit")
        self.actionNext_Quote = QtWidgets.QAction(Dialog)
        self.actionNext_Quote.setObjectName("actionNext_Quote")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.NewQuote.setText(_translate("Dialog", "New Quote"))
        self.Exit.setText(_translate("Dialog", "Exit"))
        self.Exit.setShortcut(_translate("Dialog", "Ctrl+W"))
        self.actionNext_Quote.setText(_translate("Dialog", "Next Quote"))
        self.actionNext_Quote.setToolTip(_translate("Dialog", "Push here to see the next quote"))
        self.actionNext_Quote.setShortcut(_translate("Dialog", "Ctrl+Right"))

import resources_rc
