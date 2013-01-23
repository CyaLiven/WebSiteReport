#-*- coding:utf-8 -*-
__author__ = 'aliven.cen'


from flask.ext.admin import Admin
from flask.ext.admin.contrib.fileadmin import FileAdmin
import os.path as op
from settings import app, db_sqlite
from admin_views import MyView, MyHome, PVReportView

@app.route('/')
def index():
    return '<a href="/admin/">Click me to get to Admin!</a>'

if __name__ == '__main__':
    #创建数据库
    db_sqlite.create_all()

    #创建admin界面
    admin = Admin(index_view=MyHome(name=u'首页'), name='51job')
    admin.add_view(MyView(db_sqlite.session, name=u'用户管理', endpoint='user'))
    path = op.join(op.dirname(__file__), 'static')
    admin.add_view(FileAdmin(path, '/static/', name=u'上传文件', endpoint='upload'))
    admin.add_view(PVReportView(db_sqlite.session, name='PV', endpoint='PV', category=u'网站统计'))
    admin.init_app(app)

    #运行应用
    app.debug = True
    app.run()

