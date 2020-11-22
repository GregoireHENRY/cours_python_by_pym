"""
Xmas tree field.
"""

import math
import random
from operator import itemgetter


def main():
    """main"""
    # initialization
    width = 20
    height = 20
    borders = [4, 4, 5, 1]  # to ensure tree inside field borders
    tree = ["^", "^ ^", "(o  )", "(o  o )", "U"]
    # create field with borders
    field = [
        ["#" if (j in (0, width - 1) or i in (0, height - 1)) else " " for j in range(width)]
        for i in range(height)
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
        zip(
            random.sample(range(borders[0], width - borders[1]), number_trees),
            random.sample(range(borders[2], height - borders[3]), number_trees),
        )
    )
    # sort places by height for overlapping perspective
    sorted(tree_places, key=itemgetter(1))

    # plant trees
    for place_x, place_y in tree_places:
        field[place_y - 0][place_x - 0 : place_x + 1] = tree[-1]
        field[place_y - 1][place_x - 3 : place_x + 4] = tree[-2]
        field[place_y - 2][place_x - 2 : place_x + 3] = tree[-3]
        field[place_y - 3][place_x - 1 : place_x + 2] = tree[-4]
        field[place_y - 4][place_x - 0 : place_x + 1] = tree[-5]

    # show the world your Xmas tree field
    for line in field:
        print("".join(line))


if __name__ == "__main__":
    main()
