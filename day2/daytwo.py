import aoc_common

import logging


def load_input(inputfile):
    ret = []
    infile = open(inputfile, 'r')

    for report in infile:
        levels = report.split()
        ret.append(list(map(lambda x: int(x), levels)))
    return ret

def check_safety(increasing, prev, cur):
    if increasing:
        if prev > cur:
            return False
        else:
            return 0 < cur - prev <= 3
    else:
        if prev < cur:
            return False
        else:
            return 0 < prev - cur <= 3


def determine_safety(report_levels, safety_checks=0):
    prev_report = report_levels[0]
    print(f"report_levels: {report_levels}")
    increasing = True
    start = True
    safety_ct = 0

    num_levels = len(report_levels)
    for i in range(1, num_levels):
        print(f"CHECKING --- {start} {increasing} {prev_report} {report_levels[i]}, {safety_ct}")
        if i > 1:
            start = False
        if prev_report < report_levels[i] and increasing:
            if check_safety(increasing, prev_report, report_levels[i]):
                increasing = True
            else:
                print(f"CHECK FAILED {increasing} {prev_report} {report_levels[i]}, {safety_ct}")
                if safety_ct > safety_checks:
                    return False
                safety_ct += 1
            if start:
                start = False
        elif prev_report > report_levels[i]:
            if start:
                start = False
                increasing = False
            elif not start and increasing:  # not start:

                print(f"01 DECREASE CHECK FAILED {increasing} {prev_report} {report_levels[i]}, {safety_ct}")
                safety_ct += 1
                if safety_ct > safety_checks:
                    return False

            elif not start and not increasing:
                if check_safety(increasing, prev_report, report_levels[i]):
                    increasing = False
                else:
                    print(f"02 DECREASE CHECK FAILED {increasing} {prev_report} {report_levels[i]}, {safety_ct}")
                    safety_ct += 1
                    if safety_ct > safety_checks:
                        return False
        else:
            print(f"ELSE CHECK FAILED {increasing} {prev_report} {report_levels[i]}, {safety_ct}")
            safety_ct += 1
            if safety_ct > safety_checks:
                return False
        prev_report = report_levels[i]
    return True


def count_safe(reports, safety_checks=0):
    num_safe = 0
    for report_levels in reports:
        safe = determine_safety(report_levels, safety_checks)
        if safe:
            num_safe += 1

    return num_safe


def main():
    args = aoc_common.aoc_parse_args()

    reports = load_input(args.inputfile)

    num_safe = count_safe(reports)
    logging.info(f"Number of safe: {num_safe}")


if __name__ == "__main__":
    main()