from dataclasses import dataclass
import cmath
import math
import numpy as np

@dataclass
class Instruction:
    action: str
    value: int

instrs = []
with open("day12.in") as f:
    for line in f:
        instrs.append(Instruction(line[0], int(line[1:].strip())))

pos = [0, 0]
dir = 0  # east
for instr in instrs:
    if instr.action == "N":
        pos[0] += instr.value
    if instr.action == "S":
        pos[0] -= instr.value
    if instr.action == "E":
        pos[1] += instr.value
    if instr.action == "W":
        pos[1] -= instr.value
    if instr.action == "L":
        dir += instr.value
    if instr.action == "R":
        dir -= instr.value
    if instr.action == "F":
        pos[0] += instr.value * np.sin(np.radians(dir))
        pos[1] += instr.value * np.cos(np.radians(dir))

print(round(abs(pos[0]) + abs(pos[1])))


def rotate_point_complex(point, degrees):
    return point * cmath.rect(1, np.radians(degrees))

# 1 unit north and 10 units east
waypoint = 10+1j
pos = 0+0j
for instr in instrs:
    if instr.action == "N":
        waypoint += instr.value * 1j
    if instr.action == "S":
        waypoint -= instr.value * 1j
    if instr.action == "E":
        waypoint += instr.value
    if instr.action == "W":
        waypoint -= instr.value
    if instr.action == "L":
        waypoint = rotate_point_complex(waypoint, instr.value)
    if instr.action == "R":
        waypoint = rotate_point_complex(waypoint, -instr.value)
    if instr.action == "F":
        pos += waypoint.real * instr.value
        pos += waypoint.imag * instr.value * 1j

print(round(abs(pos.real) + abs(pos.imag)))
