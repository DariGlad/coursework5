from app.classes.skills.skills import Skill


class FuryPunch(Skill):
    name = "Свирепый пинок"
    stamina = 6
    damage = 12

    def skill_effect(self) -> str:
        """ Расчёт нанесённого урона умения и расхода выносливости """

        self.target.get_damage(self.damage)
        self.user.stamina -= self.stamina
        return f"{self.user.name} используют {self.name} и наносит {self.damage} урона сопернику."
