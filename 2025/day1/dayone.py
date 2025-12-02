import math
from enum import Enum

import aoc_common
from pydantic import BaseModel


class Direction(Enum):
    LEFT = 'L'
    RIGHT = 'R'


class Rotation(BaseModel):
    direction: Direction
    amount: int
    # def __init__(self, dir: str, rot: int):
    #     self.direction = dir
    #     self.rotation = rot


def load_rotations(filename):
    with open(filename, 'r') as f:
        rotations: list[Rotation] = list[Rotation]()
        for l in f:
            dial = Rotation(direction=Direction(l[0]), amount=int(l[1:]))
            rotations.append(dial)

        return rotations


def perform_rotation(current_position: int, rotation: Rotation, max_dial=100):
    resulting_position: int = -999
    clicks: int = 0

    clicks += math.trunc(rotation.amount / max_dial)
    if rotation.direction == Direction.LEFT:
        new_pos = current_position - (rotation.amount % max_dial)
        if new_pos < 0:
            resulting_position = max_dial + new_pos
            if current_position != 0:
                clicks += 1
        else:
            resulting_position = new_pos
    elif rotation.direction == Direction.RIGHT:
        new_pos = current_position + (rotation.amount % max_dial)
        if new_pos > max_dial:
            resulting_position = new_pos - max_dial
            if current_position != 0:
                clicks += 1
        else:
            resulting_position = new_pos
    else:
        raise Exception(f"Unknown direction: {rotation.direction} or amount {rotation.amount}")

    if resulting_position == max_dial or resulting_position == 0 :
        resulting_position = 0
        clicks += 1

    return resulting_position, clicks


def main():
    args = aoc_common.aoc_parse_args()

    rotations = load_rotations(args.inputfile)

    res_pos = 50
    ct = 0
    zeroes = 0
    print(f"The dial starts at {res_pos}")
    for rotation in rotations:
        res_pos, clicks = perform_rotation(res_pos, rotation)
        ct += clicks
        if res_pos == 0:
            zeroes += 1
        print(f"The dial is rotated {rotation.direction.value}{rotation.amount} to point {res_pos}. "
              f"It points at 0 {clicks} times")
    print(f"Number of clicks {ct}")
    print(f"Number of time pointing at 0: {zeroes}")


if __name__ == "__main__":
    main()
