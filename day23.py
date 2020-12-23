class WraparoundList(list):
    def __getitem__(self, index):
        if not isinstance(index, slice):
            if index >= len(self):
                return self[index % len(self)]
            elif index < 0:
                return self[index % len(self)]
            else:
                return super().__getitem__(index)
        else:
            start = index.start
            end = index.stop
            # if start is None:
            #     return super().__getitem__(index)
            # if start < len(self) and end is not None and end >= len(self):
            #     return self[start:] + self[:end % len(self)]
            # elif start is not None and end is not None and start >= len(self):
            #     return self[start % len(self):end % len(self)] # this should work most of the time
            # elif start is None and end >= len(self):
            #     return self[:end % len(self)]
            # elif end is None and start >= len(self):
            #     return self[start % len(self):]
            if start is not None and start < len(self) and end is not None and end >= len(self):
                return self[start:] + self[:end % len(self)]
            return super().__getitem__(
                slice(
                    start if start is None else start % len(self),
                    end if end is None else end % len(self)
                )
            )
        return super().__getitem__(index)

with open("day23.in") as f:
    cups = WraparoundList([int(i) for i in f.read().strip()])

print(cups[8:10])
print(cups[7:10])

min_cup = min(cups)
max_cup = max(cups)

current_idx = 0
current = None
for _ in range(100):
    if current is None:
        current_idx = 0
    else:
        current_idx = cups.index(current) + 1
    current = cups[current_idx]
    #print("index:", current_idx)
    pickup = cups[current_idx+1:current_idx+4]
    for i in pickup:
        cups.remove(i)

    destination = current - 1
    while destination in pickup or destination < min_cup:
        destination -= 1
        if destination < min_cup:
            destination = max_cup
    dest_idx = cups.index(destination)

    #print(current, pickup, destination, dest_idx)
    cups = WraparoundList(cups[:dest_idx+1] + pickup + cups[dest_idx+1:])
    current_idx += 1
    if current_idx >= len(cups):
        current_idx = 0
    #print(cups)
    #print()

print(cups)
print(''.join([str(cup) for cup in cups[cups.index(1)+1:] + cups[:cups.index(1)]]))
