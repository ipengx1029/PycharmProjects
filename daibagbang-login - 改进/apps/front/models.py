from exts import db

from werkzeug.security import generate_password_hash,check_password_hash
import enum
from datetime import datetime

# pip install shortuuid



class FrontUser(db.Model):
    __tablename__ = 'front_user'
    id = db.Column(db.String(100),primary_key=True)
    username = db.Column(db.String(11),nullable=False,unique=True)
    _password = db.Column(db.String(100), nullable=False)
    join_time = db.Column(db.DateTime,default=datetime.now)

    def __init__(self,*args,**kwargs):
        if "password" in kwargs:
            self.password = kwargs.get('password')
            kwargs.pop("password")
        super(FrontUser, self).__init__(*args,**kwargs)


    @property
    def password(self):
        return self._password

    @password.setter
    def password(self,newpwd):
        self._password = generate_password_hash(newpwd)

    def check_password(self,rawpwd):
        return check_password_hash(self._password,rawpwd)