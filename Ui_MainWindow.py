# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainWindow.ui'
#
# Created: Wed Jun 24 23:01:00 2015
#      by: PyQt4 UI code generator 4.11.2
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

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(792, 500)
        MainWindow.setMinimumSize(QtCore.QSize(400, 500))
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.gridLayout = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.label_appid = QtGui.QLabel(self.centralwidget)
        self.label_appid.setObjectName(_fromUtf8("label_appid"))
        self.gridLayout.addWidget(self.label_appid, 0, 0, 1, 1)
        self.lineEdit_appsecret = QtGui.QLineEdit(self.centralwidget)
        self.lineEdit_appsecret.setObjectName(_fromUtf8("lineEdit_appsecret"))
        self.gridLayout.addWidget(self.lineEdit_appsecret, 1, 1, 1, 2)
        self.pushButton_connect = QtGui.QPushButton(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_connect.sizePolicy().hasHeightForWidth())
        self.pushButton_connect.setSizePolicy(sizePolicy)
        self.pushButton_connect.setObjectName(_fromUtf8("pushButton_connect"))
        self.gridLayout.addWidget(self.pushButton_connect, 0, 3, 2, 1)
        self.tableWidget = QtGui.QTableWidget(self.centralwidget)
        self.tableWidget.setObjectName(_fromUtf8("tableWidget"))
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(11)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(2, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(3, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(4, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(5, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(6, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(7, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(8, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(9, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(10, item)
        self.gridLayout.addWidget(self.tableWidget, 4, 2, 2, 1)
        self.lineEdit_appid = QtGui.QLineEdit(self.centralwidget)
        self.lineEdit_appid.setObjectName(_fromUtf8("lineEdit_appid"))
        self.gridLayout.addWidget(self.lineEdit_appid, 0, 1, 1, 2)
        self.listWidget = QtGui.QListWidget(self.centralwidget)
        self.listWidget.setObjectName(_fromUtf8("listWidget"))
        self.gridLayout.addWidget(self.listWidget, 4, 0, 2, 2)
        self.label_appsecret = QtGui.QLabel(self.centralwidget)
        self.label_appsecret.setObjectName(_fromUtf8("label_appsecret"))
        self.gridLayout.addWidget(self.label_appsecret, 1, 0, 1, 1)
        self.pushButton_show_users = QtGui.QPushButton(self.centralwidget)
        self.pushButton_show_users.setObjectName(_fromUtf8("pushButton_show_users"))
        self.gridLayout.addWidget(self.pushButton_show_users, 2, 0, 1, 2)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.label_appid.setText(_translate("MainWindow", "appid", None))
        self.pushButton_connect.setText(_translate("MainWindow", "Connect", None))
        item = self.tableWidget.verticalHeaderItem(0)
        item.setText(_translate("MainWindow", "subscribe", None))
        item = self.tableWidget.verticalHeaderItem(1)
        item.setText(_translate("MainWindow", "openid", None))
        item = self.tableWidget.verticalHeaderItem(2)
        item.setText(_translate("MainWindow", "nickname", None))
        item = self.tableWidget.verticalHeaderItem(3)
        item.setText(_translate("MainWindow", "sex", None))
        item = self.tableWidget.verticalHeaderItem(4)
        item.setText(_translate("MainWindow", "language", None))
        item = self.tableWidget.verticalHeaderItem(5)
        item.setText(_translate("MainWindow", "city", None))
        item = self.tableWidget.verticalHeaderItem(6)
        item.setText(_translate("MainWindow", "province", None))
        item = self.tableWidget.verticalHeaderItem(7)
        item.setText(_translate("MainWindow", "country", None))
        item = self.tableWidget.verticalHeaderItem(8)
        item.setText(_translate("MainWindow", "headimgurl", None))
        item = self.tableWidget.verticalHeaderItem(9)
        item.setText(_translate("MainWindow", "subscribe_time", None))
        item = self.tableWidget.verticalHeaderItem(10)
        item.setText(_translate("MainWindow", "groupid", None))
        self.label_appsecret.setText(_translate("MainWindow", "appsecret", None))
        self.pushButton_show_users.setText(_translate("MainWindow", "Show Users", None))

