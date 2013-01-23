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

class IPReport(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    record_date = db.Column(db.DATE)
    ip_total = db.Column(db.Integer)
    ip_my = db.Column(db.Integer)
    ip_search = db.Column(db.Integer)
    ip_www = db.Column(db.Integer)
    ip_ehire = db.Column(db.Integer)
    ip_wap = db.Column(db.Integer)
    ip_3g = db.Column(db.Integer)
    abnormal = db.Column(db.Boolean,default=False)

    def __unicode__(self):
        return self.record_date

class UVReport(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    record_date = db.Column(db.DATE)
    uv_total = db.Column(db.Integer)
    abnormal = db.Column(db.Boolean,default=False)

    def __unicode__(self):
        return self.record_date

class FlowReport(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    record_date = db.Column(db.DATE)
    out_max_sh_tel = db.Column(db.Float(7,2))
    out_avg_sh_tel = db.Column(db.Float(7,2))
    in_max_sh_tel = db.Column(db.Float(7,2))
    in_avg_sh_tel = db.Column(db.Float(7,2))
    out_max_sh_cnc = db.Column(db.Float(7,2))
    out_avg_sh_cnc = db.Column(db.Float(7,2))
    in_max_sh_cnc = db.Column(db.Float(7,2))
    in_avg_sh_cnc = db.Column(db.Float(7,2))
    out_max_tj_cnc = db.Column(db.Float(7,2))
    out_avg_tj_cnc = db.Column(db.Float(7,2))
    in_max_tj_cnc = db.Column(db.Float(7,2))
    in_avg_tj_cnc = db.Column(db.Float(7,2))
    abnormal = db.Column(db.Boolean,default=False)

    def __unicode__(self):
        return self.record_date

class CDNReport(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    record_date = db.Column(db.DATE)
    cdn_total = db.Column(db.Float(10,2))
    cdn_peak = db.Column(db.Float(10,2))
    abnormal = db.Column(db.Boolean,default=False)

    def __unicode__(self):
        return self.record_date

class AbnormalReport(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    record_date = db.Column(db.DATE)
    content = db.Column(db.TEXT(2000))

    def __unicode__(self):
        return self.record_date