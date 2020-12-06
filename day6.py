from operator import or_, and_
from functools import reduce

answers = []
group = set()
with open("day6.in") as f:
    for line in f:
        if not line.strip():
            answers.append(group)
            group = set()
        else:
            group.add(frozenset(line.strip()))

answers.append(group)

total = 0
for group in answers:
    flattened_ans = reduce(or_, group, set())
    total += len(flattened_ans)
print(total)

total = 0
for group in answers:
    flattened_ans = reduce(and_, group, set("abcdefghijklmnopqrstuvwxyz"))
    total += len(flattened_ans)
print(total)
