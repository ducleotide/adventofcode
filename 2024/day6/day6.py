def load_input(filename) -> list[str]:
    with open(filename) as f:
        input_arr:list[str] = []
        for line in f:
            input_arr.append(line.strip())
        return input_arr


def main():
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('input', nargs='?')
    args = parser.parse_args()

    input_arr = load_input(args.input)

    