from dataclasses import dataclass
from itertools import product

with open("day14.in") as f:
    lines = f.readlines()

mem = {}
mask = ""
for line in lines:
    if line.startswith("mask = "):
        mask = line.split(" = ")[1].strip()
    else:
        addr, val = (int(i) for i in line.lstrip("me[").strip().split("] = "))
        mem[addr] = val
        for index, c in enumerate(reversed(mask)):
            if c == "1":
                mem[addr] |= 1 << index
            elif c == "0":
                mem[addr] &= ~(1 << index)

print(sum(mem.values()))


actual_mask = 0
mask = ""
mask_combinations = []
mem = {}
for line in lines:
    if line.startswith("mask = "):
        mask = line.split(" = ")[1].strip()
        actual_mask = int(mask.replace("X", "0"), 2)
        xs = [idx for idx, ch in enumerate(mask) if ch == "X"]
        idx_combinations = product(range(2), repeat=len(xs))
        mask_combinations = []
        for combination in idx_combinations:
            mask_combination = 0
            for bit, idx in zip(combination, xs):
                mask_combination |= bit << (35 - idx)
            mask_combinations.append(mask_combination)
    else:
        addr, val = (int(i) for i in line.lstrip("me[").strip().split("] = "))
        for mask_combination in mask_combinations:
            actual_addr = (addr | actual_mask) ^ mask_combination
            mem[actual_addr] = val
        

print(sum(mem.values()))
