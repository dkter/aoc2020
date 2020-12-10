from collections import deque

ratings = []
with open("day10.in") as f:
    for line in f:
        ratings.append(int(line.strip()))

ratings.sort()
ratings.append(max(ratings) + 3)

diffs = {1: 0, 2: 0, 3: 0}
last_rating = 0
for rating in ratings:
    diffs[rating - last_rating] += 1
    last_rating = rating
print(diffs)
print(diffs[1] * diffs[3])

del ratings[-1]
ratings = [0] + ratings
count = 0
queue = deque([(0, 0)])
local_counts = {}
while queue:
    index, item = queue.popleft()
    local_count = local_counts.get((index, item), 1)
    if index == len(ratings) - 1:
        if item == ratings[-1]:
            count = local_count
            break
    else:
        try:
            next_item = ratings[index + 1]
        except IndexError:
            continue
        if next_item - item <= 3:
            if (index, item) not in queue:
                queue.append((index + 1, item))
                queue.append((index + 1, next_item))
                local_counts[(index + 1, item)] = local_counts.get((index + 1, item), 0) + local_count
                local_counts[(index + 1, next_item)] = local_counts.get((index + 1, next_item), 0) + local_count
print(count)
