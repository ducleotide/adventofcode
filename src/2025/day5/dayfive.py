from typing import Tuple

import aoc_common
from pydantic import BaseModel


class IngredientRange(BaseModel):
    start_id: int
    end_id: int


def load_input_file(filename: str) -> Tuple[list[IngredientRange], list[int]]:
    ingredient_ranges: list[IngredientRange] = []
    ingredient_ids: list[int] = []

    with open(filename, 'r') as f:
        for line in f:
            if line.strip() == "":
                break
            first_id, second_id = line.strip().split('-')
            ingredient_ranges.append(IngredientRange(start_id=int(first_id), end_id=int(second_id)))

        for line in f:
            fresh_id = int(line.strip())
            ingredient_ids.append(fresh_id)

        return ingredient_ranges, ingredient_ids


def is_fresh(fresh_id: int, ingredient_ranges: list[IngredientRange]) -> bool:
    for ingredient_range in ingredient_ranges:
        if ingredient_range.start_id <= fresh_id <= ingredient_range.end_id:
            return True
    return False


def create_fresh_ids(ingredient_ranges: list[IngredientRange]) -> list[IngredientRange]:
    union_ranges: list[IngredientRange] = []

    # sort by starting_id
    sorted_ranges = sorted(ingredient_ranges, key=lambda x: x.start_id)

    for ingredient_range in sorted_ranges:
        # print(f"ingredient range{ingredient_range}")
        if len(union_ranges) == 0:
            union_ranges.append(ingredient_range)
            continue

        if ingredient_range.start_id <= union_ranges[-1].end_id:
            # union_ranges[-1].end_id = ingredient_range.end_id
            if ingredient_range.end_id > union_ranges[-1].end_id:
                union_ranges[-1].end_id = ingredient_range.end_id
            else:
                # do nothing
                pass
        else:
            union_ranges.append(ingredient_range)

    return union_ranges


def count_union_ranges(union_ranges: list[IngredientRange]) -> int:
    count = 0
    for ingredient_range in union_ranges:
        num_fresh = ingredient_range.end_id - ingredient_range.start_id + 1
        print(f"range: {ingredient_range}: num_fresh: {num_fresh}")
        count += num_fresh

    return count


def main():
    args = aoc_common.aoc_parse_args()

    ingredient_ranges, ingredient_ids = load_input_file(args.inputfile)

    fresh_list: list[int] = []
    for fresh_id in ingredient_ids:
        if is_fresh(fresh_id, ingredient_ranges):
            fresh_list.append(fresh_id)

    print(f"part 1: num fresh {len(fresh_list)}")

    union_ranges = create_fresh_ids(ingredient_ranges)
    # print(f"union ranges: {union_ranges}")
    num_fresh_ids = count_union_ranges(union_ranges)
    print(f"part2: num fresh_ids {num_fresh_ids}")

if __name__ == "__main__":
    main()