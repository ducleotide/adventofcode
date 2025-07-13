def load_input(filename):
    fin = open(filename, 'r')
    page_ordering_rules = []
    page_number_updates = []
    for line in fin:
        if '|' in line:
            spl = line.strip().split('|')
            page_ordering = (int(spl[0]), int(spl[1]))
            page_ordering_rules.append(page_ordering)

        else:
            if len(line.strip()) > 0:
                page_numbers = list(map(lambda x: int(x), line.strip().split(',')))
                page_number_updates.append(page_numbers)
    return page_ordering_rules, page_number_updates


class Page:
    number: int
    is_before: list[int]

    def __init__(self, first, second):
        self.number = first
        self.is_before = [second]

    def update_page(self, second):
        self.is_before.append(second)


class OrderingRules:
    ordering_rules: dict(int, Page) = {}

    def __init__(self, page_ordering_rules: list[(int,int)]):
        for first, second in page_ordering_rules:
            if first not in self.ordering_rules:
                self.ordering_rules[first] = Page(first, second)
            else:
                self.ordering_rules[first].update_page(second)

            # condense update ordering rules

    def is_valid(self, update):
        for page in update:
            pass


def main():
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('filename')
    args = parser.parse_args()

    page_ordering_rules, page_number_updates = load_input(args.filename)

    ordering_rules = OrderingRules(page_ordering_rules, page_number_updates)

    for update in page_number_updates:
        print(f"pagen number update: [{update}]")
        ordering_rules.is_valid(update)


if __name__ == '__main__':
    main()
