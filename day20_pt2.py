from collections import deque
from dataclasses import dataclass
from enum import Enum
from typing import Optional, List, Union
from pprint import pprint
import time
import sys
import re


class Edge(Enum):
    TOP = 0
    RIGHT = 1
    BOTTOM = 2
    LEFT = 3

    def __str__(self):
        return self.name

    def opposite(self):
        if self == Edge.TOP:
            return Edge.BOTTOM
        elif self == Edge.BOTTOM:
            return Edge.TOP
        elif self == Edge.LEFT:
            return Edge.RIGHT
        elif self == Edge.RIGHT:
            return Edge.LEFT

class Tile:
    def __init__(self, tile_id: int, grid: List[str]):
        self.tile_id = tile_id
        self.grid = grid
        self.adjacent_tiles = {
            Edge.TOP: None,
            Edge.RIGHT: None,
            Edge.BOTTOM: None,
            Edge.LEFT: None
        }

    def get_edge(self, edge: Edge):
        if edge == Edge.TOP:
            return self.grid[0]
        elif edge == Edge.BOTTOM:
            return ''.join(reversed(self.grid[-1]))
        elif edge == Edge.LEFT:
            return ''.join(reversed([row[0] for row in self.grid]))
        elif edge == Edge.RIGHT:
            return ''.join([row[-1] for row in self.grid])

    def rotate(self):
        "rotates 90 degrees clockwise"
        self.adjacent_tiles = {
            Edge.TOP: self.adjacent_tiles[Edge.LEFT],
            Edge.RIGHT: self.adjacent_tiles[Edge.TOP],
            Edge.BOTTOM: self.adjacent_tiles[Edge.RIGHT],
            Edge.LEFT: self.adjacent_tiles[Edge.BOTTOM]
        }
        self.grid = [
            ''.join([row[i] for row in reversed(self.grid)])
            for i in range(len(self.grid))
        ]

    def flip(self):
        temp = self.adjacent_tiles[Edge.TOP]
        self.adjacent_tiles[Edge.TOP] = self.adjacent_tiles[Edge.BOTTOM]
        self.adjacent_tiles[Edge.BOTTOM] = temp

        self.grid = list(reversed(self.grid))

    def __repr__(self):
        s = f"Tile({self.tile_id}, {{"
        adjacent_tiles_str = []
        for edge, tile in self.adjacent_tiles.items():
            if tile is None:
                adjacent_tiles_str.append(f"{edge}: {tile}")
            else:
                adjacent_tiles_str.append(f"{edge}: {tile.tile_id}")
        s += ", ".join(adjacent_tiles_str)
        s += "})"
        return s

    def grid_str(self):
        no_border_grid = [
            row[1:-1]
            for row in self.grid[1:-1]
        ]
        return "\n".join(no_border_grid)

    def grid_dbg(self):
        s = "\n".join(self.grid)
        l = list(s)
        l[36:40] = list(str(self.tile_id))
        return ''.join(l)

    def combine_h_dbg(self, *others):
        return '\n'.join([
            ' '.join(lines)
            for lines in zip(self.grid_dbg().split(), *[other.grid_dbg().split() for other in others])])

    def combine_h(self, *others):
        return '\n'.join([
            ''.join(lines)
            for lines in zip(self.grid_str().split(), *[other.grid_str().split() for other in others])])

@dataclass
class UnresolvedTileMatch:
    tile: Tile
    flipped: bool

    @property
    def tile_id(self):
        return self.tile.tile_id

    def flip(self):
        self.tile.flip()

    def rotate(self):
        self.tile.rotate()

@dataclass
class TileWithEdge:
    tile: Union[Tile, UnresolvedTileMatch]
    edge: Edge

    @property
    def tile_id(self):
        return self.tile.tile_id

    def flip(self):
        self.tile.flip()
        if self.edge == Edge.TOP:
            self.edge = Edge.BOTTOM
        elif self.edge == Edge.BOTTOM:
            self.edge = Edge.TOP

    def rotate(self):
        self.tile.rotate()
        if self.edge == Edge.TOP:
            self.edge = Edge.RIGHT
        elif self.edge == Edge.RIGHT:
            self.edge = Edge.BOTTOM
        elif self.edge == Edge.BOTTOM:
            self.edge = Edge.LEFT
        elif self.edge == Edge.LEFT:
            self.edge = Edge.TOP

tiles = {}
with open("day20.in") as f:
    tile_id = None
    tile = []
    for line in f:
        if not line.strip():
            tiles[tile_id] = Tile(tile_id, tile)
            tile = []
        elif line.startswith("Tile"):
            tile_id = int(line.split(" ")[1][:-2])  # remove colon and newline
        else:
            tile.append(line.strip())
    tiles[tile_id] = Tile(tile_id, tile)
#tiles[1951].flip()

matches = {tid: [] for tid in tiles}
for tile_id, tile in tiles.items():
    for tile2_id, tile2 in tiles.items():
        if tile_id != tile2_id:
            for edge1 in Edge:
                for edge2 in Edge:
                    if tile.get_edge(edge1) == tile2.get_edge(edge2):
                        # they align when stacked, so one has to be flipped
                        utm = UnresolvedTileMatch(tile2, flipped=True)
                        matches[tile_id].append(utm)
                        tile.adjacent_tiles[edge1] = TileWithEdge(utm, edge2)
                    elif tile.get_edge(edge1) == ''.join(reversed(tile2.get_edge(edge2))):
                        utm = UnresolvedTileMatch(tile2, flipped=False)
                        matches[tile_id].append(utm)
                        tile.adjacent_tiles[edge1] = TileWithEdge(utm, edge2)

# pick a corner
corner_id = next(tid for tid, match in matches.items() if len(match) == 2)
corner = tiles[corner_id]

# first the corner needs to be lined up with the top left corner
while not (
    corner.adjacent_tiles[Edge.TOP] is None and
    corner.adjacent_tiles[Edge.LEFT] is None
):
    corner.rotate()

# now resolve the rest based on the corner
resolved = {corner_id}
queue = deque()
for edge, tile in corner.adjacent_tiles.items():
    if tile is not None:
        queue.append((False, edge.opposite(), tile))

while queue:
    was_flipped, target_edge, tile = queue.popleft()
    if tile.tile_id in resolved:
        continue
    # at this point, tile is probably a TileWithEdge with tile type UnresolvedTileMatch
    # actually i can't think of any reason it wouldn't be
    # i'm going to assume that it is. if it isn't my program will crash anyway
    previous_tile = tile.tile.tile.adjacent_tiles[tile.edge]    # lol
    # there's probably a much better way to design this model

    if tile.tile.flipped != was_flipped:
        tile.flip()
        tile.tile.flipped = True
    else:
        tile.tile.flipped = False

    while tile.edge != target_edge:
        tile.rotate()
    actual_tile = tile.tile.tile
    resolved.add(actual_tile.tile_id)

    for edge, adjacent_tile in actual_tile.adjacent_tiles.items():
        if adjacent_tile is not None and edge != target_edge and adjacent_tile.tile_id not in resolved:
            queue.append((tile.tile.flipped, edge.opposite(), adjacent_tile))

# unwrap all the tiles bc they're done
for tile in tiles.values():
    for key, adjacent_tile in tile.adjacent_tiles.items():
        try:
            tile.adjacent_tiles[key] = adjacent_tile.tile.tile
        except AttributeError:
            try:
                tile.adjacent_tiles[key] = adjacent_tile.tile
            except AttributeError:
                pass

# construct the image
leftmost = corner
image = ""
while leftmost is not None:
    right_tiles = []
    current_tile = leftmost
    while True:
        next_tile = current_tile.adjacent_tiles[Edge.RIGHT]
        if next_tile is None:
            break
        else:
            right_tiles.append(next_tile)
            current_tile = next_tile
    image += leftmost.combine_h(*right_tiles)
    image += "\n"
    leftmost = leftmost.adjacent_tiles[Edge.BOTTOM]
print(image)
image = image[:-1]  # strip trailing newline

# i have the image!
# now to find monsters

def image_orientations(img, recurse=True):
    grid = img.split("\n")
    yield img
    yield img[::-1]
    yield '\n'.join(
        [line[::-1] for line in grid]
    )
    yield '\n'.join(
        [line[::-1] for line in reversed(grid)]
    )
    if recurse:
        yield from image_orientations(
            '\n'.join(
                [
                    ''.join([row[i] for row in grid])
                    for i in range(len(grid))
                ]
            ),
            recurse=False
        )

monster_pattern = re.compile(
    r"..................#.+\n"
    r"#....##....##....###.+\n"
    r".#..#..#..#..#..#"
)

min_count = 9999
for img in image_orientations(image):
    nhashes = img.count('#')
    smallimg = img
    while smallimg.strip():
        nhashes -= 15 * len(monster_pattern.findall(smallimg))
        smallimg = '\n'.join([line[1:] for line in smallimg.split('\n')])
    min_count = min(nhashes, min_count)
    
print(min_count)
