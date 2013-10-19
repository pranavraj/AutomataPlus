# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'GrEnterWord.ui'
#
# Created: Sun Jan 30 19:21:00 2011
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
        MainWindow.resize(797, 174)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.groupBox = QtGui.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(9, 10, 781, 61))
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.lineEdit = QtGui.QLineEdit(self.groupBox)
        self.lineEdit.setGeometry(QtCore.QRect(10, 20, 751, 31))
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.line = QtGui.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(10, 80, 790, 3))
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.commandLinkButton = QtGui.QCommandLinkButton(self.centralwidget)
        self.commandLinkButton.setGeometry(QtCore.QRect(664, 90, 131, 40))
        self.commandLinkButton.setObjectName(_fromUtf8("commandLinkButton"))
        self.pushButton = QtGui.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(530, 90, 111, 40))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.line_3 = QtGui.QFrame(self.centralwidget)
        self.line_3.setGeometry(QtCore.QRect(70, 90, 3, 30))
        self.line_3.setFrameShape(QtGui.QFrame.VLine)
        self.line_3.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_3.setObjectName(_fromUtf8("line_3"))
        self.MoreButton = QtGui.QPushButton(self.centralwidget)
        self.MoreButton.setGeometry(QtCore.QRect(80, 90, 50, 30))
        self.MoreButton.setStyleSheet(_fromUtf8("font: 75 10pt \"MS Shell Dlg 2\";\n"
"color: rgb(0, 0, 255);"))
        self.MoreButton.setText(_fromUtf8(""))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/Images/MoreInfo.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.MoreButton.setIcon(icon)
        self.MoreButton.setIconSize(QtCore.QSize(25, 25))
        self.MoreButton.setObjectName(_fromUtf8("MoreButton"))
        self.HelpButton = QtGui.QPushButton(self.centralwidget)
        self.HelpButton.setGeometry(QtCore.QRect(10, 90, 50, 30))
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
        self.menubar.setGeometry(QtCore.QRect(0, 0, 797, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "MainWindow", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox.setTitle(QtGui.QApplication.translate("MainWindow", "Enter Word", None, QtGui.QApplication.UnicodeUTF8))
        self.commandLinkButton.setText(QtGui.QApplication.translate("MainWindow", "Next", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton.setText(QtGui.QApplication.translate("MainWindow", "<< Back", None, QtGui.QApplication.UnicodeUTF8))

import MoreInfoIcon_rc
import HelpIcon_rc
