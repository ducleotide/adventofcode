import logging
import pandas as pd

logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s: %(message)s")


def load_input(filename):
    fin = open(filename, 'r')
    left_arr = []
    right_arr = []
    diff_arr = []
    x = []
    for line in fin:
        spl = line.strip().split()
        if len(spl) != 2:
            continue
        x.append({'left': int(spl[0]),
                'right': int(spl[1])})

        # left_arr.append(left)
        # right_arr.append(right)
        #
        # diff = right - left
        # out_arr = [left, right, diff]
        # logging.info(out_arr)
    arr = pd.DataFrame(x)
    return arr


def diff_arr(left_arr, right_arr):
    sorted_left = sorted(left_arr)
    sorted_right = sorted(right_arr)
    ret = []
    for l, r in zip(sorted_left, sorted_right):
        diff = abs(l - r)
        ret.append(diff)
    return sum(ret)


def similarity(df):
    left_arr = df['left'].unique().tolist()
    r_ct = df['right'].value_counts().sort_index()
    ret_arr = []
    logging.debug(f"r_ct {r_ct}")
    logging.debug(f"left_arr {left_arr}")
    for l in left_arr:
        if l in r_ct.index:
            x = int(r_ct.loc[l])
        else:
            x = 0
        logging.debug(f"{l} and rload {x}")
        ret_arr.append(x * l)
    ret = sum(ret_arr) if len(ret_arr) > 0 else 0
    return ret


def main():

    import argparse
    parser = argparse.ArgumentParser(description='Advent of Code 2024 Day 1')
    parser.add_argument('inputfile', type=str, )

    args = parser.parse_args()

    df = load_input(args.inputfile)

    left_arr = list(df['left'])
    right_arr = list(df['right'])
    logging.debug(f"left: {left_arr}, right: {right_arr}")
    part_one = diff_arr(left_arr, right_arr)
    logging.info(f"part_one {part_one}")

    part_two = similarity(df)
    logging.info(f"part two: {part_two}")


if __name__ == '__main__':
    main()