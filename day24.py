def get_adjacent_tiles(map, q, r):
    return [
        ((q, r-1), map.get((q, r-1), False)),
        ((q, r+1), map.get((q, r+1), False)),
        ((q-1, r), map.get((q-1, r), False)),
        ((q+1, r), map.get((q+1, r), False)),
        ((q-1, r+1), map.get((q-1, r+1), False)),
        ((q+1, r-1), map.get((q+1, r-1), False))
    ]

def black_count(map):
    return list(map.values()).count(True)

paths = []
with open("day24.in") as f:
    for line in f:
        dirs = []
        l = iter(line.strip())
        dir = next(l)
        for ch in l:
            if dir in ("e", "w") or len(dir) == 2:
                dirs.append(dir)
                dir = ch
            else:
                dir += ch
        dirs.append(dir)
        paths.append(dirs)

map = {}
for path in paths:
    coords = [0, 0]
    for dir in path:
        if dir == "e":
            coords[0] += 1
        elif dir == "w":
            coords[0] -= 1
        elif dir == "nw":
            coords[1] -= 1
        elif dir == "se":
            coords[1] += 1
        elif dir == "sw":
            coords[0] -= 1
            coords[1] += 1
        elif dir == "ne":
            coords[0] += 1
            coords[1] -= 1
    coords = tuple(coords)
    map[coords] = not map.get(coords, False)

print(black_count(map))

for _ in range(100):
    new_map = map.copy()
    for coords, val in map.items():
        adjacent_tiles = get_adjacent_tiles(map, *coords)
        for coords2, val2 in adjacent_tiles + [(coords, val)]:
            adj_count = [tup[1] for tup in get_adjacent_tiles(map, *coords2)].count(True)
            if val2 == True and (adj_count == 0 or adj_count > 2):
                new_map[coords2] = False
            elif val2 == False and adj_count == 2:
                new_map[coords2] = True
    map = new_map

print(black_count(map))
