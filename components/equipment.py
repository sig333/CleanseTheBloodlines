from components.equipment_slots import EquipmentSlots
from attacks import unarmed_attack
import types


class Equipment:
    def __init__(self, main_hand=None, off_hand=None, chest=None, head=None, gloves=None, feet=None):
        self.main_hand = main_hand
        self.off_hand = off_hand
        self.chest = chest
        self.head = head
        self.gloves = gloves
        self.feet = feet

    @property
    def max_hp_bonus(self):
        bonus = 0

        if self.main_hand and self.main_hand.equippable:
            bonus += self.main_hand.equippable.max_hp_bonus
        if self.off_hand and self.off_hand.equippable:
            bonus += self.off_hand.equippable.max_hp_bonus
        if self.chest and self.chest.equippable:
            bonus += self.chest.equippable.max_hp_bonus
        if self.head and self.head.equippable:
            bonus += self.head.equippable.max_hp_bonus
        if self.gloves and self.gloves.equippable:
            bonus += self.gloves.equippable.max_hp_bonus
        if self.feet and self.feet.equippable:
            bonus += self.feet.equippable.max_hp_bonus

        return bonus

    @property
    def power_bonus(self):
        bonus = 0

        if self.main_hand and self.main_hand.equippable:
            bonus += self.main_hand.equippable.power_bonus
        if self.off_hand and self.off_hand.equippable:
            bonus += self.off_hand.equippable.power_bonus
        if self.chest and self.chest.equippable:
            bonus += self.chest.equippable.power_bonus
        if self.head and self.head.equippable:
            bonus += self.head.equippable.power_bonus
        if self.gloves and self.gloves.equippable:
            bonus += self.gloves.equippable.power_bonus
        if self.feet and self.feet.equippable:
            bonus += self.feet.equippable.power_bonus

        return bonus

    @property
    def defense_bonus(self):
        bonus = 0

        if self.main_hand and self.main_hand.equippable:
            bonus += self.main_hand.equippable.defense_bonus
        if self.off_hand and self.off_hand.equippable:
            bonus += self.off_hand.equippable.defense_bonus
        if self.chest and self.chest.equippable:
            bonus += self.chest.equippable.defense_bonus
        if self.head and self.head.equippable:
            bonus += self.head.equippable.defense_bonus
        if self.gloves and self.gloves.equippable:
            bonus += self.gloves.equippable.defense_bonus
        if self.feet and self.feet.equippable:
            bonus += self.feet.equippable.defense_bonus

        return bonus

    @property
    def dexterity_bonus(self):
        bonus = 0

        if self.main_hand and self.main_hand.equippable:
            bonus += self.main_hand.equippable.dexterity_bonus
        if self.off_hand and self.off_hand.equippable:
            bonus += self.off_hand.equippable.dexterity_bonus
        if self.chest and self.chest.equippable:
            bonus += self.chest.equippable.dexterity_bonus
        if self.head and self.head.equippable:
            bonus += self.head.equippable.dexterity_bonus
        if self.gloves and self.gloves.equippable:
            bonus += self.gloves.equippable.dexterity_bonus
        if self.feet and self.feet.equippable:
            bonus += self.feet.equippable.dexterity_bonus

        return bonus

    @property
    def accuracy(self):
        bonus = 0

        if self.main_hand and self.main_hand.equippable:
            bonus += self.main_hand.equippable.accuracy
        if self.off_hand and self.off_hand.equippable:
            bonus += self.off_hand.equippable.accuracy
        if self.chest and self.chest.equippable:
            bonus += self.chest.equippable.accuracy
        if self.head and self.head.equippable:
            bonus += self.head.equippable.accuracy
        if self.gloves and self.gloves.equippable:
            bonus += self.gloves.equippable.accuracy
        if self.feet and self.feet.equippable:
            bonus += self.feet.equippable.accuracy

        return bonus

    def toggle_equip(self, equippable_entity):
        results = []

        slot = equippable_entity.equippable.slot

        if slot == EquipmentSlots.MAIN_HAND:
            if self.main_hand == equippable_entity:
                self.main_hand = None
                results.append({'dequipped': equippable_entity})
                self.owner.fighter.set_attack(unarmed_attack)
            else:
                if self.main_hand:
                    results.append({'dequipped': self.main_hand})
                    self.owner.fighter.set_attack(unarmed_attack)

                self.main_hand = equippable_entity
                results.append({'equipped': equippable_entity})
                self.owner.fighter.set_attack(equippable_entity.equippable.attack)
        elif slot == EquipmentSlots.OFF_HAND:
            if self.off_hand == equippable_entity:
                self.off_hand = None
                results.append({'dequipped': equippable_entity})
            else:
                if self.off_hand:
                    results.append({'dequipped': self.off_hand})

                self.off_hand = equippable_entity
                results.append({'equipped': equippable_entity})
        elif slot == EquipmentSlots.CHEST:
            if self.off_hand == equippable_entity:
                self.off_hand = None
                results.append({'dequipped': equippable_entity})
            else:
                if self.off_hand:
                    results.append({'dequipped': self.off_hand})

                self.off_hand = equippable_entity
                results.append({'equipped': equippable_entity})
        elif slot == EquipmentSlots.HEAD:
            if self.off_hand == equippable_entity:
                self.off_hand = None
                results.append({'dequipped': equippable_entity})
            else:
                if self.off_hand:
                    results.append({'dequipped': self.off_hand})

                self.off_hand = equippable_entity
                results.append({'equipped': equippable_entity})
        elif slot == EquipmentSlots.GLOVES:
            if self.off_hand == equippable_entity:
                self.off_hand = None
                results.append({'dequipped': equippable_entity})
            else:
                if self.off_hand:
                    results.append({'dequipped': self.off_hand})

                self.off_hand = equippable_entity
                results.append({'equipped': equippable_entity})
        elif slot == EquipmentSlots.FEET:
            if self.feet == equippable_entity:
                self.off_hand = None
                results.append({'dequipped': equippable_entity})
            else:
                if self.off_hand:
                    results.append({'dequipped': self.off_hand})

                self.off_hand = equippable_entity
                results.append({'equipped': equippable_entity})

        return results
