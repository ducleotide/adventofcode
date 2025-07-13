
def main():
    import argparse
    arg_parser = argparse.ArgumentParser()
    arg_parser.add_argument('input', nargs='?', default=sys.stdin)
    arg_parser.add_argument('-c', default="", dest='instr')
    args = arg_parser.parse_args()

    if args.instr:
        print(f'Part one: {args.instr}')
        
    else:
        args.input = os.path.abspath(args.input)