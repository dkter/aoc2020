import re
from collections import deque

bags = {}
pattern = re.compile(r"( (?P<number>\d) (?P<name>.+?) bags?[,.])")
with open("day7.in") as f:
    for line in f:
        bag, contents = line.strip().split(" bags contain")
        if not pattern.match(contents):
            bags[bag] = []
        for match in pattern.findall(contents):
            if bag in bags:
                bags[bag].append((int(match[1]), match[2]))
            else:
                bags[bag] = [(int(match[1]), match[2])]

count = 0
for bag in bags:
    visited = set()
    queue = deque(bags[bag])
    while queue:
        current_bag = queue.popleft()
        if current_bag[1] == "shiny gold":
            count += 1
            break
        visited.add(current_bag)
        for contained in bags[current_bag[1]]:
            if contained not in visited:
                queue.append(contained)

print(count)


number_of_bags = {bname: None for bname in bags}
done = False
while not done:
    done = True
    for bag in bags:
        if len(bags[bag]) == 0:
            number_of_bags[bag] = 0
        else:
            total = 0
            for bag2 in bags[bag]:
                if number_of_bags[bag2[1]] is None:
                    done = False
                    break
                else:
                    total += (number_of_bags[bag2[1]] + 1) * bag2[0]
            else:
                number_of_bags[bag] = total

print(number_of_bags['shiny gold'])
