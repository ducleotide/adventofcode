import re
import aoc_common

def build_line_w_beams(line: str, beam_row: list[int]) -> str:
    new_line = line
    if len(beam_row) > 0:
        for beam_index in beam_row:
            # print(f"beam_index {beam_index}")
            # print(f"old_line: {line}")
            new_line = new_line[:beam_index] + '|' + new_line[beam_index+1:]
    return new_line


def print_table(input_table: list[str]) -> None:
    for l in input_table:
        print(l)


def find_beams(line: str) -> list[int]:
    ret: list[int] = []

    if line.find('S') != -1:
        ret.append(line.find('S'))
        return ret

    beam_ranges = re.finditer('\\|', line)
    for beam_range in list(beam_ranges):
        # print(f"beam_range: {beam_range.span()}")
        ret.append(beam_range.span()[0])
    return ret


def find_splitters(line: str) -> list[int]:
    ret: list[int] = []
    splitters_ranges = re.finditer('\\^', line)
    for splitter_range in list(splitters_ranges):
        ret.append(splitter_range.span()[0])
    return ret


def main():
    args = aoc_common.aoc_parse_args()

    input_table = aoc_common.load_input_table(args.inputfile)
    print(f"input_table")
    output_table: list[str] = []
    print_table(input_table)

    beam_indices_rows: list[list[int]] = []

    beam_indices: list[int] = [input_table[0].find('S')]

    print(f"beams indices {beam_indices}")
    print(f"beams_rows {beam_indices_rows}")
    # prev_beam_indices = beam_indices
    output_table.append(input_table[0].strip())
    beam_indices_rows.append(beam_indices)
    split_ct = 0
    for l in range(1, len(input_table)):
        prev_line = output_table[l-1]
        prev_beam_indices = find_beams(prev_line)
        curr_line = input_table[l]
        print(f"prev_line: {prev_line}")
        print(f"curr_line: {curr_line}")
        print(f"prev_row_beams = {prev_beam_indices}")
        splitters = find_splitters(curr_line)
        # print(f"splitters: {splitters_list} {len(splitters_list)}")
        if len(splitters) > 0:
            print(f"splitters: {splitters}")
            row_beam_indices: list[int] = []
            for splitter in splitters:
                print(f"splitter {splitter}")
                if prev_line[splitter] == '|':
                    # split
                    print(f"splitting at {splitter}")
                    row_beam_indices.append(splitter-1)
                    row_beam_indices.append(splitter+1)
                    split_ct += 1
            #merge row_beam_indices and
            for prev_beam_index in prev_beam_indices:
                if curr_line[prev_beam_index] == '.':
                    row_beam_indices.append(prev_beam_index)
        else:
            print(f"splitters_list is empty")
            row_beam_indices = prev_beam_indices
            # beams_rows.append(prev_row_beams)
        line_w_beams = build_line_w_beams(curr_line, row_beam_indices)
        print(f"beam_line: {line_w_beams}")
        output_table.append(line_w_beams)
        beam_indices_rows.append(prev_beam_indices)

        # print(f"prev_rows  {prev_row_beams}")
        # print(f"beams_rows {beams_rows}")

        # print(f"index ^: {l.find('^')}")
        # l_index = l.find('^')
        # if l_index > 0:
        #     if l_index ==
        print("----end loop----")
    print_table(output_table)
    print(f"number of splits: {split_ct}" )

if __name__ == "__main__":
    main()
