import logging
from pydantic import BaseModel
import aoc_common

logger = logging.getLogger(name=__name__)
# logger.setLevel(level=logging.DEBUG)

class IdRange(BaseModel):
    start_id: int
    end_id: int


def load_idranges(inputfile):
    with open(inputfile, 'r') as f:
        idranges: list[IdRange] = []
        lines = f.readlines()
        for x in lines:
            str_idranges = x.split(',')
            for str_idrange in str_idranges:
                start_id, end_id = str_idrange.split('-')
                id_range = IdRange(start_id=int(start_id), end_id=int(end_id))
                logging.debug(f"id_range {id_range}")
                idranges.append(id_range)

        return idranges


def compare_with_rest(orig_str: str, substr: str, rest_of_str: str, sublen: int):
    len_rest_of_str = len(rest_of_str)
    if sublen >= int(len(orig_str)/2+1):
        return True
    for i in range(0, len_rest_of_str, sublen):
        if substr != rest_of_str[i: i+sublen]:
            return compare_with_rest(orig_str, orig_str[:sublen+1], orig_str[sublen+1:], sublen+1)
    return False


def id_valid(id: int, idlen:int = 1) -> bool:
    str_id = str(id)
    logger.debug(f"str: {str_id}")

    substr = str_id[:idlen]
    rest_of_str = str_id[idlen:]
    logger.debug(f"substr")
    return compare_with_rest(str_id, substr, rest_of_str, idlen)

    #
    # if len(str_id) % mult_factor != 0:
    #     logger.debug(f"{id} is valid (modulo != 0)")
    #     return True
    # subs_len = int(len(str_id) / mult_factor)
    # substr = str_id[0:subs_len]
    # logger.debug(f"sub_len {subs_len}; substr {substr} ")
    # logger.debug(f"range: {list(range(subs_len, len(str_id), subs_len))}")
    # for i in range(subs_len, len(str_id), subs_len):
    #     logger.debug(f"{i}: str_id[i:i+subs_len] {str_id[i:i+subs_len]}")
    #     if substr != str_id[i:i+subs_len]:
    #         return True
    # return False
    # return str_id[0:subs_len] != str_id[subs_len:]


def find_invalid_ids(id_range: IdRange, use_mult_factor:bool = False):
    invalid_ids: list[int] = []

    for id in range(id_range.start_id, id_range.end_id+1):
        # logging.debug(f"check valid {id}")
        if use_mult_factor:
            max_mult_factor = int(len(str(id))/2) + 1
            logging.info(f"from 2 to {max_mult_factor} {list(range(1, max_mult_factor))}")
            for mult_factor in range(1, max_mult_factor):
                if not id_valid(id, mult_factor=mult_factor):
                    invalid_ids.append(id)
                    continue
        else:
            if not id_valid(id, int(len(str(id))/2)):
                # logging.debug(f"{id} is invalid")
                invalid_ids.append(id)
    logger.info(f"num invalid ids in {id_range} is {len(invalid_ids)}")
    return invalid_ids


def main():
    args = aoc_common.aoc_parse_args()

    id_ranges = load_idranges(args.inputfile)
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
    # sum_invalid_ids = 0
    # tot_invalid_ids: list[int] = []
    # for id_range in id_ranges:
    #     invalid_ids = find_invalid_ids(id_range, use_mult_factor=True)
    #     logger.info(f"invalid_ids: {invalid_ids}")
    #     tot_invalid_ids.extend(invalid_ids)
    #     sum_invalid_ids += sum(invalid_ids)
    # logger.info(f"totinvalid ids: {len(tot_invalid_ids)}")
    # logger.info(f"PART2: sum_tot_invalid: {sum_invalid_ids}")

if __name__ == "__main__":
    main()