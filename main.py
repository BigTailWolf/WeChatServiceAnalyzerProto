#!/usr/bin/python

import sys
import json
import requests
from PyQt4.QtGui   import QApplication, QMainWindow
from Ui_MainWindow import Ui_MainWindow


class MainWindow(QMainWindow, Ui_MainWindow):

    def __init__(self, parent=None):
        QMainWindow.__init__(self, parent)
        Ui_MainWindow.setupUi(self, self)
        self.lineEdit_appid.setText('wxaafc0692eca7f8d6')
        self.lineEdit_appsecret.setText('077b4e1bed2b773c1014efa4512cd652')
        self.pushButton_connect.clicked.connect(self.onConnect)
        self.pushButton_show_users.clicked.connect(self.onShowUsers)
        self.pushButton_show_users.setEnabled(False)

    def onConnect(self):
        self.statusBar().showMessage('Connecting WeChat Server');
        appid = self.lineEdit_appid.text()
        appsecret = self.lineEdit_appsecret.text()
        url = 'https://api.weixin.qq.com/cgi-bin/token?grant_type=client_credential&appid=%s&secret=%s' %(appid, appsecret)
        try:
            r = requests.get(url)
            if r.status_code == 200:
                content = json.loads(r.content)
                if content.has_key('access_token'):
                    self.access_token = content['access_token']
                    self.statusBar().showMessage('Connected successfully')
                    self.pushButton_show_users.setEnabled(True)
                elif content.has_key('errmsg'):
                    errmsg = content['errmsg']
                    self.statusBar().showMessage(errmsg)
                else:
                    self.statusBar().showMessage('Unhandling error with server connected')

            else:
                errmsg = 'Connection error with code %i' %(r.status_code)
                self.statusBar().showMessage(errmsg)
        except:
            self.statusBar().showMessage('Unhandling error in connection')

    def onShowUsers(self):
        self.statusBar().showMessage('requesting get users')
        url = 'https://api.weixin.qq.com/cgi-bin/user/get?access_token=%s&next_openid=' %(self.access_token)
        try:
            r = requests.get(url)
            if r.status_code == 200:
                content = json.loads(r.content)
                if content.has_key('data'):
                    self.openids = content['data']['openid']
                    count = len(self.openids)
                    self.listWidget.addItems(self.openids)
                    #self.users = []
                    #for i in self.openids:
                    #    url = 'https://api.weixin.qq.com/cgi-bin/user/info?access_token=%s&openid=%s' %(self.access_token, i)
                    #    r = requests.get(url)
                    #    content = json.loads(r.content)
                    #    self.users.append(content)
                    #    msg = '%i/%i users information pulled' %(len(self.users), count)
                    #    self.statusBar().showMessage(msg)
            else:
                errmsg = 'Connection error with code %i' %(r.status_code)
                self.statusBar.showMessage(errmsg)
                
        except:
            self.statusBar().showMessage('Unhandling error in show users')

def main():
    app = QApplication(sys.argv)
    ex  = MainWindow()
    ex.show()
    sys.exit(app.exec_())


if __name__ == '__main__':

    main()

