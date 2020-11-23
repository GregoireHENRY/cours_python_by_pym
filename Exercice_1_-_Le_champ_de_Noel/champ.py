#!/usr/bin/env python3
"""
Xmas field of trees.

A short program that generates a field with a random numbers of pretty trees, just like this one:
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
PLANTABLE_REGION_LIMITS_HORIZONTAL = (PROTECTION_SPAWN_LEFT, WIDTH - PROTECTION_SPAWN_RIGHT)
PLANTABLE_REGION_LIMTIS_VERTICAL = (PROTECTION_SPAWN_BOTTOM, HEIGHT - PROTECTION_SPAWN_TOP)
MINIMUM_TREES = 1
BORDER_CHAR = "#"
EMPTY_CHAR = " "
TREE_DESIGN = ["^", "^ ^", "(o  )", "(o  o )", "U"]


def main():
    # initialization
    # create field with borders
    field = [
        [BORDER_CHAR if (x in X_LIMITS or y in Y_LIMITS) else EMPTY_CHAR for x in range(WIDTH)]
        for y in range(HEIGHT)
    ]

    # empiric max number of trees for the sake of visibility
    # WIDTH and HEIGHT sizes contribute to the number of trees
    max_tree_for_field = math.ceil((WIDTH * HEIGHT) ** (1 / 2) / 4)
    number_trees = random.randint(MINIMUM_TREES, max_tree_for_field)

    # get number_trees random positions in the field (excluded the border protection area)
    # list of y positions are sorted to handle perspective by planting them from top to bottom
    tree_positions_x = random.sample(range(*PLANTABLE_REGION_LIMITS_HORIZONTAL), number_trees)
    tree_positions_y = sorted(random.sample(range(*PLANTABLE_REGION_LIMTIS_VERTICAL), number_trees))

    # plant trees from top to bottom
    for position_x, position_y in zip(tree_positions_x, tree_positions_y):
        # plant each tree from truc to crown
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
