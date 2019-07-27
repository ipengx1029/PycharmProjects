from wtforms import Form,StringField,IntegerField
from wtforms.validators import InputRequired,Regexp,Length
import re
class LoginForm(Form):
    username= StringField(validators=[Regexp(r'1[38745]\d{9}',message="手机号码格式错误"),InputRequired(message="请输入用户名/手机号")])
    password=StringField(validators=[Length(min=2,max=16,message="请输入正确长度的密码"),InputRequired(message="请输入密码")])
    remember=IntegerField()

