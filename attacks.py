import tcod as libtcod

from game_messages import Message

from random_utils import sigmoid_randint, rne

from components.ai import StunnedMonster
from components.status import PoisonedStatus


def melee_attack(self, target):
    results = []

    damage = self.power - target.fighter.defense

    accuracy = self.dexterity * 2 + self.owner.equipment.accuracy

    if sigmoid_randint() < accuracy:
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


def unarmed_attack(self, target):
    results = []

    damage = self.power - target.fighter.defense
    accuracy = self.dexterity * 5 + 50

    if sigmoid_randint() < accuracy:
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


def polearm_attack(self, target):
    results = []

    target.status = PoisonedStatus(previous_status=target.status)
    target.status.owner = target

    damage = self.power - target.fighter.defense

    if self.owner.distance(target.x, target.y) == 2:
        accuracy = self.dexterity * 2 + self.owner.equipment.accuracy
    else:
        accuracy = self.dexterity * 2 + self.owner.equipment.accuracy - 20

    stun_chance = self.dexterity * 2 + 20

    if sigmoid_randint() < accuracy:
        if damage > 0:
            results.append({'message': Message('{0} attacks {1} for {2} hit points.'.format(
                self.owner.name.capitalize(), target.name, str(damage)), libtcod.white)})
            results.extend(target.fighter.take_damage(damage))

            if sigmoid_randint() < stun_chance and target.fighter.hp - damage > 0:
                confused_ai = StunnedMonster(target.ai, rne(1, 3))

                confused_ai.owner = target
                target.ai = confused_ai

                results.append({'message': Message(
                    'A knockout blow! {0} looks stunned.'.format(target.name), libtcod.light_green)})
        else:
            results.append({'message': Message('{0} attacks {1} but does no damage.'.format(
                self.owner.name.capitalize(), target.name), libtcod.white)})
    else:
        results.append({'message': Message('{0} attacks {1} but misses.'.format(
            self.owner.name.capitalize(), target.name), libtcod.white)})
    return results
