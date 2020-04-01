from random import randint


def from_dungeon_level(table, dungeon_level):
    for (value, level) in reversed(table):
        if dungeon_level >= level:
            return value

    return 0


def random_choice_index(chances):
    random_chance = randint(1, sum(chances))

    running_sum = 0
    choice = 0
    for w in chances:
        running_sum += w

        if random_chance <= running_sum:
            return choice
        choice += 1


def random_choice_from_dict(choice_dict):
    choices = list(choice_dict.keys())
    chances = list(choice_dict.values())

    return choices[random_choice_index(chances)]


def sigmoid_randint():
    return (randint(1, 100) + randint(1, 100))/2


def rn2(x):
    return randint(0, x-1)


def rne(x, truncation=3):  # Thanks to Dr. Lilian Besson for the implementation
    truncation = max(truncation, 1)
    tmp = 1
    while tmp < truncation and rn2(x) == 0:
        tmp += 1
    return tmp
