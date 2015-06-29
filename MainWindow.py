#!/usr/bin/python

import json
import requests
from PyQt4.QtGui   import QMainWindow
from PyQt4.QtGui   import QTableWidgetItem
from Ui_MainWindow import Ui_MainWindow
from UserManager   import UserManager


class MainWindow(QMainWindow, Ui_MainWindow):

    def __init__(self, parent=None):
        QMainWindow.__init__(self, parent)
        Ui_MainWindow.setupUi(self, self)
        self.manager = UserManager()
        self.users = {}
        self.lineEdit_appid.setText('wxaafc0692eca7f8d6')
        self.lineEdit_secret.setText('077b4e1bed2b773c1014efa4512cd652')
        self.progressBar.setValue(0)
        self.pushButton_get_openids.setEnabled(False)
        
        self.pushButton_connect.clicked.connect(self.onConnect)
        self.pushButton_get_openids.clicked.connect(self.onGetOpenids)
        self.listWidget.currentItemChanged.connect(self.onOpenidFocus)
        self.manager.connected.connect(self.onConnected)
        self.manager.openidGot.connect(self.onOpenidGot)
        self.manager.info.connect(self.onInfo)
        self.manager.error.connect(self.onError)
        self.manager.onUser.connect(self.onUserInfo)

    def onInfo(self, msg):
        self.statusBar().showMessage(msg)

    def onError(self, errmsg):
        self.statusBar().showMessage(errmsg)

    def onConnect(self):
        self.statusBar().showMessage('Connecting WeChat Server');
        appid = self.lineEdit_appid.text()
        secret = self.lineEdit_secret.text()
        self.manager.connect(appid, secret)

    def onConnected(self, msg):
        self.pushButton_get_openids.setEnabled(True)
        self.statusBar().showMessage(msg)

    def onGetOpenids(self):
        self.statusBar().showMessage('Getting openids');
        self.manager.get_openids()

    def onOpenidGot(self, msg):
        self.statusBar().showMessage(msg)
        self.listWidget.addItems(self.manager.openids)
        self.progressBar.setValue(0)
        self.lcdNumber_totalUsers.display(len(self.manager.openids))

    def onOpenidFocus(self, target):
        openid = target.text().__str__()
        self.manager.get_user(openid)
        self.lcdNumber_loadedUsers.display(len(self.manager.users))
        percentage = 100 * self.lcdNumber_loadedUsers.value() / self.lcdNumber_totalUsers.value()
        self.progressBar.setValue(percentage)

    def onUserInfo(self, user):

        #self.tableWidget.setItem( 1, 0, QTableWidgetItem('1'))
        #self.tableWidget.setItem( 2, 0, QTableWidgetItem('2'))
        #self.tableWidget.setItem( 3, 0, QTableWidgetItem( 3))
        #self.tableWidget.setItem( 4, 0, QTableWidgetItem( 4))
        #self.tableWidget.setItem( 5, 0, QTableWidgetItem( 5))
        #self.tableWidget.setItem( 6, 0, QTableWidgetItem( 6))
        #self.tableWidget.setItem( 7, 0, QTableWidgetItem( 7))
        #self.tableWidget.setItem( 8, 0, QTableWidgetItem( 8))
        #self.tableWidget.setItem( 9, 0, QTableWidgetItem( 9))
        #self.tableWidget.setItem(10, 0, QTableWidgetItem(10))
        #self.tableWidget.setItem(11, 0, QTableWidgetItem(11))
        #self.tableWidget.setItem(12, 0, QTableWidgetItem(12))

        self.tableWidget.setItem( 0, 0, QTableWidgetItem(str(user.subscribe))     )
        self.tableWidget.setItem( 1, 0, QTableWidgetItem(user.openid)             )
        self.tableWidget.setItem( 2, 0, QTableWidgetItem(user.nickname)           )
        self.tableWidget.setItem( 3, 0, QTableWidgetItem(str(user.sex))           )
        self.tableWidget.setItem( 4, 0, QTableWidgetItem(user.language)           )
        self.tableWidget.setItem( 5, 0, QTableWidgetItem(user.city)               )
        self.tableWidget.setItem( 6, 0, QTableWidgetItem(user.province)           )
        self.tableWidget.setItem( 7, 0, QTableWidgetItem(user.country)            )
        self.tableWidget.setItem( 8, 0, QTableWidgetItem(user.headimgurl)         )
        self.tableWidget.setItem( 9, 0, QTableWidgetItem(str(user.subscribe_time)))
        self.tableWidget.setItem(10, 0, QTableWidgetItem(user.remark)             )
        self.tableWidget.setItem(11, 0, QTableWidgetItem(str(user.groupid))       )
