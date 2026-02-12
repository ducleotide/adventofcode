import logging
from pydantic import BaseModel
import aoc_common

logger = logging.getLogger(name=__name__)
# logger.setLevel(level=logging.DEBUG)

class IdRange(BaseModel):
    start_id: int
    end_id: int


def load_id_ranges(input_file):
    with open(input_file, 'r') as f:
        id_ranges: list[IdRange] = []
        lines = f.readlines()
        for x in lines:
            str_id_ranges = x.split(',')
            for str_id_range in str_id_ranges:
                start_id, end_id = str_id_range.split('-')
                id_range = IdRange(start_id=int(start_id), end_id=int(end_id))
                logging.debug(f"id_range {id_range}")
                id_ranges.append(id_range)

        return id_ranges


def compare_with_rest(orig_str: str, substr: str, rest_of_str: str, sub_len: int):
    len_rest_of_str = len(rest_of_str)
    if sub_len >= int(len(orig_str) / 2 + 1):
        return True
    for i in range(0, len_rest_of_str, sub_len):
        if substr != rest_of_str[i: i + sub_len]:
            return compare_with_rest(orig_str, orig_str[:sub_len + 1], orig_str[sub_len + 1:], sub_len + 1)
    return False


def id_valid(prod_id: int, id_len:int = 1) -> bool:
    str_id = str(prod_id)
    logger.debug(f"str: {str_id}")

    substr = str_id[:id_len]
    rest_of_str = str_id[id_len:]
    logger.debug(f"substr")
    return compare_with_rest(str_id, substr, rest_of_str, id_len)


def find_invalid_ids(id_range: IdRange, use_mult_factor:bool = False):
    invalid_ids: list[int] = []

    for prod_id in range(id_range.start_id, id_range.end_id+1):
        if use_mult_factor:
            id_len = 1
        else:
            id_len = int(len(str(prod_id))/2)
            if len(str(prod_id)) % 2 == 1:
                logging.debug(f"{prod_id} is of odd length. it is Valid")
                continue
        logging.debug(f"check valid {prod_id}, id_len {id_len}")
        if not id_valid(prod_id, id_len=id_len):
            # logging.debug(f"{id} is invalid")
            invalid_ids.append(prod_id)
    logger.info(f"num invalid ids in {id_range} is {len(invalid_ids)}")
    return invalid_ids


def main():
    args = aoc_common.aoc_parse_args()

    id_ranges = load_id_ranges(args.inputfile)
    tot_invalid_ids: list[int] = []
    for id_range in id_ranges:
        invalid_ids = find_invalid_ids(id_range)
        logger.info(f"invalid_ids: {invalid_ids}")
        tot_invalid_ids.extend(invalid_ids)
    logger.info(f"tot invalid_ids: {len(tot_invalid_ids)}")
    logger.info(f"PART 1: sum tot_invalid: {sum(tot_invalid_ids)}")
    logger.info("-----------------")
    logger.info("-----------------")
    logger.info("-----------------")
    sum_invalid_ids = 0
    tot_invalid_ids: list[int] = []
    for id_range in id_ranges:
        invalid_ids = find_invalid_ids(id_range, use_mult_factor=True)
        logger.info(f"invalid_ids: {invalid_ids}")
        tot_invalid_ids.extend(invalid_ids)
        sum_invalid_ids += sum(invalid_ids)
    logger.info(f"tot invalid ids: {len(tot_invalid_ids)}")
    logger.info(f"PART2: sum_tot_invalid: {sum_invalid_ids}")

if __name__ == "__main__":
    main()