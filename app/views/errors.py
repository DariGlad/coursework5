from typing import Tuple

from flask import Blueprint, render_template

app = Blueprint("errors_bp", __name__)


@app.app_errorhandler(404)  # Обработчик ошибки 404
def page_404(e: Exception) -> Tuple[str, int]:
    return render_template("404.html"), 404


@app.app_errorhandler(ValueError)  # Обработчик ошибки ValueError
def page_value_error(e: Exception) -> Tuple[str, int]:
    return render_template("404.html"), 404


@app.app_errorhandler(500)  # Обработчик ошибки 500
def page_500(e: Exception) -> Tuple[str, int]:
    return render_template("500.html"), 500


@app.app_errorhandler(405)  # Обработчик ошибки 405
def page_405(e: Exception) -> Tuple[str, int]:
    return render_template("500.html"), 405
