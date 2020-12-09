preamble_size = 25

nums = []
with open("day9.in") as f:
    for line in f:
        nums.append(int(line.strip()))

number = 0
for offset_index, num in enumerate(nums[preamble_size:]):
    index = offset_index + preamble_size
    preamble = nums[index-preamble_size:index]
    found = False
    for n1 in preamble:
        for n2 in preamble:
            if n1 + n2 == num:
                found = True
                break
        if found:
            break
    if not found:
        number = num
        break

print(number)

found = False
bounds = None
for index_start, num1 in enumerate(nums):
    sum = 0
    for offset_index_end, num2 in enumerate(nums[index_start:]):
        index_end = offset_index_end + index_start
        sum += num2
        if sum > number:
            break
        elif sum == number:
            found = True
            bounds = (index_start, index_end)
            break
    if found:
        break
print(bounds)
# bounds are inclusive
rg = nums[bounds[0]:bounds[1]+1]
print(min(rg) + max(rg))
