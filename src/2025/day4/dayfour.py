import aoc_common


def print_table_box(input_table: list[str], x_x: int, x_y: int):
    y_start = x_y - 1 if x_y > 0 else 0
    y_end = x_y + 1 if x_y < len(input_table)-1 else len(input_table)-1
    x_start = x_x - 1 if x_x > 0 else 0
    x_end = x_x + 1 if x_x < len(input_table[0]) + 1 else len(input_table[0]) + 1

    print("---")
    for y in range(y_start, y_end+1):
        print(input_table[y][x_start:x_end+1])
    print("---")


def count_rolls(input_table: list[str], x_x:int, x_y:int) -> int:
    """
    return the number of rolls in this
    :param input_table: input table
    :param x_x: x location
    :param x_y: y location
    :return: number of
    """

    # print_table_box(input_table, x_x, x_y)
    ret = 0

    y_start = x_y - 1 if x_y > 0 else 0
    y_end = x_y + 2 if x_y+2 <= len(input_table) else len(input_table)
    x_start = x_x - 1 if x_x > 0 else 0
    x_end = x_x + 2 if x_x+2 <= len(input_table[0]) else len(input_table[0])

    for y in range(y_start, y_end):
        l = input_table[y][x_start:x_end]
        # print(l)
        # print(f'({x_x},{x_y}) {y} range: {list(range(x_start, x_end))}, {list(range(y_start, y_end))} ; {ret} ')
        for x in range(x_start, x_end):
            if input_table[y][x] == '@':
                ret += 1
        # print(f'({x_x},{x_y}) {y} range: {list(range(x_start, x_end))}, {list(range(y_start, y_end))} ; {ret} ')

    return ret


def print_table(input_table: list[str], x_x:int = -1, x_y:int = -1) -> None:
    for y in range(len(input_table)):
        if x_y != -1 and x_y == y:
            before = input_table[y][:x_x]
            after = input_table[y][x_x+1:]
            line = before + 'X' + after
        else:
            line = input_table[y]
        print(line)


def remove_roll(input_table, x_x, x_y) -> list[str]:
    updated_table: list[str] = []
    for y in range(len(input_table)):
        if y == x_y:
            before = input_table[y][:x_x]
            after = input_table[y][x_x + 1:]
            line = before + '.' + after
        else:
            line = input_table[y]
        updated_table.append(line)
    # print_table(updated_table)
    return updated_table


def remove_rolls(input_table: list[str], rolls_to_remove: list[(int,int)]):
    updated_table: list[str]= input_table

    for x, y in rolls_to_remove:
        # print(f"removing ({x},{y})")
        updated_table = remove_roll(updated_table, x, y)

    return updated_table


def count_rolls_in_table(input_table, func=count_rolls):
    roll_count = 0
    rolls_to_remove: list[(int,int)] = []
    for y in range(len(input_table)):
        for x in range(len(input_table[y])):
            # print_table(input_table, x, y)
            if input_table[y][x] == '@':
                num_rolls = func(input_table, x, y)

                if num_rolls <= 4:
                    roll_count += 1
                    rolls_to_remove.append((x,y))
                # print(f"num rolls {num_rolls} -- rollcount -- {roll_count}")
            # print("------")
    # print(f"rolls to remove: {rolls_to_remove}")
    updated_table = remove_rolls(input_table, rolls_to_remove)
    return roll_count, updated_table


def count_and_remove_rolls(input_table) -> int:
    tot_rolls_removed = 0
    num_rolls_removed = 999

    curr_table = input_table
    # print_table(curr_table)
    ct = 0
    while num_rolls_removed > 0:
        num_rolls_removed, curr_table = count_rolls_in_table(curr_table)
        # print_table(curr_table)
        print(f"iteration: {ct} num rolls removed {num_rolls_removed}")
        tot_rolls_removed += num_rolls_removed
        ct += 1
    return tot_rolls_removed


def main():
    args = aoc_common.aoc_parse_args()
    input_table = aoc_common.load_input_table(args.inputfile)

    count_part1, _ = count_rolls_in_table(input_table)
    print(f"Part 1: {count_part1}")
    print("============")

    input_table = aoc_common.load_input_table(args.inputfile)
    count_part2 = count_and_remove_rolls(input_table)
    print(f"Part 2: {count_part2}")

if __name__ == "__main__":
    main()
