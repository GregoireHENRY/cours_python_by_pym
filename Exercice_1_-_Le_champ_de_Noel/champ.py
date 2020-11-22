#!/usr/bin/env python3
"""
Xmas field of trees.

A short program that generates a field WIDTH a random numbers of pretty trees, just like this one:
   ^
  ^ ^
 (o  )
(o  o )
   U

The field is delimited with the symbol `#`.
The program handles perspective, showing trees "at the bottom" in front of the other trees.
"""

import math
import random
from operator import itemgetter

# minimum WIDTH and HEIGHT of 12 is adviced
WIDTH = 20
HEIGHT = 20
X_LIMITS = (0, WIDTH - 1)
Y_LIMITS = (0, HEIGHT - 1)
PROTECTION_SPAWN_LEFT = 4
PROTECTION_SPAWN_RIGHT = 4
PROTECTION_SPAWN_TOP = 1
PROTECTION_SPAWN_BOTTOM = 5
MINIMUM_TREES = 1
BORDER_CHAR = "#"
EMPTY_CHAR = " "
TREE_DESIGN = ["^", "^ ^", "(o  )", "(o  o )", "U"]


def main():
    # initialization
    # create field with BORDERS
    field = [
        [BORDER_CHAR if (j in X_LIMITS or i in Y_LIMITS) else EMPTY_CHAR for j in range(WIDTH)]
        for i in range(HEIGHT)
    ]

    # TODO:
    # + colored trees
    # + add more field designs (circle, diamond, random)
    # + add more tree design
    # + input fixed size as parameters

    # empiric max number of trees for the sake of visibility
    max_tree_for_field = math.ceil((width * height) ** (1 / 2) / 4)
    # get random number of trees at random places
    number_trees = random.randint(1, max_tree_for_field)
    tree_places = list(
    number_trees = random.randint(MINIMUM_TREES, max_tree_for_field)
    # list of coordinates as tuple (x, y) to plant trees
    tree_positions = list(
        zip(
            random.sample(
                range(PROTECTION_SPAWN_LEFT, WIDTH - PROTECTION_SPAWN_RIGHT), number_trees
            ),
            random.sample(
                range(PROTECTION_SPAWN_BOTTOM, HEIGHT - PROTECTION_SPAWN_TOP), number_trees
            ),
        )
    )
    # sort places by height for overlapping perspective
    sorted(tree_places, key=itemgetter(1))

    # plant trees
    for position_x, position_y in tree_positions:
        for index_line, tree_line in enumerate(TREE_DESIGN[::-1]):
            half_width_tree = int(len(tree_line) / 2)
            # replace field symbols at current field line from -half_width_tree to
            #  half_width_tree + 1 around the x position of the trunk
            field[position_y - index_line][
                position_x - half_width_tree : position_x + half_width_tree + 1
            ] = tree_line

    # show the world your Xmas tree field
    for line in field:
        print("".join(line))


if __name__ == "__main__":
    main()
