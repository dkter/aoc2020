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

# bus_offsets = [(bus, index) for index, bus in enumerate(ids) if bus is not None]
# order = 1
# for time_start in count(0, ids[0]):
#     if time_start > 10**order:
#         print(10**order)
#         order += 1
#     # for diff, busid in enumerate(ids[1:]):
#     #     diff += 1
#     #     if busid is not None and busid - (time_start % busid) != diff:
#     #         break
#     for bus, offset in bus_offsets:
#         if (time_start + offset) % bus != 0:
#             break
#     else:
#         print(time_start)
#         break
