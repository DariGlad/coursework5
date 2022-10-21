from flask import Blueprint, request, render_template, redirect, url_for
from werkzeug import Response

from app.classes.heroes import PlayerUnit, unit_classes, EnemyUnit
from app.container import forms_create_units, equipment, heroes

app = Blueprint("choose_bp", __name__)


@app.route("/choose-hero/", methods=['post', 'get'])
def choose_hero() -> Response | str:
    """ Выбор героя """

    if request.method == "GET":
        forms_create_units["header"] = "Выберите героя"
        return render_template("hero_choosing.html", result=forms_create_units)
    if request.method == "POST":
        name = request.form["name"]
        unit_class = request.form["unit_class"]
        armor = request.form["armor"]
        weapon = request.form["weapon"]
        player = PlayerUnit(name=name, unit_class=unit_classes[unit_class])
        player.equip_weapon(equipment.get_weapon(weapon))
        player.equip_armor(equipment.get_armor(armor))
        heroes["player"] = player  # type: ignore
        return redirect(url_for("choose_bp.choose_enemy"))


@app.route("/choose-enemy/", methods=['post', 'get'])
def choose_enemy() -> Response | str:
    """ Выбор противника """

    if request.method == "GET":
        forms_create_units["header"] = "Выберите противника"
        return render_template("hero_choosing.html", result=forms_create_units)
    if request.method == "POST":
        name = request.form["name"]
        unit_class = request.form["unit_class"]
        armor = request.form["armor"]
        weapon = request.form["weapon"]
        enemy = EnemyUnit(name=name, unit_class=unit_classes[unit_class])
        enemy.equip_weapon(equipment.get_weapon(weapon))
        enemy.equip_armor(equipment.get_armor(armor))
        heroes["enemy"] = enemy  # type: ignore
        return redirect(url_for("fight_bp.start_fight"))
