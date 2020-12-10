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

# del ratings[-1]
# ratings = [0] + ratings
# count = 0
# queue = deque([[0]])
# items = set()
# while queue:
#     #print(queue)
#     item = queue.popleft()
#     if len(item) == len(ratings) and item[-1] == ratings[-1]:
#         print(item)
#         items.add(tuple(item))
#     else:
#         print(ratings, item, len(ratings), len(item))
#         try:
#             for i in range(ratings[len(item)], ratings[len(item)-1], -1):
#                 new_item = item[:]
#                 new_item.append(i)
#                 queue.append(new_item)
#         except IndexError:
#             pass
# print(items, len(items))

del ratings[-1]
ratings = [0] + ratings
count = 0
queue = deque([(0, 0)])
#items = set()
indices = {}
options_after = {}
calculation_done = {i: False for i in range(len(ratings))}
visited = set()
local_counts = {}
while queue:
    #print(queue)
    index, item = queue.popleft()
    local_count = local_counts.get((index, item), 1)
    #print(index, end=' ')
    # try:
    #     indices[index] += 1
    # except KeyError:
    #     indices[index] = 1
    #     if index != 0:
    #         print(f'({index})', item, queue)#, indices[index - 1], index, item, end=' ')
    #visited.add(item)
        #print(queue)
    if index == len(ratings) - 1:
        if item == ratings[-1]:
            #print(item)
            #items.add(tuple(item))
            #print("+")
            #print(local_count)
            count = local_count
            # for index2, i in enumerate(item):
            #     pass
        # else:
        #     print("F(1)")
        #     if item in visited:
        #         options_after[item[-1]] = 1
    else:
        #print(ratings, item, len(ratings), len(item))
        try:
            next_item = ratings[index + 1]
        except IndexError:
            continue
        if next_item - item <= 3:
            # if (index + 1, item) in queue:
            #     local_counts[(index + 1, item)] += 1
            # else:
            #     local_counts[(index + 1, item)] = 1
            #     queue.append((index + 1, item))
            # if (index + 1, next_item) in queue:
            #     local_counts[(index + 1, next_item)] += 1
            # else:
            #     local_counts[(index + 1, next_item)] = 1
            #     queue.append((index + 1, next_item))
            #print(local_counts)
            if (index, item) in queue:
                pass
                #print(queue)
                # try:
                #     print(index, item, local_count, "adding")
                #     local_counts[(index, item)] += local_count
                #     #local_counts[(index, next_item)] += local_count
                # except KeyError:
                #     print("hmm", index, item, local_count)
                #     local_counts[(index, item)] = 2 * local_count
                #     #local_counts[(index, next_item)] = 2 * local_count
            else:
                queue.append((index + 1, item))
                queue.append((index + 1, next_item))
                local_counts[(index + 1, item)] = local_counts.get((index + 1, item), 0) + local_count
                local_counts[(index + 1, next_item)] = local_counts.get((index + 1, next_item), 0) + local_count
                # local_counts[(index + 1, item)] = local_count
                # local_counts[(index + 1, next_item)] = local_count
                # if (index+1, item) == (5, 7) or (index+1, next_item) == (5, 7):
                #     print("adding to (5, 7) -- i'm", (index, item), local_count)
                # if (index+1, item) == (4, 6) or (index+1, next_item) == (4, 6):
                #     print("adding to (4, 6) -- i'm", (index, item), local_count)
        # else: 
        #     print("F(2)")
        #     if item in visited:
        #         options_after[item[-1]] = 1
#print(len(items))
# print(local_counts)
# print()
print(count)
#print(indices)
