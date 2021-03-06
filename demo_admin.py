#-*- coding:utf-8 -*-
__author__ = 'aliven.cen'


from flask.ext.admin import Admin
from flask.ext.admin.contrib.fileadmin import FileAdmin
import os.path as op
from settings import app, db_my
from admin_views import UserView, MyIndex, PVReportView,\
                          IPReportView, UVReportView, FlowReportView,\
                          CDNReportView, AbnormalReportView

@app.route('/')
def index():
    return '<a href="/admin/">Click me to get to Admin!</a>'

if __name__ == '__main__':
    #创建数据库
    db_my.create_all()

    #创建admin界面
    admin = Admin(index_view=MyIndex(name=u'首页'), name='51job')
    admin.add_view(UserView(db_my.session, name=u'用户管理', endpoint='user'))
    admin.add_view(PVReportView(db_my.session, name=u'PV统计', endpoint='pv', category=u'网站统计'))
    admin.add_view(IPReportView(db_my.session, name=u'IP统计', endpoint='ip', category=u'网站统计'))
    admin.add_view(UVReportView(db_my.session, name=u'UV统计', endpoint='uv', category=u'网站统计'))
    admin.add_view(FlowReportView(db_my.session, name=u'流量统计', endpoint='flow', category=u'网站统计'))
    admin.add_view(CDNReportView(db_my.session, name=u'CDN统计', endpoint='cdn', category=u'网站统计'))
    admin.add_view(AbnormalReportView(db_my.session, name=u'异常记录', endpoint='abnormal'))
    path = op.join(op.dirname(__file__), 'static')
    admin.add_view(FileAdmin(path, '/static/', name=u'原始数据文件', endpoint='upload'))
    admin.init_app(app)

    #运行应用
    app.debug = True
    app.run()

