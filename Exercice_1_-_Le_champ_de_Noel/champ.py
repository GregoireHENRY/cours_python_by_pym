"""
Xmas tree field.
"""


def main():
    """main"""
    # initialization
    width = 20
    height = 20
    tree = ["^", "^ ^", "(o  )", "(o  o )", "U"]
    # create field with borders
    field = [
        ["#" if (j in (0, width - 1) or i in (0, height - 1)) else " " for j in range(width)]
        for i in range(height)
    ]

    # TODO:
    # + get a single random place
    # + place only tree trunks
    # + place trees wholy
    # + get several random places
    # + do perspective (sort by height?)

    # show the world your Xmas tree field
    for line in field:
        print("".join(line))


if __name__ == "__main__":
    main()
