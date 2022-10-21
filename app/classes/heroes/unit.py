from __future__ import annotations
from abc import ABC, abstractmethod
from app.classes.equipment.equipment import Weapon, Armor
from app.classes.heroes.classes import UnitClass
from typing import Type


class BaseUnit(ABC):
    """
    Базовый класс юнита
    """

    def __init__(self, name: str, unit_class: UnitClass):
        """
        При инициализации класса Unit используем свойства класса UnitClass
        """
        self.name: str = name
        self.unit_class: UnitClass = unit_class
        self.hp: float = unit_class.max_health
        self.stamina: float = unit_class.max_stamina
        self.weapon: Weapon = Type[Weapon]
        self.armor: Armor = Type[Armor]
        self._is_skill_used: bool = False

    @property
    def health_points(self) -> float:
        return round(self.hp, 1)

    @property
    def stamina_points(self) -> float:
        return round(self.stamina, 1)

    def equip_weapon(self, weapon: Weapon) -> str:
        """ Присваиваем герою новое оружие"""
        self.weapon = weapon
        return f"{self.name} экипирован оружием {self.weapon.name}"

    def equip_armor(self, armor: Armor) -> str:
        """ Одеваем новую броню """
        self.armor = armor
        return f"{self.name} экипирован броней {self.weapon.name}"

    def _count_damage(self, target: BaseUnit) -> float:
        """ Метод расчёта нанесённого, полученного урона,
        и затраченной выносливости """
        self.stamina -= self.weapon.stamina_per_hit
        damage = self.unit_class.attack * self.weapon.damage
        target_stamina = target.armor.stamina_per_turn * target.unit_class.stamina
        if target.stamina > target_stamina:
            damage -= target.armor.defence * target.unit_class.armor
            target.stamina -= target_stamina
        damage = round(damage, 1)
        target.get_damage(damage)
        return damage

    def get_damage(self, damage: float) -> None:
        """ Получение урона целью """
        if damage > 0:
            self.hp -= damage
            if self.hp < 0:
                self.hp = 0

    @abstractmethod
    def hit(self, target: BaseUnit) -> str:
        pass

    def use_skill(self, target: BaseUnit) -> str:
        """ метод использования умения."""
        if self._is_skill_used:
            return "Навык уже использован"

        self._is_skill_used = True
        return self.unit_class.skill.use(self, target)
