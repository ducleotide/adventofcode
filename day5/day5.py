
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


class OrderingRules:
    def __init__(self, page_ordering_rules: list(int)):
        self.ordering_rules = []
        for ordering_rule in page_ordering_rules:
            self.ordering_rules.append(page_ordering_rules)


def build_ordering_rules(page_ordering_rules):
    ordering_rules: OrderingRules = OrderingRules(page_ordering_rules)



    return ordering_rules