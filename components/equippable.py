from attacks import melee_attack

from components.equipment_slots import EquipmentSlots


class Equippable:
    def __init__(self, slot, power_bonus=0, defense_bonus=0, max_hp_bonus=0, dexterity_bonus=0, accuracy=0,
                 melee_range=1, attack=None):
        self.slot = slot
        self.power_bonus = power_bonus
        self.defense_bonus = defense_bonus
        self.max_hp_bonus = max_hp_bonus
        self.dexterity_bonus = dexterity_bonus
        self.accuracy = accuracy
        self.melee_range = melee_range
        if attack:
            self.attack = attack
        elif not attack and self.slot == EquipmentSlots.MAIN_HAND:
            self.attack = melee_attack
        else:
            self.attack = None
