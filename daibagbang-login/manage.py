#encoding: utf-8

from flask_script import Manager
from flask_migrate import Migrate,MigrateCommand
from daibangbang import create_app
from exts import db
from apps.cms import models as cms_models

CMSUser = cms_models.CMSUser

app = create_app()

manager = Manager(app)

Migrate(app,db)
manager.add_command('db',MigrateCommand)

@manager.option('-u','--username',dest='username')
@manager.option('-p','--password',dest='password')

def create_cms_user(username,password):
    user = CMSUser(username=username,password=password)
    db.session.add(user)
    db.session.commit()
    print('cms用户添加成功！')

if __name__ == '__main__':
    manager.run()