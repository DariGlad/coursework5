from flask import render_template, Blueprint

app = Blueprint("main_bp", __name__)


@app.route("/")
def menu_page() -> str:
    """ Главное меню """

    return render_template("index.html")
