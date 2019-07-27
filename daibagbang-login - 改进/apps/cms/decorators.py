import config
from functools import wraps
from flask import session,redirect,url_for
def login_require(func):
    @wraps(func)
    def inner(*args,**kwargs):
        if config.CMS_USER_ID in session:
            return func(*args,**kwargs)
        else:
            return redirect(url_for("cms.index"))
    return inner