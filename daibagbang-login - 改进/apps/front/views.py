from .models import  FrontUser
from flask import Blueprint,views,redirect,render_template,request
from apps.front.forms import SignupForm
from exts import db
from apps.cms.models import CMSUser
bp=Blueprint("front",__name__)

@bp.route("/")
def index():
    return "front index"

# class SignupView(views.MethodView):
#     def get(self):
#         return render_template("front/front_signup.html")
#
#     def post(self):
#         form = SignupForm(request.form)
#         if form.validate():
#             username = form.username.data
#             password = form.password.data
#             user = FrontUser(username=username,password=password)
#             db.session.add(user)
#             db.session.commit()
#         else:
#             return "错误了"


class SignupView(views.MethodView):
    def get(self):
        return render_template("front/front_signup.html")

    def post(self):
        username = request.form.get('username')
        password = request.form.get('password')
        user = CMSUser(username=username,password=password)
        db.session.add(user)
        db.session.commit()
        return "注册啦"

bp.add_url_rule("/signup/",view_func=SignupView.as_view("signup"))