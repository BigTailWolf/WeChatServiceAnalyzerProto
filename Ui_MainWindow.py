# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainWindow.ui'
#
# Created: Mon Jun 29 14:26:50 2015
#      by: PyQt4 UI code generator 4.10.3
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
        MainWindow.resize(650, 560)
        MainWindow.setMinimumSize(QtCore.QSize(650, 560))
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.gridLayout = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.lineEdit_secret = QtGui.QLineEdit(self.centralwidget)
        self.lineEdit_secret.setObjectName(_fromUtf8("lineEdit_secret"))
        self.gridLayout.addWidget(self.lineEdit_secret, 1, 1, 1, 5)
        self.pushButton_connect = QtGui.QPushButton(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_connect.sizePolicy().hasHeightForWidth())
        self.pushButton_connect.setSizePolicy(sizePolicy)
        self.pushButton_connect.setObjectName(_fromUtf8("pushButton_connect"))
        self.gridLayout.addWidget(self.pushButton_connect, 0, 6, 2, 1)
        self.label_appid = QtGui.QLabel(self.centralwidget)
        self.label_appid.setObjectName(_fromUtf8("label_appid"))
        self.gridLayout.addWidget(self.label_appid, 0, 0, 1, 1)
        self.pushButton_dump_all_user = QtGui.QPushButton(self.centralwidget)
        self.pushButton_dump_all_user.setObjectName(_fromUtf8("pushButton_dump_all_user"))
        self.gridLayout.addWidget(self.pushButton_dump_all_user, 7, 0, 1, 7)
        self.label_secret = QtGui.QLabel(self.centralwidget)
        self.label_secret.setObjectName(_fromUtf8("label_secret"))
        self.gridLayout.addWidget(self.label_secret, 1, 0, 1, 1)
        self.pushButton_get_openids = QtGui.QPushButton(self.centralwidget)
        self.pushButton_get_openids.setObjectName(_fromUtf8("pushButton_get_openids"))
        self.gridLayout.addWidget(self.pushButton_get_openids, 3, 0, 1, 2)
        self.lineEdit_appid = QtGui.QLineEdit(self.centralwidget)
        self.lineEdit_appid.setObjectName(_fromUtf8("lineEdit_appid"))
        self.gridLayout.addWidget(self.lineEdit_appid, 0, 1, 1, 5)
        self.progressBar = QtGui.QProgressBar(self.centralwidget)
        self.progressBar.setProperty("value", 24)
        self.progressBar.setObjectName(_fromUtf8("progressBar"))
        self.gridLayout.addWidget(self.progressBar, 3, 3, 1, 1)
        self.line = QtGui.QFrame(self.centralwidget)
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.gridLayout.addWidget(self.line, 2, 0, 1, 7)
        self.tableWidget = QtGui.QTableWidget(self.centralwidget)
        self.tableWidget.setMinimumSize(QtCore.QSize(0, 384))
        self.tableWidget.setObjectName(_fromUtf8("tableWidget"))
        self.tableWidget.setColumnCount(1)
        self.tableWidget.setRowCount(12)
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
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(11, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setItem(0, 0, item)
        self.tableWidget.horizontalHeader().setVisible(True)
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.gridLayout.addWidget(self.tableWidget, 5, 2, 2, 5)
        self.listWidget = QtGui.QListWidget(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.listWidget.sizePolicy().hasHeightForWidth())
        self.listWidget.setSizePolicy(sizePolicy)
        self.listWidget.setMinimumSize(QtCore.QSize(256, 384))
        self.listWidget.setObjectName(_fromUtf8("listWidget"))
        self.gridLayout.addWidget(self.listWidget, 5, 0, 2, 2)
        self.lcdNumber_loadedUsers = QtGui.QLCDNumber(self.centralwidget)
        self.lcdNumber_loadedUsers.setStyleSheet(_fromUtf8("QLCDNumber{\n"
"    color: rgb(100, 200, 0);    \n"
"    background-color: rgb(50, 50, 50);\n"
"}"))
        self.lcdNumber_loadedUsers.setObjectName(_fromUtf8("lcdNumber_loadedUsers"))
        self.gridLayout.addWidget(self.lcdNumber_loadedUsers, 3, 2, 1, 1)
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout.addWidget(self.label, 3, 4, 1, 1, QtCore.Qt.AlignRight)
        self.lcdNumber_totalUsers = QtGui.QLCDNumber(self.centralwidget)
        self.lcdNumber_totalUsers.setStyleSheet(_fromUtf8("QLCDNumber{\n"
"    color: rgb(100, 200, 0);    \n"
"    background-color: rgb(50, 50, 50);\n"
"}"))
        self.lcdNumber_totalUsers.setObjectName(_fromUtf8("lcdNumber_totalUsers"))
        self.gridLayout.addWidget(self.lcdNumber_totalUsers, 3, 6, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.pushButton_connect.setText(_translate("MainWindow", "Connect", None))
        self.label_appid.setText(_translate("MainWindow", "appid", None))
        self.pushButton_dump_all_user.setText(_translate("MainWindow", "Dump all user information", None))
        self.label_secret.setText(_translate("MainWindow", "secret", None))
        self.pushButton_get_openids.setText(_translate("MainWindow", "Get Openids", None))
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
        item.setText(_translate("MainWindow", "remark", None))
        item = self.tableWidget.verticalHeaderItem(11)
        item.setText(_translate("MainWindow", "groupid", None))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "User Information", None))
        __sortingEnabled = self.tableWidget.isSortingEnabled()
        self.tableWidget.setSortingEnabled(False)
        self.tableWidget.setSortingEnabled(__sortingEnabled)
        self.label.setText(_translate("MainWindow", "of total users", None))

