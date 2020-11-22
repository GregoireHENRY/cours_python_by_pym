"""
Xmas tree field.
"""

import random


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
    # + place trees wholy
    # + get several random places
    # + do perspective (sort by height?)

    number_trees = 1
    tree_places = list(
        zip(
            random.sample(range(borders[0], width - borders[1]), number_trees),
            random.sample(range(borders[2], height - borders[3]), number_trees),
        )
    )

    # plant trees
    for place_x, place_y in tree_places:
        field[place_y][place_x] = tree[-1]

    # show the world your Xmas tree field
    for line in field:
        print("".join(line))


if __name__ == "__main__":
    main()
