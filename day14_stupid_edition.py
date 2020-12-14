import re
import sys
import importlib
from importlib.abc import SourceLoader
from importlib.machinery import FileFinder
from itertools import product


class Mem:
    def __init__(self, module_namespace):
        self.module_namespace = module_namespace
        self.mem_part1 = {}
        self.mem_part2 = {}

    def __setitem__(self, key, value):
        self._part1_set(key, value)
        self._part2_set(key, value)

    def _part1_set(self, addr, value):
        mask = self.module_namespace.mask
        self.mem_part1[addr] = value
        for index, c in enumerate(reversed(mask)):
            if c == "1":
                self.mem_part1[addr] |= 1 << index
            elif c == "0":
                self.mem_part1[addr] &= ~(1 << index)

    def _part2_set(self, addr, value):
        # this is slightly less efficient than my original day 14b solution,
        # because it redoes the mask calculation every time the memory is set,
        # instead of when the mask is set. unfortunately, python doesn't let you
        # overload assignment. sad. actually i'm not mad about this because
        # that would be stupid
        mask = self.module_namespace.mask
        actual_mask = int(mask.replace("X", "0"), 2)
        x_indices = [idx for idx, ch in enumerate(mask) if ch == "X"]
        bit_combinations = product(range(2), repeat=len(x_indices))
        mask_combinations = []
        for combination in bit_combinations:
            mask_combination = 0
            for bit, idx in zip(combination, x_indices):
                mask_combination |= bit << (35 - idx)
            mask_combinations.append(mask_combination)

        for mask_combination in mask_combinations:
            actual_addr = (addr | actual_mask) ^ mask_combination
            self.mem_part2[actual_addr] = value

    @property
    def part1(self):
        return sum(self.mem_part1.values())

    @property
    def part2(self):
        return sum(self.mem_part2.values())

    def __str__(self):
        return f"part 1: {self.part1}\npart 2: {self.part2}"


class Day14Loader(SourceLoader):
    def __init__(self, fullname, path):
        self.fullname = fullname
        self.path = path

    def get_filename(self, fullname):
        return self.path

    def get_data(self, filename):
        with open(filename) as f:
            program = f.read()
        # okay this is kind of cheating
        # i need to change the masks to string literals because most of them
        # aren't valid integer literals in python
        better_program = re.sub(r"mask = ([01X]+)",
                                r"mask = '\1'",
                                program)
        return better_program

    def exec_module(self, module):
        module.mem = Mem(module)
        super().exec_module(module)


hook = FileFinder.path_hook((Day14Loader, [".in", ".py"]))
sys.path_hooks.insert(0, hook)
sys.path_importer_cache.clear()
importlib.invalidate_caches()


# okay. ignore everything i wrote above. this is where the REAL program starts
import day14_input
print(day14_input.mem)
