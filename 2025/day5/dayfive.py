import aoc_common
from pydantic import BaseModel


class IngredientRange(BaseModel):
    start_id: int
    end_id: int


def load_input_file(filename: str):
    ingredient_ranges: list[IngredientRange] = []
    ingredient_ids: list[int] = []

    with open(filename, 'r') as f:
        for line in f:
            if line.strip() == "":
                break
            first_id, second_id = line.strip().split('-')
            ingredient_ranges.append(IngredientRange(start_id=int(first_id), end_id=int(second_id)))

        for line in f:
            id = int(line.strip())
            ingredient_ids.append(id)

        return ingredient_ranges, ingredient_ids


def is_fresh(id: int, ingredient_ranges: list[IngredientRange]) -> bool:
    ret = False

    for ingredient_range in ingredient_ranges:
        if ingredient_range.start_id <= id <= ingredient_range.end_id:
            return True

    return ret


def main():
    args = aoc_common.aoc_parse_args()

    ingredient_ranges, ingredient_ids = load_input_file(args.inputfile)

    fresh_list: list[int] = []
    for id in ingredient_ids:
        if is_fresh(id, ingredient_ranges):
            fresh_list.append(id)

    print(f"part 1: num fresh {len(fresh_list)}")

if __name__ == "__main__":
    main()