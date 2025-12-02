import aoc_common
from pydantic import BaseModel


class Rotation(BaseModel):
    direction: str
    amount: int
    # def __init__(self, dir: str, rot: int):
    #     self.direction = dir
    #     self.rotation = rot


def load_rotations(filename):
    with open(filename, 'r') as f:
        rotations: list[Rotation] = list[Rotation]()
        for l in f:
            dial = Rotation(direction=l[0], amount=int(l[1:]))
            rotations.append(dial)

        return rotations

def perform_rotation(current_position: int, rotation: Rotation, max_dial=99):
    resulting_position: int = -999

    if rotation.direction == "L":
        new_pos = current_position - (rotation.amount % (max_dial + 1))
        if new_pos < 0:
            resulting_position = (max_dial + 1) + new_pos
        else:
            resulting_position = new_pos
    elif rotation.direction == "R":
        new_pos = current_position + (rotation.amount % (max_dial + 1))
        if new_pos > (max_dial + 1):
            resulting_position = new_pos - (max_dial + 1)
        else:
            resulting_position = new_pos
    else:
        raise Exception(f"Unknown direction: {rotation.direction} or amount {rotation.amount}")

    if resulting_position == (max_dial + 1):
        resulting_position = 0

    return resulting_position


def main():
    args = aoc_common.aoc_parse_args()

    rotations = load_rotations(args.inputfile)

    res_pos = 50
    ct = 0
    print(f"The dial starts at {res_pos}")
    for rotation in rotations:
        res_pos = perform_rotation(res_pos, rotation)
        if res_pos == 0:
            ct += 1
        print(f"The dial is rotated {rotation.direction}{rotation.amount} to point {res_pos}")
    print(f"Number of time pointing at 0: {ct}")

if __name__ == "__main__":
    main()
