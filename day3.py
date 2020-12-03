lines = []
with open("day3.in") as f:
    lines = [l.strip() for l in f.readlines()]

line_length = len(lines[0])

def count_trees(xstep, ystep):
    x = 0
    y = 0
    tree_count = 0
    for line in lines:
        if y % ystep != 0:
            y += 1
            continue
        chars = list(line)
        if x >= line_length:
            x -= line_length
        if line[x] == '#':
            tree_count += 1
        x += xstep
        y += 1
    return tree_count

# part A
print(count_trees(3, 1))

# part B
print(count_trees(1, 1),
    count_trees(3, 1),
    count_trees(5, 1),
    count_trees(7, 1),
    count_trees(1, 2))

print(count_trees(1, 1)
    * count_trees(3, 1)
    * count_trees(5, 1)
    * count_trees(7, 1)
    * count_trees(1, 2))
