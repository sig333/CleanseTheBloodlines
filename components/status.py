import tcod as libtcod

from game_messages import Message


class PoisonedStatus:
    def __init__(self, percent_damage = .2, turns = 10):
        self.percent_damage = percent_damage
        self.turns = turns

    def status(self):
        results = []

        damage = self.owner.fighter.max_hp * self.percent_damage

        if self.owner.fighter.hp - damage > 1:
            self.owner.fighter.hp = 1
            results.append({'message': Message('{0} nearly dies from poison!'.format(
                self.owner.name.capitalize()), libtcod.red)})
        else:
            results.extend(self.owner.fighter.take_damage(damage))

        return results
