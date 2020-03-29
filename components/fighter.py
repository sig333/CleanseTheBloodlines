import tcod as libtcod

from game_messages import Message

from random_utils import sigmoid_randint


class Fighter:
    def __init__(self, hp, defense, strength, dexterity, xp=0):
        self.base_max_hp = hp
        self.hp = hp
        self.base_defense = defense
        self.base_strength = strength
        self.base_dexterity = dexterity
        self.xp = xp

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

    def attack(self, target):
        results = []

        damage = self.power - target.fighter.defense

        if self.owner.equipment:
            if self.owner.equipment.accuracy == 0:
                accuracy = 80
            else:
                accuracy = self.owner.equipment.accuracy
        else:
            accuracy = 80

        if sigmoid_randint() < self.dexterity * 2 + accuracy:
            if damage > 0:
                results.append({'message': Message('{0} attacks {1} for {2} hit points.'.format(
                    self.owner.name.capitalize(), target.name, str(damage)), libtcod.white)})
                results.extend(target.fighter.take_damage(damage))
            else:
                results.append({'message': Message('{0} attacks {1} but does no damage.'.format(
                    self.owner.name.capitalize(), target.name), libtcod.white)})
        else:
            results.append({'message': Message('{0} attacks {1} but misses.'.format(
                self.owner.name.capitalize(), target.name), libtcod.white)})

        return results
