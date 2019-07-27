from apps import BaseForm
from wtforms import Form,StringField,IntegerField
from wtforms.validators import InputRequired,Regexp,Length
from wtforms.validators import Regexp,ValidationError


class SignupForm(Form):
    username=StringField(validators=[Regexp(r'1[38745]\d{9}',message="手机号码格式错误")])
    password = StringField(validators=[Regexp(r"[0-9a-zA-Z_\.]{6,20}", message='请输入正确格式的密码！')])