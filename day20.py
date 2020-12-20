import math
from dataclasses import dataclass

@dataclass
class Orientation:
    flipped: bool
    direction: int   # 0, 90, 180, 270 clockwise referring to top

    def __repr__(self):
        return "{" + str(self.direction) + ("f" if self.flipped else "") + "}"

possible_orientations = [
    Orientation(False, 0),
    Orientation(False, 90),
    Orientation(False, 180),
    Orientation(False, 270),
    Orientation(True, 0),
    Orientation(True, 90),
    Orientation(True, 180),
    Orientation(True, 270)
]

def get_left_col(grid):
    return [row[0] for row in grid]

def get_right_col(grid):
    return [row[-1] for row in grid]

def get_borders(grid):
    yield (list(grid[0]), Orientation(False, 0))
    yield (list(grid[-1]), Orientation(False, 180))
    yield (list(reversed(grid[0])), Orientation(True, 0))
    yield (list(reversed(grid[-1])), Orientation(True, 180))
    yield (get_left_col(grid), Orientation(False, 270))
    yield (list(reversed(get_left_col(grid))), Orientation(True, 270))
    yield (get_right_col(grid), Orientation(False, 90))
    yield (list(reversed(get_right_col(grid))), Orientation(True, 90))


tiles = {}
with open("day20.in") as f:
    tile_id = None
    tile = []
    for line in f:
        if not line.strip():
            tiles[tile_id] = tile
            tile = []
        elif line.startswith("Tile"):
            tile_id = int(line.split(" ")[1][:-2])  # remove colon and newline
        else:
            tile.append(line.strip())
    tiles[tile_id] = tile

grid_size = int(math.sqrt(len(tiles)))

matches = {tid: [] for tid in tiles}
for tile_id, tile in tiles.items():
    for tile2_id, tile2 in tiles.items():
        if tile_id != tile2_id:
            for border1, orientation1 in get_borders(tile):
                for border2, orientation2 in get_borders(tile2):
                    if border1 == border2:
                        matches[tile_id].append((tile2_id, orientation1, orientation2))

product = 1
corners = []
for tile_id, match in matches.items():
    if len(match) == 4:
        # got lucky here
        # (4, not 2, because you can always flip both tiles)
        product *= tile_id
        corners.append(tile_id)
print("part 1:", product)
