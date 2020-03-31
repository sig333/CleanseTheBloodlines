class Equippable:
    def __init__(self, slot, power_bonus=0, defense_bonus=0, max_hp_bonus=0, dexterity_bonus=0, accuracy=0,
                 melee_range=1):
        self.slot = slot
        self.power_bonus = power_bonus
        self.defense_bonus = defense_bonus
        self.max_hp_bonus = max_hp_bonus
        self.dexterity_bonus = dexterity_bonus
        self.accuracy = accuracy
        self.melee_range = melee_range
