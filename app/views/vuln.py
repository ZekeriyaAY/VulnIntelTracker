from flask import Blueprint, render_template

bp = Blueprint("vuln", __name__, template_folder="../templates")


@bp.route("/vuln")
def Vuln():
    return render_template("vulnerability/list.html")


@bp.route("/vuln/add")
def VulnAdd():
    return render_template("vulnerability/add.html")
