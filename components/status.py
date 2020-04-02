import tcod as libtcod

from game_messages import Message
from numpy import floor


class PoisonedStatus:
    def __init__(self, previous_status, percent_damage=.1, turns=5):
        self.previous_status = previous_status
        self.percent_damage = percent_damage
        self.turns = turns

    def status(self):
        results = []

        damage = floor(self.owner.fighter.max_hp * self.percent_damage)

        if self.owner.fighter.hp - damage < 1:
            self.owner.fighter.hp = 1
            results.append({'message': Message('{0} nearly dies from poison!'.format(
                self.owner.name.capitalize()), libtcod.green)})
        else:
            results.extend(self.owner.fighter.take_damage(damage))
            results.append({'message': Message('{0} takes {1} damage from poison.'.format(
                self.owner.name.capitalize(), str(int(damage))), libtcod.green)})

        self.turns -= 1
        if self.turns == 0:
            self.owner.status = self.previous_status
            results.append({'message': Message('{0} recovers from poison.'.format(
                self.owner.name.capitalize()), libtcod.red)})

        return results

    def refresh(self, turns):
        self.turns += turns
