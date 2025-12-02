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
    # print(f"TEST report_levels: {report_levels}")
    start = True
    safety_ct = 0
    if prev_report < report_levels[1]:
        increasing = True
    else:
        increasing = False
    num_levels = len(report_levels)
    i = 1
    while i < num_levels:
        # print(f"CHECKING --- {start} {increasing} {prev_report} {report_levels[i]}, {safety_ct}")
        # if i > 1:
        #     start = False
        if not check_safety(increasing, prev_report, report_levels[i]):
            # print(f"CHECK FAILED inc:{increasing}; {prev_report} {report_levels[i]}; {i}")
            return i
            # safety_ct += 1
            # if safety_ct > safety_checks:
            #     print(f"=== FAILED {report_levels} ====")
            #     return False
            # else:
            #     print(f"ALLOW {safety_ct} safety check {safety_checks}")
        prev_report = report_levels[i]
        i += 1
    # print(f"=== PASSED {report_levels} ====")
    return -100
        # if increasing:
        #
        #         increasing = True
        #     else:
        #         if safety_ct > safety_checks:
        #             return False
        #         safety_ct += 1
        #     if start:
        #         start = False
        # elif prev_report > report_levels[i]:
        #     if start:
        #         start = False
        #         increasing = False
        #     elif not start and increasing:  # not start:
        #
        #         print(f"01 DECREASE CHECK FAILED {increasing} {prev_report} {report_levels[i]}, {safety_ct}")
        #         safety_ct += 1
        #         if safety_ct > safety_checks:
        #             return False
        #
        #     elif not start and not increasing:
        #         if check_safety(increasing, prev_report, report_levels[i]):
        #             increasing = False
        #         else:
        #             print(f"02 DECREASE CHECK FAILED {increasing} {prev_report} {report_levels[i]}, {safety_ct}")
        #             safety_ct += 1
        #             if safety_ct > safety_checks:
        #                 return False
        # else:
        #     print(f"ELSE CHECK FAILED {increasing} {prev_report} {report_levels[i]}, {safety_ct}")
        #     safety_ct += 1
        #     if safety_ct > safety_checks:
        #         return False


def count_safe(reports, safety_checks=0):
    num_safe = 0
    for report_levels in reports:

        index = determine_safety(report_levels)
        if index == -100:  #len(report_levels):
            # print("SAFE")
            num_safe += 1
        else:
            if safety_checks > 0:
                # remove_bad_report and try again
                new_report_levels = report_levels.copy()
                del new_report_levels[index]
                index = determine_safety(new_report_levels)
                if index == -100:  #len(new_report_levels):
                    # print("==== SAFE PASS2")
                    num_safe += 1
                else:
                    print(f"==== FAIL2: orig: {report_levels}; new {new_report_levels}")

    return num_safe


def main():
    args = aoc_common.aoc_parse_args()

    reports = load_input(args.inputfile)

    num_safe = count_safe(reports)
    logging.info(f"Number of safe: {num_safe} out of {len(reports)}")


if __name__ == "__main__":
    main()