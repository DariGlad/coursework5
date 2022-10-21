from random import randint

from app.classes.heroes.unit import BaseUnit


class EnemyUnit(BaseUnit):

    def hit(self, target: BaseUnit) -> str:
        """
        функция удар противника
        """
        if not self._is_skill_used and self.stamina >= self.unit_class.skill.stamina and randint(0, 100) < 15:
            return self.use_skill(target)

        if self.stamina < self.weapon.stamina_per_hit:
            return f"{self.name} попытался использовать {self.weapon.name}, но у него не хватило выносливости."

        damage = self._count_damage(target)

        if damage > 0:
            return f"{self.name} используя {self.weapon.name} пробивает {target.armor.name} соперника " \
                   f"и наносит {damage} урона."

        return f"{self.name} используя {self.weapon.name} наносит удар," \
               f" но {target.armor.name} cоперника его останавливает."
