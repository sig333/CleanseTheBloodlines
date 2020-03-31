import tcod as libtcod

from game_messages import Message

from random_utils import sigmoid_randint


def melee_attack(self, target):
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


# def unarmed_attack:
#     results = []
#
#     damage = self.power - target.fighter.defense