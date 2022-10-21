from app.classes.heroes.unit import BaseUnit


class PlayerUnit(BaseUnit):

    def hit(self, target: BaseUnit) -> str:
        """
        функция удар игрока
        """
        if self.stamina < self.weapon.stamina_per_hit:
            return f"{self.name} попытался использовать {self.weapon.name}, но у него не хватило выносливости."
        damage = self._count_damage(target)
        if damage > 0:
            return f"{self.name} используя {self.weapon.name} пробивает {target.armor.name} соперника и наносит {damage} урона."
        return f"{self.name} используя {self.weapon.name} наносит удар," \
               f" но {target.armor.name} cоперника его останавливает."
