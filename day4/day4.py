
def load_input(filename) -> list[str]:
    with open(filename) as f:
        input:list[list[str]] = []
        for line in f:
            input.append(line.strip())
        return input


def check_xmas(input: list[str], x_x:int, x_y:int) -> int:
    """
    given an X, check in all directions if XMAS is in the arr.
    :param input: 2-d array of the input
    :param x_x: x coordinate of X
    :param x_y: y coordinate of X
    :return: number of times XMAS is found for this X
    """
    ret = 0
    # check normal along X

    if x_x + 3 < len(input[x_y]) and input[x_y][x_x + 1] == 'M':
        if input[x_y][x_x + 2] == 'A':
            if input[x_y][x_x + 3] == 'S':
                print(f"{x_x, x_y} 01 Along X {input[x_y][x_x:x_x + 4]}")
                ret += 1
                # return True

    # along Y down
    if x_y + 3 < len(input) and input[x_y + 1][x_x] == 'M':
        if input[x_y + 2][x_x] == 'A':
            if input[x_y + 3][x_x] == 'S':
                print(f"{x_x, x_y} 02 Along Y ")  #{input[x_y:x_y + 3][x_x]}
                ret += 1
                # return True

    # along X backward
    if x_x >= 3 and input[x_y][x_x - 1] == 'M':
        if input[x_y][x_x - 2] == 'A':
            if input[x_y][x_x - 3] == 'S':
                print(f"{x_x, x_y} 03 X backward")
                ret += 1
                # return True

    # along Y up
    if x_y >= 3 and input[x_y - 1][x_x] == 'M':
        if input[x_y - 2][x_x] == 'A':
            if input[x_y - 3][x_x] == 'S':
                print(f"{x_x, x_y} 04 Y UP ")
                ret += 1
                # return True

    # diag down right
    if (x_x + 3 < len(input[x_y]) and x_y + 3 < len(input) and
            input[x_y + 1][x_x + 1] == 'M'):
        if input[x_y + 2][x_x + 2] == 'A':
            if input[x_y + 3][x_x + 3] == 'S':
                print(f"{x_x, x_y} 05 diag down right")
                ret += 1
                # return True

    # diag up right
    if (x_y >= 3 and x_x + 3 < len(input[x_y]) and
            input[x_y - 1][x_x + 1] == 'M'):
        if input[x_y - 2][x_x + 2] == 'A':
            if input[x_y - 3][x_x + 3] == 'S':
                print(f"{x_x, x_y} 06 diag UP right")
                ret += 1
                # return True

    # diag up left and x_x + 3 < len(input[x_y]) and x_y + 3 < len(input)
    if (x_x >= 3 and x_y >= 3 and
            input[x_y - 1][x_x - 1] == 'M'):
        if input[x_y - 2][x_x - 2] == 'A':
            if input[x_y - 3][x_x - 3] == 'S':
                print(f"{x_x, x_y} 07 diag UP left")
                ret += 1
                # return True

    # diag down left
    if (x_x >= 3 and x_y + 3 < len(input) and
            input[x_y + 1][x_x - 1] == 'M'):
        if input[x_y + 2][x_x - 2] == 'A':
            if input[x_y + 3][x_x - 3] == 'S':
                print(f"{x_x, x_y} 08 diag DOWN left")
                ret += 1
                # return True

    return ret


def check_x_mas(input_table: list[str], x_x:int, x_y:int) -> int:
    """
    given an X, check in all directions if MAS in the shape of an X is in the arr.
    M.S
    .A.
    M.S
    :param input_table:
    :param x_x: x coordinate of M in upper left
    :param x_y: y coordinate of M in upper left
    :return:
    """
    ret = 0
    if x_y + 2 < len(input_table) and x_x + 2 < len(input_table[x_y]) and \
            input_table[x_y][x_x] == 'M' and input_table[x_y][x_x + 2] == 'S' and \
            input_table[x_y + 1][x_x + 1] == 'A' and \
            input_table[x_y + 2][x_x] == 'M' and input_table[x_y + 2][x_x + 2] == 'S':
        print(f"{x_x, x_y} 01 MAS")
        ret += 1

    if x_x > 2 and \
            x_y + 2 < len(input_table) and \
            input_table[x_y][x_x] == 'M' and input_table[x_y][x_x - 2] == 'S' and \
            input_table[x_y + 1][x_x - 1] == 'A' and \
            input_table[x_y + 2][x_x] == 'M' and input_table[x_y + 2][x_x - 2] == 'S':
        print(f"{x_x, x_y} 02 MAS backward")
        ret += 1

    if x_y > 2 and \
            x_x + 2 < len(input_table[x_y]) and \
            input_table[x_y][x_x] == 'M' and input_table[x_y][x_x + 2] == 'M' and \
            input_table[x_y - 1][x_x + 1] == 'A' and \
            input_table[x_y - 2][x_x] == 'S' and input_table[x_y - 2][x_x + 2] == 'S':
        print(f"{x_x, x_y} 02 MAS UP")
        ret += 1

    # x_x + 2 < len(input_table[x_y]) and\
    if x_x > 2 and x_y > 2 and \
            input_table[x_y][x_x] == 'M' and input_table[x_y][x_x - 2] == 'M' and \
            input_table[x_y - 1][x_x - 1] == 'A' and \
            input_table[x_y - 2][x_x] == 'S' and input_table[x_y - 2][x_x - 2] == 'S':
        print(f"{x_x, x_y} 02 MAS UP BACKWARD")
        ret += 1

    return ret


def count_xmas(input_table: list[str], letter='X', func=check_xmas) -> int:
    num_xmas = 0
    for y in range(len(input_table)):
        for x in range(len(input_table[y])):
            if input_table[y][x] == letter :
                num_xmas += func(input_table, x, y)

    return num_xmas


def main():
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("inputfile", type=str, help="path to input file")
    args = parser.parse_args()
    input_table = load_input(args.inputfile)
    num_xmas = count_xmas(input_table)
    print(f"Number of XMAS: {num_xmas}")

    num_xmas = count_xmas(input_table, letter='M', func=check_x_mas)
    print(f"Number of X-MAS: {num_xmas}")



if __name__ == "__main__":
    main()