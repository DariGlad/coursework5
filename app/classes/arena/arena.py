from typing import Dict, Any, Optional

from app.classes.heroes import BaseUnit


class BaseSingleton(type):
    _instances: Dict[Any, Any] = {}

    def __call__(cls, *args: Any, **kwargs: Any) -> Dict:
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]


class Arena(metaclass=BaseSingleton):
    STAMINA_PER_ROUND = 1
    player = None
    enemy = None
    game_is_running = False
    result = ""

    def start_game(self, player: BaseUnit, enemy: BaseUnit) -> None:
        """ Начало игры (создаём персонажей, запускаем игру) """

        self.player = player
        self.enemy = enemy
        self.game_is_running = True

    def _check_players_hp(self) -> Optional[str]:
        """ Проверка здоровья """

        if self.player.health_points > 0 and self.enemy.health_points > 0:
            return None
        if self.player.health_points <= 0 and self.enemy.health_points <= 0:
            self.result = "Ничья"
        elif self.player.health_points <= 0:
            self.result = "Поражение"
        else:
            self.result = "Победа"
        return self._end_game()

    def _stamina_regeneration(self) -> None:
        """ Регенирация выносливости """
        units = (
            self.player,
            self.enemy
        )
        for unit in units:
            if unit.stamina + self.STAMINA_PER_ROUND > unit.unit_class.max_stamina:
                unit.stamina = unit.unit_class.max_stamina
            else:
                unit.stamina += self.STAMINA_PER_ROUND

    def next_turn(self) -> Optional[str]:
        """ Следующий ход """

        if self.game_is_running:
            self._stamina_regeneration()
            result = self.enemy.hit(self.player)
            self._check_players_hp()
            return result

    def _end_game(self) -> str:
        """ Завершение игры """

        self._instances: Dict[Any, Any] = {}
        self.game_is_running = False
        return self.result

    def player_hit(self) -> str:
        """ Метод удара игрока """

        player_punch = self.player.hit(self.enemy)
        enemy_punch = self.next_turn()
        return f"{player_punch}<br>{enemy_punch}"

    def player_use_skill(self) -> str:
        """ Использовать умение игрока """

        player_punch = self.player.use_skill(self.enemy)
        enemy_punch = self.next_turn()
        return f"{player_punch}<br>{enemy_punch}"
