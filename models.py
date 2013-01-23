# -*- coding:utf-8 -*-
__author__ = 'aliven.cen'

from settings import db_my as db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True)
    email = db.Column(db.String(120), unique=True)
    status = db.Column(db.Boolean,default=True)

    def __unicode__(self):
        return self.username

class PVReport(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    record_date = db.Column(db.DATE)
    pv_total = db.Column(db.Integer)
    pv_my = db.Column(db.Integer)
    pv_search = db.Column(db.Integer)
    pv_www = db.Column(db.Integer)
    pv_ehire = db.Column(db.Integer)
    pv_wap = db.Column(db.Integer)
    pv_3g = db.Column(db.Integer)
    abnormal = db.Column(db.Boolean,default=False)

    def __unicode__(self):
        return self.record_date

