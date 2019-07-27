from flask import Blueprint

bp=Blueprint("common",__name__,url_prefix="/common")

@bp.route("/index/")
def index():
    return "common"