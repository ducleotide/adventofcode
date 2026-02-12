import re

def load_input(filename):
    with open(filename) as f:
        ret = []
        for line in f:
            ret.append(line)
        return ret


def apply_mult(mult_str: str) -> int:
    split_str = mult_str.split(',')
    n1 = int(split_str[0].strip('mul('))
    n2 = int(split_str[1].strip(')'))
    return n1 * n2


def find_mul(lines: list[str], func, filter_func) -> list[list[int]]:
    mult_pats_lines:list[list[int]] = []

    for line in lines:
        print(f"line [==={line}===]")
        mult = func(line)
        if filter_func:
            mult = filter_func(mult)
        print(f"mult [==={mult}===]")
        mult_pats_lines.append(mult)
    return mult_pats_lines


def parse_pattern(line) -> list[int]:
    pat = re.compile("mul\\([0-9]*,[0-9]*\\)", re.UNICODE)
    x = re.findall(pat, line)
    # print(f"patterns = {x}")
    return x


def sum_total_mult_nums(mult_pats_lines: list[list[int]]) -> int:
    sum_total = 0
    for mult_num in mult_pats_lines:
        mult = list(map(apply_mult, mult_num))
        sum_line = sum(mult)
        print(f'sum {mult} = {sum_line}')
        sum_total += sum(mult)
    return sum_total


def parse_pattern_part2(line: str) -> list[str]:
    # regex include do() and don't()
    pat2 = re.compile("mul\\([0-9]*,[0-9]*\\)|do\\(\\)|don\'t\\(\\)", re.UNICODE)
    x = re.findall(pat2, line)
    # print(f"pattern2 = {x}")
    return x


def filter_pattern2(pat_list: list[str]) -> list[str]:
    # filter between don'ts and dos
    enabled = True
    ret_list: list[str] = []
    for elem in pat_list:
        if "don't()" == elem:
            enabled = False
        elif "do()" == elem:
            enabled = True
        else:
            if enabled:
                ret_list.append(elem)
    return ret_list


def main():
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument('input', help='path to input file')
    args = parser.parse_args()

    lines = load_input(args.input)

    mult_nums = find_mul(lines, parse_pattern, None)
    sum_total = sum_total_mult_nums(mult_nums)
    print(f"part one = {sum_total}")

    # --- part two ---
    ## joined lines
    input_line = ''.join(lines)
    parsed_input = parse_pattern_part2(input_line)
    filter_nums = filter_pattern2(parsed_input)
    mult_nums = list(map(apply_mult, filter_nums))
    sum_total = sum(mult_nums)
    # p2_mult_nums = find_mul(lines, parse_pattern_part2, filter_pattern2)
    # sum_total = sum_total_mult_nums(p2_mult_nums)
    print(f"part two = {sum_total}")


if __name__ == "__main__":
    main()
