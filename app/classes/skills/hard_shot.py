from app.classes.skills.skills import Skill


class HardShot(Skill):
    name = "Мощный укол"
    stamina = 5
    damage = 15

    def skill_effect(self) -> str:
        """ Расчёт нанесённого урона умения и расхода выносливости """

        self.target.get_damage(self.damage)
        self.user.stamina -= self.stamina
        return f"{self.user.name} используют {self.name} и наносит {self.damage} урона сопернику."
