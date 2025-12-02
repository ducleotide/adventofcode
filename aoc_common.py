import logging


def aoc_parse_args():
    import argparse
    parser = argparse.ArgumentParser(description='Advent of Code')
    parser.add_argument('inputfile', type=str, )
    parser.add_argument('--debug', '-d', action='store_true', help='Debug mode')
    args = parser.parse_args()
    if args.debug:
        log_level = logging.DEBUG
    else:
        log_level = logging.INFO
    logging.basicConfig(level=log_level,
                        format="%(asctime)s %(levelname)s: %(message)s")
    return args
