#!/usr/bin/python

import json
import requests
from PyQt4.QtGui   import QMainWindow
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
        self.pushButton_connect.clicked.connect(self.onConnect)
        self.pushButton_get_openids.clicked.connect(self.onGetOpenids)
        self.pushButton_get_openids.setEnabled(False)
        self.manager.connected.connect(self.onConnected)
        self.manager.openidGot.connect(self.onOpenidGot)
        self.listWidget.currentItemChanged.connect(self.onOpenidFocus)

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
        openid = target.text()
        self.manager.get_user(openid)
