from typing import Tuple

import aoc_common

import numpy as np


def load_input_table(inputfile: str) -> Tuple[list[list[int]], list[str]]:
    with open(inputfile, 'r') as f:
        input_table: list[list[int]] = []
        operations: list[str] = []
        for line in f:
            spl = line.strip().split()
            if spl[0] == '+' or spl[0] == '*':
                operations = spl
            else:
                input_table.append([int(x) for x in spl])

    return input_table, operations


def transpose_table(input_table: list[list[int]]) -> list[list[int]]:
    """Transposes a 2D array represented as a list of integ."""
    if not input_table:
        return []

    # Convert the list of strings to a 2D NumPy array of characters
    int_arr = np.array([list(row) for row in input_table])

    # Transpose the array and join characters back into strings
    return [list(row) for row in int_arr.T]


def calculate_table(table_t: list[list[int]], operations: list[str]) -> list[int]:
    ret: list[int] = []
    i = 0
    for row in table_t:
        oper = operations[i]
        if oper == '+':
            ret.append(sum(row))
        elif oper == '*':
            ret.append(np.prod(row))
        i += 1
    return ret


def main():
    args = aoc_common.aoc_parse_args()

    input_table, operations = load_input_table(args.inputfile)
    print(f"operations {operations}")
    print(f"input_table\n{input_table}")
    table_t = transpose_table(input_table)
    print(f"table_t\n{table_t}")
    answers = calculate_table(table_t, operations)
    print(f"answers\n{answers}")
    print(f"PART 1: {sum(answers)}")
    

if __name__ == "__main__":
    main()
