from dataclasses import dataclass

class Grid:
    def __init__(self, initial_2d_slice):
        self.grid = {0: {0: self.parse(initial_2d_slice)}}
        self.xbounds = [0, len(self.grid[0][0][0])]
        self.ybounds = [0, len(self.grid[0][0])]
        self.zbounds = [0, 1]
        self.wbounds = [0, 1]

    def parse(self, string):
        grid_2d = {}
        for index, line in enumerate(string.strip().split('\n')):
            grid_2d[index] = {i: (ch == '#') for i, ch in enumerate(line)}
        return grid_2d

    def cycle(self):
        newgrid = {}
        for w in self.bigger_range(*self.wbounds):
            newgrid[w] = {}
            for z in self.bigger_range(*self.zbounds):
                newgrid[w][z] = {}
                for y in self.bigger_range(*self.ybounds):
                    newgrid[w][z][y] = {}
                    for x in self.bigger_range(*self.xbounds):
                        cube = self[x, y, z, w]
                        neighbour_count = list(self.neighbours_of(x, y, z, w)).count(True)
                        if cube:
                            if neighbour_count == 2 or neighbour_count == 3:
                                newgrid[w][z][y][x] = True
                            else:
                                newgrid[w][z][y][x] = False
                        else:
                            if neighbour_count == 3:
                                newgrid[w][z][y][x] = True
                            else:
                                newgrid[w][z][y][x] = False
            
        self.grid = newgrid
        self.xbounds = [self.xbounds[0]-1, self.xbounds[1]+1]
        self.ybounds = [self.ybounds[0]-1, self.ybounds[1]+1]
        self.zbounds = [self.zbounds[0]-1, self.zbounds[1]+1]
        self.wbounds = [self.wbounds[0]-1, self.wbounds[1]+1]

    def neighbours_of(self, x, y, z, w):
        for w_offset in range(-1, 2):
            if w + w_offset in range(*self.wbounds):
                for z_offset in range(-1, 2):
                    if z + z_offset in range(*self.zbounds):
                        for y_offset in range(-1, 2):
                            if y + y_offset in range(*self.ybounds):
                                for x_offset in range(-1, 2):
                                    if x + x_offset in range(*self.xbounds) and not (w_offset == z_offset == y_offset == x_offset == 0):
                                        yield self[x + x_offset,
                                                   y + y_offset,
                                                   z + z_offset,
                                                   w + w_offset]

    def bigger_range(self, *bounds):
        yield min(bounds) - 1
        yield from range(*bounds)
        yield max(bounds)

    def count_active(self):
        count = 0
        for w in range(*self.wbounds):
            for z in range(*self.zbounds):
                for y in range(*self.ybounds):
                    for x in range(*self.xbounds):
                        if self[x, y, z, w]:
                            count += 1
        return count

    def __getitem__(self, index):
        x, y, z, w = index
        try:
            return self.grid[w][z][y][x]
        except KeyError:
            return False

    def __str__(self):
        s = ""
        for w in sorted(self.grid.keys()):
            for z in sorted(self.grid[w].keys()):
                s += f"z={z}, w={w}\n"
                for y in sorted(self.grid[w][z].keys()):
                    s += "".join(('#' if self.grid[w][z][y][x] else '.') for x in sorted(self.grid[w][z][y].keys()))
                    s += "\n"
                s += "\n"
        return s


with open("day17.in") as f:
    grid = Grid(f.read())

for _ in range(6):
    grid.cycle()
print(grid.count_active())
