from pprint import pprint
import timeit

layout = []
with open("day11.in") as f:
    for line in f:
        layout.append(list(line.strip()))

def part1(layout=[row[:] for row in layout]):
    new_layout = None
    while layout != new_layout:
        if new_layout is not None:
            layout = new_layout
        new_layout = [row[:] for row in layout]
        for y, row in enumerate(layout):
            for x, chr in enumerate(row):
                adjacent_seats = []
                for x_adj in range(-1, 2):
                    for y_adj in range(-1, 2):
                        if (x_adj != 0 or y_adj != 0) and 0 <= x + x_adj < len(row) and 0 <= y + y_adj < len(layout):
                            adjacent_seats.append(layout[y + y_adj][x + x_adj])
                if chr == 'L' and all(c != '#' for c in adjacent_seats):
                    new_layout[y][x] = '#'
                elif chr == '#' and adjacent_seats.count('#') >= 4:
                    new_layout[y][x] = 'L'
                
    return sum(row.count('#') for row in layout)

def part2(layout=[row[:] for row in layout]):
    new_layout = None
    positions = {}
    while layout != new_layout:
        if new_layout is not None:
            layout = new_layout
        new_layout = [row[:] for row in layout]
        for y, row in enumerate(layout):
            for x, chr in enumerate(row):
                adjacent_seats = []
                if (x, y) not in positions:
                    positions[(x, y)] = []
                    for x_adj in range(-1, 2):
                        for y_adj in range(-1, 2):
                            if (x_adj != 0 or y_adj != 0) and 0 <= x + x_adj < len(row) and 0 <= y + y_adj < len(layout):
                                x_search = x
                                y_search = y
                                while True:
                                    x_search += x_adj
                                    y_search += y_adj
                                    if x_search >= 0 and y_search >= 0:
                                        try:
                                            if layout[y_search][x_search] != '.':
                                                adjacent_seats.append(layout[y_search][x_search])
                                                positions[(x, y)].append((x_search, y_search))
                                                break
                                        except IndexError:
                                            adjacent_seats.append('.')
                                            break
                                    else:
                                        adjacent_seats.append('.')
                                        break
                else:
                    for x_pos, y_pos in positions[(x, y)]:
                        adjacent_seats.append(layout[y_pos][x_pos])
                if chr == 'L' and all(c != '#' for c in adjacent_seats):
                    new_layout[y][x] = '#'
                elif chr == '#' and adjacent_seats.count('#') >= 5:
                    new_layout[y][x] = 'L'
                
    return sum(row.count('#') for row in layout)

print("part 1:", part1())
print("part 2:", part2())
print("time for part 1:", timeit.timeit(part1, number=1))
print("time for part 2:", timeit.timeit(part2, number=1))
