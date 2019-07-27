from flask import Blueprint,url_for,render_template,views,request,sessions,redirect
from .forms import LoginForm
from .models import CMSUser
bp=Blueprint("cms",__name__,url_prefix="/cms")


@bp.route('/')
def index():
    return "登录成功"

class loginView(views.MethodView):
    def get(self):
        return render_template("daibangbang-login.html")
    def post(self):
        form = LoginForm(request.form)
        if form.validate():
            username=form.username.data
            password=form.password.data
            remember=form.remember.data
            user = CMSUser.query.filter_by(username=username).first()
            if user and user.check_password(password):
                # sessions["user_id"]=user.id
                if remember:
                    sessions.permanent=True
                return render_template("home.html")
            else:
                return self.get()
        else:
            print(form.errors)
            return self.get()


bp.add_url_rule("/login/",view_func=loginView.as_view("login"))