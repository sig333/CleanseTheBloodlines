from attacks import unarmed_attack
import types


class Fighter:
    def __init__(self, hp, defense, strength, dexterity, xp=0, attack=unarmed_attack):
        self.base_max_hp = hp
        self.hp = hp
        self.base_defense = defense
        self.base_strength = strength
        self.base_dexterity = dexterity
        self.xp = xp
        self.attack = types.MethodType(attack, self)

    @property
    def max_hp(self):
        if self.owner and self.owner.equipment:
            bonus = self.owner.equipment.max_hp_bonus
        else:
            bonus = 0

        return self.base_max_hp + bonus

    @property
    def power(self):
        if self.owner and self.owner.equipment:
            bonus = self.owner.equipment.power_bonus
        else:
            bonus = 0

        return self.base_strength + bonus

    @property
    def defense(self):
        if self.owner and self.owner.equipment:
            bonus = self.owner.equipment.defense_bonus
        else:
            bonus = 0

        return self.base_defense + bonus

    @property
    def dexterity(self):
        if self.owner and self.owner.equipment:
            bonus = self.owner.equipment.dexterity_bonus
        else:
            bonus = 0

        return self.base_dexterity + bonus

    def take_damage(self, amount):
        results = []

        self.hp -= amount

        if self.hp <= 0:
            results.append({'dead': self.owner, 'xp': self.xp})

        return results

    def heal(self, amount):
        self.hp += amount

        if self.hp > self.max_hp:
            self.hp = self.max_hp

    def set_attack(self, attack):
        self.attack = types.MethodType(attack, self)
