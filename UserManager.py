#!/usr/bin/python

import json
import requests
from PyQt4.QtCore import QObject, pyqtSignal

class User(object):

    def __init__(self, jstr):
        jobj = json.load(jstr)
        self.subscribe      = jobj['subscribe']
        self.openid         = jobj['openid']
        self.nickname       = jobj['nickname']
        self.sex            = jobj['sex']
        self.language       = jobj['language']
        self.city           = jobj['city']
        self.province       = jobj['province']
        self.country        = jobj['country']
        self.headimgurl     = jobj['headimgurl']
        self.subscribe_time = jobj['subscribe_time']
        self.remark         = jobj['remark']
        self.groupid        = jobj['groupid']


class UserManager(QObject):

    connected = pyqtSignal(str)
    openidGot = pyqtSignal(str)
    error     = pyqtSignal(str)

    def __init__(self):
        QObject.__init__(self)
        self.reset()

    def reset(self):
        self.users = {}

    def connect(self, appid, secret):
        url = 'https://api.weixin.qq.com/cgi-bin/token?grant_type=client_credential&appid=%s&secret=%s' %(appid, secret)
        try:
            r = requests.get(url)
            if r.status_code == 200:
                content = json.loads(r.content)
                if content.has_key('access_token'):
                    self.access_token = content['access_token']
                    self.connected.emit('Connected to server successfully')
                elif content.has_key('errmsg'):
                    errmsg = content['errmsg']
                else:
                    self.error.emit('Unknown error in connection')

            else:
                errmsg = 'Connection error with code %i' %(r.status_code)
                self.error.emit(errmsg)
        except:
            self.error.emit('Unhandling error in connection')
 
    def get_openids(self):
        url = 'https://api.weixin.qq.com/cgi-bin/user/get?access_token=%s&next_openid=' %(self.access_token)
        try:
            r = requests.get(url)
            if r.status_code == 200:
                content = json.loads(r.content)
                if content.has_key('data'):
                    self.openids = content['data']['openid']
                    print self.openids
                    self.openidGot.emit('Pull openids successfully')
                    
            else:
                errmsg = 'Connection error with code %i' %(r.status_code)
                self.error.emit(errmsg)
                
        except:
            self.error.emit('Unhandling error in show users')

    def get_user(self, openid):
        print 'Pulling information of %s' %(openid)

