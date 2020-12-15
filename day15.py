with open("day15.in") as f:
    orig_nums = [int(i) for i in f.read().split(",")]

idx = len(orig_nums)
nums = orig_nums[:]
for i in range(idx, 2020):
    last_num = nums[-1]
    for index, num in enumerate(reversed(nums[:-1])):
        if num == last_num:
            nums.append(index + 1)
            break
    else:
        nums.append(0)
print(nums[-1])

nums = orig_nums[:]
old_positions = {}
positions = {num: idx for idx, num in enumerate(nums)}
for i in range(idx, 30000000):
    last_num = nums[-1]
    if last_num in positions:
        new_num = i - positions[last_num] - 1
    else:
        new_num = 0
    nums.append(new_num)
    positions[last_num] = i - 1
print(nums[-1])
