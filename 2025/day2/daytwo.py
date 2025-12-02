import logging
from pydantic import BaseModel
import aoc_common


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


def find_invalid_ids(id_range: IdRange):
    invalid_ids: list[int] = []

    for id in range(id_range.start_id, id_range.end_id+1):
        logging.debug(f"check valid {id}")
        str_id = str(id)
        if len(str_id) % 2 == 1:
            logging.debug(f"{id} is valid (odd length)")
            continue
        half_size = int(len(str_id)/2)
        if str_id[0:half_size] == str_id[half_size:]:
            logging.info(f"{id} is invalid")
            invalid_ids.append(id)
    logging.info(f"num invalid ids in {id_range} is {len(invalid_ids)}")
    return invalid_ids


def main():
    args = aoc_common.aoc_parse_args()

    id_ranges = load_idranges(args.inputfile)
    tot_invalid_ids: list[int] = []
    for id_range in id_ranges:
        invalid_ids = find_invalid_ids(id_range)
        logging.info(f"invalid_ids: {invalid_ids}")
        tot_invalid_ids.extend(invalid_ids)
    logging.info(f"tot invalid_ids: {len(tot_invalid_ids)}")
    logging.info(f"sum tot_invalid: {sum(tot_invalid_ids)}")

if __name__ == "__main__":
    main()