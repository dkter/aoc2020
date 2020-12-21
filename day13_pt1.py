from itertools import count

with open("day13.in") as f:
    lines = f.readlines()
    earliest_timestamp = int(lines[0].strip())
    ids = []
    for c in lines[1].strip().split(','):
        try:
            ids.append(int(c))
        except ValueError:
            ids.append(None)

time, bus = min((earliest_timestamp - (earliest_timestamp % id) + id, id) for id in ids if id is not None)
print((time - earliest_timestamp) * bus)
