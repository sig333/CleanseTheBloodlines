from random_utils import sigmoid_randint


class Level:
    def __init__(self, current_level=1, current_xp=0, level_up_base=200, level_up_factor=150, hp_growth=0,
                 defense_growth=0, strength_growth=0, dexterity_growth=0):
        self.current_level = current_level
        self.current_xp = current_xp
        self.level_up_base = level_up_base
        self.level_up_factor = level_up_factor
        self.hp_growth = hp_growth
        self.defense_growth = defense_growth
        self.strength_growth = strength_growth
        self.dexterity_growth = dexterity_growth
        self.latest_hp = 0
        self.latest_defense = 0
        self.latest_strength = 0
        self.latest_dexterity = 0

    @property
    def experience_to_next_level(self):
        return self.level_up_base + self.current_level * self.level_up_factor

    def add_xp(self, xp):
        self.current_xp += xp

        if self.current_xp > self.experience_to_next_level:
            self.current_xp -= self.experience_to_next_level
            self.current_level += 1

            hp_increment = self.hp_growth // 100  # Initializes it and covers for when growth > 99
            if sigmoid_randint() <= self.hp_growth:
                hp_increment += 1
            self.owner.fighter.base_max_hp += hp_increment
            self.owner.fighter.hp += hp_increment
            self.latest_hp = hp_increment

            defense_increment = self.defense_growth // 100  # Initializes it and covers for when growth > 99
            if sigmoid_randint() <= self.defense_growth:
                defense_increment += 1
            self.owner.fighter.base_defense += defense_increment
            self.latest_defense = defense_increment

            strength_increment = self.strength_growth // 100  # Initializes it and covers for when growth > 99
            if sigmoid_randint() <= self.strength_growth:
                strength_increment += 1
            self.owner.fighter.base_strength += strength_increment
            self.latest_strength = strength_increment

            dexterity_increment = self.dexterity_growth // 100  # Initializes it and covers for when growth > 99
            if sigmoid_randint() <= self.dexterity_growth:
                dexterity_increment += 1
            self.owner.fighter.base_dexterity += dexterity_increment
            self.latest_dexterity = dexterity_increment

            return True
        else:
            return False
