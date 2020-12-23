class Cup:
    def __init__(self, value):
        self.next_cup = None
        self.value = value


class CupCircle:
    def __init__(self, cups):
        self.current_cup = Cup(cups[0])
        cup = self.current_cup
        for i in range(len(cups) - 1):
            cup.next_cup = Cup(cups[i + 1])
            cup = cup.next_cup
        cup.next_cup = self.current_cup
        self.iter_cup = self.current_cup
        self.break_on_first = False
        self.visited_first = False
        self.cup_hash = {
            c.value: c
            for c in self.linear()
        }

    def rotate(self):
        self.current_cup = self.current_cup.next_cup

    def pickup(self):
        pickup = (
            self.current_cup.next_cup,
            self.current_cup.next_cup.next_cup,
            self.current_cup.next_cup.next_cup.next_cup
        )
        self.current_cup.next_cup = pickup[-1].next_cup
        return pickup

    def find_value(self, to_find):
        return self.cup_hash[to_find]

    def linear(self):
        # there's probably a much better way of doing this
        self.break_on_first = True
        return iter(self)

    def __iter__(self):
        self.iter_cup = self.current_cup
        return self

    def __next__(self):
        old_iter_cup = self.iter_cup
        self.iter_cup = self.iter_cup.next_cup
        if old_iter_cup == self.current_cup and self.break_on_first:
            if self.visited_first:
                self.break_on_first = False
                self.visited_first = False
                raise StopIteration
            else:
                self.visited_first = True
        return old_iter_cup


with open("day23.in") as f:
    cups = [int(i) for i in f.read().strip()]
cups += list(range(10, 1000001))
min_cup = min(cups)
max_cup = max(cups)

cups = CupCircle(cups)

current = None
for _ in range(10_000_000):
    if current is not None:
        cups.current_cup = current.next_cup
    current = cups.current_cup
    pickup = cups.pickup()

    destination = current.value - 1
    while (
        destination == pickup[0].value
        or destination == pickup[1].value
        or destination == pickup[2].value
        or destination < min_cup
    ):
        destination -= 1
        if destination < min_cup:
            destination = max_cup
    dest_item = cups.find_value(destination)

    dest_item_next = dest_item.next_cup
    dest_item.next_cup = pickup[0]
    pickup[-1].next_cup = dest_item_next

one = cups.find_value(1)
print(one.next_cup.value * one.next_cup.next_cup.value)
