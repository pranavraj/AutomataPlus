# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'DispInterface.ui'
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
        MainWindow.resize(1056, 623)
        MainWindow.setMaximumSize(QtCore.QSize(16777215, 16777215))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("Images/AutPlusLogo.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setIconSize(QtCore.QSize(30, 30))
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.graphicsView = QtGui.QGraphicsView(self.centralwidget)
        self.graphicsView.setGeometry(QtCore.QRect(0, 0, 1060, 540))
        self.graphicsView.setObjectName(_fromUtf8("graphicsView"))
        self.pushButton = QtGui.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(970, 550, 81, 31))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.line = QtGui.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(0, 540, 1060, 3))
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.line_3 = QtGui.QFrame(self.centralwidget)
        self.line_3.setGeometry(QtCore.QRect(80, 550, 3, 30))
        self.line_3.setFrameShape(QtGui.QFrame.VLine)
        self.line_3.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_3.setObjectName(_fromUtf8("line_3"))
        self.MoreButton = QtGui.QPushButton(self.centralwidget)
        self.MoreButton.setGeometry(QtCore.QRect(90, 550, 50, 30))
        self.MoreButton.setStyleSheet(_fromUtf8("font: 75 10pt \"MS Shell Dlg 2\";\n"
"color: rgb(0, 0, 255);"))
        self.MoreButton.setText(_fromUtf8(""))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8(":/Images/MoreInfo.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.MoreButton.setIcon(icon1)
        self.MoreButton.setIconSize(QtCore.QSize(25, 25))
        self.MoreButton.setObjectName(_fromUtf8("MoreButton"))
        self.HelpButton = QtGui.QPushButton(self.centralwidget)
        self.HelpButton.setGeometry(QtCore.QRect(20, 550, 50, 30))
        self.HelpButton.setStyleSheet(_fromUtf8("font: 75 11pt \"MS Shell Dlg 2\";\n"
"color: rgb(85, 0, 127);"))
        self.HelpButton.setText(_fromUtf8(""))
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(_fromUtf8(":/Images/Help.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.HelpButton.setIcon(icon2)
        self.HelpButton.setIconSize(QtCore.QSize(44, 26))
        self.HelpButton.setObjectName(_fromUtf8("HelpButton"))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1056, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuFile = QtGui.QMenu(self.menubar)
        self.menuFile.setObjectName(_fromUtf8("menuFile"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.actionSave_Automata = QtGui.QAction(MainWindow)
        self.actionSave_Automata.setObjectName(_fromUtf8("actionSave_Automata"))
        self.menuFile.addAction(self.actionSave_Automata)
        self.menubar.addAction(self.menuFile.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "Automata+ : Automata Image", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton.setText(QtGui.QApplication.translate("MainWindow", "Finish", None, QtGui.QApplication.UnicodeUTF8))
        self.menuFile.setTitle(QtGui.QApplication.translate("MainWindow", "Options", None, QtGui.QApplication.UnicodeUTF8))
        self.actionSave_Automata.setText(QtGui.QApplication.translate("MainWindow", "Save Automata", None, QtGui.QApplication.UnicodeUTF8))

import MoreInfoIcon_rc
import HelpIcon_rc
