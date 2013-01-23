#-*- coding:utf-8 -*-
__author__ = 'aliven.cen'

from flask.ext.admin import expose, AdminIndexView
from flask.ext.admin.contrib.sqlamodel import ModelView
from models import User, PVReport, IPReport, UVReport, FlowReport, CDNReport, AbnormalReport
from libs.MyFields import TextAreaField

class MyIndex(AdminIndexView):
    @expose('/')
    def index(self):
        return self.render('MyIndex.html')

class UserView(ModelView):
    can_create = True

    column_list = ('username', 'email', 'status')
    column_labels = dict(username=u'用户名', status=u'状态')

    def __init__(self, session, **kwargs):
        super(UserView, self).__init__(User, session, **kwargs)

class PVReportView(ModelView):
    can_delete = False

    column_labels = dict(
        record_date = u'时间',
        pv_total    = u'PV总数',
        pv_my       = u'My频道',
        pv_search   = u'Search频道',
        pv_www      = u'WWW频道',
        pv_ehire    = u'ehire频道',
        pv_wap      = u'Wap频道',
        pv_3g       = u'3G频道',
        abnormal    = u'异常',
    )
    column_filters = ('pv_total','abnormal')

    def __init__(self, session, **kwargs):
        super(PVReportView, self).__init__(PVReport, session, **kwargs)

class IPReportView(ModelView):
    can_delete = False

    column_labels = dict(
        record_date = u'时间',
        ip_total    = u'IP总数',
        ip_my       = u'My频道',
        ip_search   = u'Search频道',
        ip_www      = u'WWW频道',
        ip_ehire    = u'ehire频道',
        ip_wap      = u'Wap频道',
        ip_3g       = u'3G频道',
        abnormal    = u'异常',
    )
    column_filters = ('ip_total','abnormal')

    def __init__(self, session, **kwargs):
        super(IPReportView, self).__init__(IPReport, session, **kwargs)

class UVReportView(ModelView):
    can_delete = False

    column_labels = dict(
        record_date = u'时间',
        uv_total    = u'UV总数',
        abnormal    = u'异常',
    )
    column_filters = ('uv_total','abnormal')

    def __init__(self, session, **kwargs):
        super(UVReportView, self).__init__(UVReport, session, **kwargs)

class FlowReportView(ModelView):
    can_delete = False

    column_labels = dict(
        record_date    = u'时间',
        out_max_sh_tel = u'上海电信最大流出',
        out_avg_sh_tel = u'上海电信平均流出',
        in_max_sh_tel  = u'上海电信最大流入',
        in_avg_sh_tel  = u'上海电信平均流入',
        out_max_sh_cnc = u'上海联通最大流出',
        out_avg_sh_cnc = u'上海联通平均流出',
        in_max_sh_cnc  = u'上海联通最大流入',
        in_avg_sh_cnc  = u'上海联通平均流入',
        out_max_tj_cnc = u'天津联通最大流出',
        out_avg_tj_cnc = u'天津联通平均流出',
        in_max_tj_cnc  = u'天津联通最大流入',
        in_avg_tj_cnc  = u'天津联通平均流入',
        abnormal       = u'异常',
    )
    column_filters = ('abnormal',)

    def __init__(self, session, **kwargs):
        super(FlowReportView, self).__init__(FlowReport, session, **kwargs)

class CDNReportView(ModelView):
    can_delete = False

    column_labels = dict(
        record_date = u'时间',
        cdn_total   = u'CDN总流量',
        cdn_peak    = u'CDN峰值流量',
        abnormal    = u'异常',
    )
    column_filters = ('abnormal',)

    def __init__(self, session, **kwargs):
        super(CDNReportView, self).__init__(CDNReport, session, **kwargs)

class AbnormalReportView(ModelView):
    can_delete = False

    form_overrides = dict(content=TextAreaField)

    form_args = dict(
        content=dict(width=500, high=200)
    )

    column_labels = dict(
            record_date = u'时间',
            content     = u'批注'
        )

    def __init__(self, session, **kwargs):
            super(AbnormalReportView, self).__init__(AbnormalReport, session, **kwargs)