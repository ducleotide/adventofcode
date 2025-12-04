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
    max_battery: tuple[Battery, Battery] = (Battery(bank_index=-1, joltage=-1),
                                            Battery(bank_index=-1, joltage=-1))

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


def determine_max_battery_joltage(battery_bank: BatteryBank):
    """Iterate through the battery bank joltages and determine the top 2 joltages"""
    first_max = battery_bank.max_battery[0]
    for i in range(len(battery_bank.joltages)-1):
        battery: Battery = battery_bank.joltages[i]
        if battery.joltage > first_max.joltage:
            first_max = battery
            logging.debug(f"found higher joltage: [{first_max}]")
    logging.debug(f"first max [{first_max}]")
    second_max = battery_bank.max_battery[1]
    logging.debug(f"starting second max")
    starting_point = first_max.bank_index
    for j in range(starting_point, len(battery_bank.joltages)):
        battery = battery_bank.joltages[j]
        if battery.joltage > second_max.joltage and battery.bank_index != first_max.bank_index:
            second_max = battery
            logging.debug(f"found higher joltage: [{second_max}]")
    logging.debug(f"second max [{second_max}")

    if first_max.bank_index < second_max.bank_index:
        battery_bank.max_battery[0].joltage = first_max.joltage
        battery_bank.max_battery[0].bank_index = first_max.bank_index
        battery_bank.max_battery[1].joltage = second_max.joltage
        battery_bank.max_battery[1].bank_index = second_max.bank_index
    else:
        battery_bank.max_battery[0].joltage = second_max.joltage
        battery_bank.max_battery[0].bank_index = second_max.bank_index
        battery_bank.max_battery[1].joltage = first_max.joltage
        battery_bank.max_battery[1].bank_index = first_max.bank_index

    battery_bank.max_joltage = battery_bank.max_battery[0].joltage * 10 + battery_bank.max_battery[1].joltage
    logging.info(f"batterybank max_joltage {battery_bank.max_joltage}")


def load_battery_banks(input_file: str) -> list[BatteryBank]:
    """Loads battery banks from the input file."""
    with open(input_file, 'r') as f:
        battery_banks: list[BatteryBank] = []
        for line in f:
            battery_bank = BatteryBank(bank_list=line.strip())
            logging.info(f"battery_bank: {battery_bank.bank_list}")

            determine_max_battery_joltage(battery_bank)
            battery_banks.append(battery_bank)

        return battery_banks


def main():
    args = aoc_common.aoc_parse_args()
    battery_banks = load_battery_banks(args.inputfile)

    joltage_sum = 0
    for battery_bank in battery_banks:
        joltage_sum += battery_bank.max_joltage
    logging.info(f"joltage_sum = {joltage_sum}")




if __name__ == "__main__":
    main()
