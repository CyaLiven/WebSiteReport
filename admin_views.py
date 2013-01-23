#-*- coding:utf-8 -*-
__author__ = 'aliven.cen'

from flask.ext.admin import expose, AdminIndexView
from flask.ext.admin.contrib.sqlamodel import ModelView
from wtforms.fields import SelectField
from models import User, PVReport

class MyHome(AdminIndexView):
    @expose('/')
    def index(self):
        return self.render('MyView.html')

status_choices = [(0, 'waiting'), (1, 'in_progress'), (2, 'finished')]

def get_status_choices(context, model, name):
    status_choices_dict = dict(status_choices)
    return status_choices_dict.get(model.status, 'error')

class MyView(ModelView):
    # Disable model creation
    can_create = True

    # Override displayed fields
    column_list = ('username', 'email', 'status')
    column_labels = dict(username=u'用户名', status=u'状态')
    column_formatters = dict(status=get_status_choices)

    form_overrides = dict(status=SelectField)
    form_args = dict(
        # Pass the choices to the `SelectField`
        status=dict(
            choices=status_choices,coerce=int
        ))

    def __init__(self, session, **kwargs):
        # You can pass name and other parameters if you want to
        super(MyView, self).__init__(User, session, **kwargs)

class PVReportView(ModelView):
    can_delete = False

    #column_sortable_list = ['record_date', 'abnormal']
    column_labels = dict(
        record_date = u'时间',
        pv_total    = u'pv总数',
        pv_my       = u'my频道',
        pv_search   = u'search频道',
        pv_www      = u'www频道',
        pv_ehire    = u'ehire频道',
        pv_wap      = u'wap频道',
        pv_3g       = u'3G频道',
        abnormal    = u'异常',
    )
    column_filters = ('pv_total','abnormal')

    def __init__(self, session, **kwargs):
        super(PVReportView, self).__init__(PVReport, session, **kwargs)

