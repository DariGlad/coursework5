from dataclasses import dataclass
from typing import List
from random import uniform
import marshmallow_dataclass
import marshmallow
import json

from constants import EQUIPMENT_DATA


@dataclass
class Armor:
    id: int
    name: str
    defence: float
    stamina_per_turn: float


@dataclass
class Weapon:
    id: int
    name: str
    min_damage: float
    max_damage: float
    stamina_per_hit: float

    @property
    def damage(self) -> float:
        return round(uniform(self.min_damage, self.max_damage), 1)


@dataclass
class EquipmentData:
    weapons: List[Weapon]
    armors: List[Armor]


class Equipment:

    def __init__(self) -> None:
        self.equipment = self._get_equipment_data()

    def get_weapon(self, weapon_name: str) -> Weapon:
        """ Возвращает объект оружия по имени """

        return next(
            weapon
            for weapon in self.equipment.weapons
            if weapon_name == weapon.name
        )

    def get_armor(self, armor_name: str) -> Armor:
        """ Возвращает объект брони по имени """

        return next(
            armor
            for armor in self.equipment.armors
            if armor_name == armor.name
        )

    def get_weapons_names(self) -> list:
        """ Возвращаем список с оружием """

        return [
            weapon.name
            for weapon in self.equipment.weapons
        ]

    def get_armors_names(self) -> list:
        """ Возвращаем список с броней """

        return [
            armor.name
            for armor in self.equipment.armors
        ]

    @staticmethod
    def _get_equipment_data() -> EquipmentData:
        """ Этот метод загружает json в переменную EquipmentData """

        with open(EQUIPMENT_DATA, encoding="utf-8") as file:
            data = json.load(file)
        equipment_schema = marshmallow_dataclass.class_schema(EquipmentData)
        try:
            return equipment_schema().load(data)
        except marshmallow.exceptions.ValidationError:
            raise ValueError
