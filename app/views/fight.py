from flask import Blueprint, render_template, redirect, url_for
from werkzeug import Response

from app.container import arena, heroes

app = Blueprint("fight_bp", __name__)


@app.route("/")
def start_fight() -> str:
    """ Начало боя """

    arena.start_game(player=heroes["player"], enemy=heroes["enemy"])  # type: ignore
    return render_template("fight.html", heroes=heroes, result="Бой начался")


@app.route("/hit/")
def hit() -> str:
    """ Кнопка нанесения удара """

    if arena.game_is_running:
        result = arena.player_hit()
    else:
        result = arena.result
    return render_template("fight.html", heroes=heroes, result=result)


@app.route("/use-skill/")
def use_skill() -> str:
    """ Кнопка использования умения """

    if arena.game_is_running:
        result = arena.player_use_skill()
    else:
        result = arena.result
    return render_template("fight.html", heroes=heroes, result=result)


@app.route("/pass-turn/")
def pass_turn() -> str:
    """ Кнопка пропуска хода """

    if arena.game_is_running:
        result = arena.next_turn()
    else:
        result = arena.result
    return render_template("fight.html", heroes=heroes, result=result)


@app.route("/end-fight/")
def end_fight() -> Response:
    """ Кнопка завершения игры """

    return redirect(url_for("main_bp.menu_page"))
