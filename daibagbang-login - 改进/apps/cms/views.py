from flask import Blueprint,url_for,render_template,views,request,session,redirect
from .forms import LoginForm
from .models import CMSUser
import config
bp=Blueprint("cms",__name__,url_prefix="/cms")


@bp.route('/')
def index():
    return render_template("cms/home.html")

class loginView(views.MethodView):
    def get(self,message=None):
        return render_template("cms/daibangbang-login.html",message=message)
    def post(self):
        form = LoginForm(request.form)
        if form.validate():
            username=form.username.data
            password=form.password.data
            remember=form.remember.data
            user = CMSUser.query.filter_by(username=username).first()
            # if user and user.check_password(password):
            if user:
                session[config.CMS_USER_ID]=user.id
                if remember:
                    session.permanent=True
                return redirect(url_for("cms.index"))
            else:
                return self.get(message="用户名或密码错误")
        else:
            print(form.errors)
            return self.get(message='表单验证错误')

bp.add_url_rule("/login/",view_func=loginView.as_view("login"))