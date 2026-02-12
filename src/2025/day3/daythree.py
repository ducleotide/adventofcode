import logging

import aoc_common
from pydantic import BaseModel

# logging.basicConfig(level=logging.DEBUG)

class Battery(BaseModel):
    bank_index: int
    joltage: int


class BatteryBank(BaseModel):
    bank_list: str
    joltages: list[Battery] = []
    max_joltage: int = -1
    max_battery: list[Battery] = []

    def __init__(self, /, **data):
        super().__init__(**data)
        if self.bank_list:
            int_list = [int(c) for c in self.bank_list]
            for i in range(len(int_list)):
                logging.debug(f"joltage: {i} {int_list[i]}")
                battery = Battery(bank_index=i, joltage=int_list[i])
                self.joltages.append(battery)
        else:
            logging.error("bank_list is no initialized")


def determine_max_battery_joltage(battery_bank: BatteryBank, battery_length=2):
    """Iterate through the battery bank joltages and determine the top "battery_length" joltages"""
    next_bank_starting_point = 0
    for battery_index in range(battery_length):
        next_max = Battery(bank_index=0, joltage=-1)
        bank_range_end = len(battery_bank.joltages) - (battery_length - (battery_index + 1))
        logging.debug(f"starting next max index = {battery_index}. len {len(battery_bank.joltages)}. bank_range: {next_bank_starting_point} {bank_range_end}")
        for j in range(next_bank_starting_point, bank_range_end):
            battery = battery_bank.joltages[j]
            if battery.joltage > next_max.joltage:
                next_max = battery
                logging.debug(f"found higher joltage: [{next_max}]")
        logging.debug(f"next max [{next_max}")
        battery_bank.max_battery.append(next_max)
        next_bank_starting_point = next_max.bank_index + 1

    # calculate joltage value
    battery_bank.max_joltage = 0
    exp = 0
    for max_battery_val in reversed(battery_bank.max_battery):
        joltage_val = max_battery_val.joltage * (10**exp)
        logging.debug(f"max_battery_val {max_battery_val.joltage}, exp {exp}, {max_battery_val.joltage} * (10**{exp}) {joltage_val}")
        exp += 1
        battery_bank.max_joltage += joltage_val

    logging.info(f"batterybank max_joltage {battery_bank.max_joltage}")


def load_battery_banks(input_file: str, ) -> list[BatteryBank]:
    """Loads battery banks from the input file."""
    with open(input_file, 'r') as f:
        battery_banks: list[BatteryBank] = []
        for line in f:
            battery_bank = BatteryBank(bank_list=line.strip())
            logging.debug(f"battery_bank: {battery_bank.bank_list}")

            # determine_max_battery_joltage(battery_bank)
            battery_banks.append(battery_bank)

        return battery_banks


def main():
    args = aoc_common.aoc_parse_args()
    battery_banks = load_battery_banks(args.inputfile)

    joltage_sum = 0
    for battery_bank in battery_banks:
        determine_max_battery_joltage(battery_bank)
        joltage_sum += battery_bank.max_joltage
    logging.info(f"Part1 joltage_sum = {joltage_sum}")
    logging.info(f"------------------")
    battery_banks = load_battery_banks(args.inputfile)
    joltage_sum = 0
    for battery_bank in battery_banks:
        determine_max_battery_joltage(battery_bank, battery_length=12)
        joltage_sum += battery_bank.max_joltage
    logging.info(f"Part2 joltage_sum = {joltage_sum}")


if __name__ == "__main__":
    main()
