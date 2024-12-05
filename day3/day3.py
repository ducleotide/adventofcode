import re

def load_input(filename):
    with open(filename) as f:
        ret = []
        for line in f:
            ret.append(line)
        return ret


def apply_mult(mult_str):
    split_str = mult_str.split(',')
    n1 = int(split_str[0].strip('mul('))
    n2 = int(split_str[1].strip(')'))
    return n1 * n2


def find_mul(lines: list[str]) -> list[list[int]]:
    mult_pats_lines:list[list[int]] = []

    for line in lines:
        print(f"line [==={line}===]")
        mult = parse_pattern(line)
        mult_pats_lines.append(mult)
    return mult_pats_lines


def parse_pattern(line):
    pat = re.compile("mul\\([0-9]*,[0-9]*\\)", re.UNICODE)
    x = re.findall(pat, line)
    print(f"patterns = {x}")
    mult = list(map(apply_mult, x))
    return mult


def sum_total_mult_nums(mult_pats_lines: list[list[int]]) -> int:
    sum_total = 0
    for mult_num in mult_pats_lines:
        sum_line = sum(mult_num)
        print(f'sum {mult_num} = {sum_line}')
        sum_total += sum(mult_num)
    return sum_total


def main():
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument('input', help='path to input file')
    args = parser.parse_args()

    lines = load_input(args.input)

    mult_nums = find_mul(lines)
    sum_total = sum_total_mult_nums(mult_nums)
    print(f"part one = {sum_total}")


if __name__ == "__main__":
    main()
