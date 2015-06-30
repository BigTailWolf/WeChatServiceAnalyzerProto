#!/usr/bin/python

import json
import requests
import threading
from PyQt4.QtCore import QObject, pyqtSignal

class User(object):

    def __init__(self, jobj):
        self.subscribe      = jobj[u'subscribe']
        self.openid         = jobj[u'openid']
        self.nickname       = jobj[u'nickname']
        self.sex            = jobj[u'sex']
        self.language       = jobj[u'language']
        self.city           = jobj[u'city']
        self.province       = jobj[u'province']
        self.country        = jobj[u'country']
        self.headimgurl     = jobj[u'headimgurl']
        self.subscribe_time = jobj[u'subscribe_time']
        self.remark         = jobj[u'remark']
        self.groupid        = jobj[u'groupid']


class UserManager(QObject):

    connected = pyqtSignal(str)
    openidGot = pyqtSignal(str)
    error     = pyqtSignal(str)
    info      = pyqtSignal(str)
    onUser    = pyqtSignal(User)
    progress  = pyqtSignal(int, int)

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
                    self.openidGot.emit('Pull openids successfully')
                    
            else:
                errmsg = 'Connection error with code %i' %(r.status_code)
                self.error.emit(errmsg)
                
        except:
            self.error.emit('Unhandling error in show users')


    def get_user(self, openid):
        
        if openid not in self.users:
            self.load_user(openid)

        self.onUser.emit(self.users[openid])


    def dump_all_users(self):

        for openid in self.openids:
            if openid not in self.users:
                t = threading.Thread(target = self.load_user, args = (openid,))
                t.start()

    def load_user(self, openid):
        url = 'https://api.weixin.qq.com/cgi-bin/user/info?access_token=%s&openid=%s' %(self.access_token, openid)
        msg = 'loading user %s' %(openid)
        self.info.emit(msg)
        try:
            r = requests.get(url)
            if r.status_code == 200:
                jobj = json.loads(r.content)
                if jobj.has_key('openid'):
                    self.users[openid] = User(jobj)
                    self.progress.emit(len(self.users), len(self.openids))
                else:
                    errmsg = 'User information error'
                    self.error.emit(errmsg)
            else:
                errmsg = 'Connection error with code %i' %(r.status_code)
                self.error.emit(errmsg)
        except:
            self.error.emit('Unhandling error in load user info')


