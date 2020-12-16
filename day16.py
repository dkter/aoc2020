from dataclasses import dataclass

@dataclass
class Range:
    name: str
    a1: int
    a2: int
    b1: int
    b2: int

names = []
notes = {}
your_ticket = None
nearby_tickets = []
with open("day16.in") as f:
    for line in f:
        if ":" in line:
            if line.startswith("your ticket"):
                your_ticket = tuple(int(i) for i in next(f).strip().split(','))
            elif line.startswith("nearby tickets"):
                pass
            else:
                key, range_ = line.split(":")
                a, b = range_.split(" or ")
                a1, a2 = (int(i) for i in a.split("-"))
                b1, b2 = (int(i) for i in b.split("-"))
                notes[key] = Range(key, a1, a2, b1, b2)
                names.append(key)
        elif not line.strip():
            pass
        else:
            # it's a ticket
            nearby_tickets.append(tuple(int(i) for i in line.strip().split(',')))

error_rate = 0
valid_tickets = []
for ticket in nearby_tickets:
    invalid = False
    for value in ticket:
        for range_ in notes.values():
            if range_.a1 <= value <= range_.a2 or range_.b1 <= value <= range_.b2:
                break
        else:
            error_rate += value
            invalid = True
    if not invalid:
        valid_tickets.append(ticket)

print(error_rate)

position_possibilities = {
    idx: names[:]
    for idx in range(len(your_ticket))
}
for ticket in valid_tickets:
    for index, value in enumerate(ticket):
        for name in position_possibilities[index]:
            range_ = notes[name]
            if not (range_.a1 <= value <= range_.a2 or range_.b1 <= value <= range_.b2):
                position_possibilities[index].remove(name)

decided = set()
while not all(len(p) == 1 for p in position_possibilities.values()):
    for key, p in position_possibilities.items():
        if len(p) == 1:
            decided.add(p[0])
        else:
            for name in p:
                if name in decided:
                    position_possibilities[key].remove(name)

product = 1
for idx, p in position_possibilities.items():
    if "departure" in p[0]:
        product *= your_ticket[idx]

print(product)
