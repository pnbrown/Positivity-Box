# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Designer Gui.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import pyqtSignal, QObject, pyqtSlot
import functions as pb
import sys

class Ui_Dialog(object):
    def setupUi(self, PositivityBox):
        PositivityBox.setObjectName("PositivityBox")
        PositivityBox.resize(754, 851)
        font = QtGui.QFont()
        font.setFamily("Futura")
        font.setPointSize(36)
        PositivityBox.setFont(font)
        PositivityBox.setStyleSheet("background-image: url(:/kanye_holding2.jpg)")
        self.textBrowser = QtWidgets.QTextBrowser(PositivityBox)
        self.textBrowser.setGeometry(QtCore.QRect(130, 170, 491, 261))
        font = QtGui.QFont()
        font.setFamily("Futura")
        font.setPointSize(34)
        self.textBrowser.setFont(font)
        self.textBrowser.setTextInteractionFlags(QtCore.Qt.TextSelectableByMouse)
        self.textBrowser.setObjectName("textBrowser")
        self.NewQuote = QtWidgets.QPushButton(PositivityBox)
        self.NewQuote.setGeometry(QtCore.QRect(630, 180, 113, 32))
        self.NewQuote.setObjectName("NewQuote")
        self.NewQuote.setToolTip('Press here to get the next quote. ')
        self.Exit = QtWidgets.QPushButton(PositivityBox)
        self.Exit.setGeometry(QtCore.QRect(630, 220, 113, 32))
        self.Exit.setObjectName("Exit")
        self.actionNext_Quote = QtWidgets.QAction(PositivityBox)
        self.actionNext_Quote.setObjectName("actionNext_Quote")
        self.retranslateUi(PositivityBox)
        QtCore.QMetaObject.connectSlotsByName(PositivityBox)
        global quotes_entry
        quotes_entry = 0
        global quotes_gathered_bool
        quotes_gathered_bool = False
        global quotes
        quotes = []
        global function_call_values
        function_call_values = [quotes_gathered_bool, quotes_entry, quotes]
        self.NewQuote.clicked.connect(lambda: self.newQuotePushed(function_call_values[0], function_call_values[1], function_call_values[2]))
        self.Exit.clicked.connect(sys.exit)

    @pyqtSlot()
    def newQuotePushed(self, get_quotes, quotes_num, quotes):
        # print(get_quotes)
        if not get_quotes:
            global quotes_list
            quotes_list = self.setQuotes()
            print("Gathered quotes")
            print(quotes_list)
            global gathered_bool
            gathered_bool = True
            get_quotes = gathered_bool
        if quotes_num == (len(quotes_list)):
            self.textBrowser.setText("There are no quotes left to return. Please push Exit.")
            return
        else:
            data = pb.print_quote(quotes_list, quotes_num)
            text = data[0]
            print(text)
            global quotes_entry
            quotes_entry = data[1]
            self.textBrowser.setText(text)
            global function_call_values
            function_call_values = [get_quotes, quotes_entry, quotes_list]

    def setQuotes(self):
        global quotes_list
        quotes_list = pb.program_run()
        print(quotes_list)
        return quotes_list


    def retranslateUi(self, PositivityBox):
        _translate = QtCore.QCoreApplication.translate
        PositivityBox.setWindowTitle(_translate("PositivityBox", "Positivity Box"))
        self.textBrowser.setPlaceholderText(_translate("PositivityBox", "Press \"New Quote\" to see a dose of positivity."))
        self.NewQuote.setText(_translate("PositivityBox", "New Quote"))
        self.Exit.setText(_translate("PositivityBox", "Exit"))
        self.Exit.setShortcut(_translate("PositivityBox", "Ctrl+W"))
        self.actionNext_Quote.setText(_translate("PositivityBox", "Next Quote"))
        self.actionNext_Quote.setToolTip(_translate("PositivityBox", "Push here to see the next quote"))
        self.actionNext_Quote.setShortcut(_translate("PositivityBox", "Ctrl+Right"))


import background_rc
