# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'RPLInterface.ui'
#
# Created: Sun Jan 30 19:21:02 2011
#      by: PyQt4 UI code generator 4.8.2
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(281, 401)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.OptionBox = QtGui.QGroupBox(self.centralwidget)
        self.OptionBox.setGeometry(QtCore.QRect(10, 10, 260, 301))
        self.OptionBox.setObjectName(_fromUtf8("OptionBox"))
        self.AutButton = QtGui.QCommandLinkButton(self.OptionBox)
        self.AutButton.setGeometry(QtCore.QRect(10, 20, 240, 51))
        self.AutButton.setStyleSheet(_fromUtf8(""))
        self.AutButton.setObjectName(_fromUtf8("AutButton"))
        self.line = QtGui.QFrame(self.OptionBox)
        self.line.setGeometry(QtCore.QRect(10, 70, 240, 21))
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.line_4 = QtGui.QFrame(self.OptionBox)
        self.line_4.setGeometry(QtCore.QRect(10, 140, 240, 21))
        self.line_4.setFrameShape(QtGui.QFrame.HLine)
        self.line_4.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_4.setObjectName(_fromUtf8("line_4"))
        self.AutButton_2 = QtGui.QCommandLinkButton(self.OptionBox)
        self.AutButton_2.setGeometry(QtCore.QRect(10, 90, 240, 51))
        self.AutButton_2.setStyleSheet(_fromUtf8(""))
        self.AutButton_2.setObjectName(_fromUtf8("AutButton_2"))
        self.line_9 = QtGui.QFrame(self.OptionBox)
        self.line_9.setGeometry(QtCore.QRect(10, 210, 240, 21))
        self.line_9.setFrameShape(QtGui.QFrame.HLine)
        self.line_9.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_9.setObjectName(_fromUtf8("line_9"))
        self.AutButton_3 = QtGui.QCommandLinkButton(self.OptionBox)
        self.AutButton_3.setGeometry(QtCore.QRect(10, 160, 240, 51))
        self.AutButton_3.setStyleSheet(_fromUtf8(""))
        self.AutButton_3.setObjectName(_fromUtf8("AutButton_3"))
        self.AutButton_4 = QtGui.QCommandLinkButton(self.OptionBox)
        self.AutButton_4.setGeometry(QtCore.QRect(10, 230, 240, 51))
        self.AutButton_4.setStyleSheet(_fromUtf8(""))
        self.AutButton_4.setObjectName(_fromUtf8("AutButton_4"))
        self.line_12 = QtGui.QFrame(self.OptionBox)
        self.line_12.setGeometry(QtCore.QRect(10, 280, 240, 21))
        self.line_12.setFrameShape(QtGui.QFrame.HLine)
        self.line_12.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_12.setObjectName(_fromUtf8("line_12"))
        self.pushButton = QtGui.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(180, 330, 91, 31))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.line_2 = QtGui.QFrame(self.centralwidget)
        self.line_2.setGeometry(QtCore.QRect(0, 320, 280, 3))
        self.line_2.setFrameShape(QtGui.QFrame.HLine)
        self.line_2.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_2.setObjectName(_fromUtf8("line_2"))
        self.line_3 = QtGui.QFrame(self.centralwidget)
        self.line_3.setGeometry(QtCore.QRect(70, 330, 3, 30))
        self.line_3.setFrameShape(QtGui.QFrame.VLine)
        self.line_3.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_3.setObjectName(_fromUtf8("line_3"))
        self.MoreButton = QtGui.QPushButton(self.centralwidget)
        self.MoreButton.setGeometry(QtCore.QRect(80, 330, 50, 30))
        self.MoreButton.setStyleSheet(_fromUtf8("font: 75 10pt \"MS Shell Dlg 2\";\n"
"color: rgb(0, 0, 255);"))
        self.MoreButton.setText(_fromUtf8(""))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/Images/MoreInfo.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.MoreButton.setIcon(icon)
        self.MoreButton.setIconSize(QtCore.QSize(25, 25))
        self.MoreButton.setObjectName(_fromUtf8("MoreButton"))
        self.HelpButton = QtGui.QPushButton(self.centralwidget)
        self.HelpButton.setGeometry(QtCore.QRect(10, 330, 50, 30))
        self.HelpButton.setStyleSheet(_fromUtf8("font: 75 11pt \"MS Shell Dlg 2\";\n"
"color: rgb(85, 0, 127);"))
        self.HelpButton.setText(_fromUtf8(""))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8(":/Images/Help.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.HelpButton.setIcon(icon1)
        self.HelpButton.setIconSize(QtCore.QSize(44, 26))
        self.HelpButton.setObjectName(_fromUtf8("HelpButton"))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 281, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "MainWindow", None, QtGui.QApplication.UnicodeUTF8))
        self.OptionBox.setTitle(QtGui.QApplication.translate("MainWindow", "SELECT AN OPTION", None, QtGui.QApplication.UnicodeUTF8))
        self.AutButton.setToolTip(QtGui.QApplication.translate("MainWindow", "AUTOMATA", None, QtGui.QApplication.UnicodeUTF8))
        self.AutButton.setText(QtGui.QApplication.translate("MainWindow", "TYPE OF\n"
"GRAMMAR", None, QtGui.QApplication.UnicodeUTF8))
        self.AutButton_2.setToolTip(QtGui.QApplication.translate("MainWindow", "AUTOMATA", None, QtGui.QApplication.UnicodeUTF8))
        self.AutButton_2.setText(QtGui.QApplication.translate("MainWindow", "IDENTIFY LEFT\n"
"RECURSION", None, QtGui.QApplication.UnicodeUTF8))
        self.AutButton_3.setToolTip(QtGui.QApplication.translate("MainWindow", "AUTOMATA", None, QtGui.QApplication.UnicodeUTF8))
        self.AutButton_3.setText(QtGui.QApplication.translate("MainWindow", "GRAMMAR TO\n"
"CFG", None, QtGui.QApplication.UnicodeUTF8))
        self.AutButton_4.setToolTip(QtGui.QApplication.translate("MainWindow", "AUTOMATA", None, QtGui.QApplication.UnicodeUTF8))
        self.AutButton_4.setText(QtGui.QApplication.translate("MainWindow", "CYK\n"
"ALGORITHM", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton.setText(QtGui.QApplication.translate("MainWindow", "< Back", None, QtGui.QApplication.UnicodeUTF8))

import MoreInfoIcon_rc
import HelpIcon_rc
