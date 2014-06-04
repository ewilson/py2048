from itertools import groupby
from random import choice,randint

class Board(object):
    def __init__(self):
        self.tiles = {}

    def slide(self, dir):
        prior = self.tiles.copy()
        if dir == 'L':
            self._slide_left()
        elif dir == 'R':
            self._flip_horiz()
            self._slide_left()
            self._flip_horiz()
        elif dir == 'U':
            self._transpose()
            self._slide_left()
            self._transpose()
        elif dir == 'D':
            self._transpose()
            self._flip_horiz()
            self._slide_left()
            self._flip_horiz()
            self._transpose()
        return not self.tiles == prior

    def place_random(self):
        empties = self._find_empty_squares()
        if empties:
            key = choice(empties)
            val = randint(1,2)*2
            self.tiles[key] = val
        return empties
    
    def _flip_horiz(self):
        self.tiles = {(x,3-y):self.tiles[(x,y)] for (x,y) in self.tiles}

    def _transpose(self):
        self.tiles = {(y,x):self.tiles[(x,y)] for (x,y) in self.tiles}

    def _find_groups(self):
        keys = self.tiles.keys()
        keys = sorted(keys, key=lambda x: x[0])
        groups = []
        for k, group in groupby(keys, key=lambda x: x[0]):
            groups.append(sorted(list(group), key=lambda x: x[1]))
        return groups

    def _slide_left(self):
        groups = self._find_groups()

        for group in groups:
            previous_val = -1
            previous_key = None
            merges = 0
            for idx, key in enumerate(group):
                if self.tiles[key] == previous_val:
                    self.tiles[previous_key] = 2*previous_val
                    del self.tiles[key]
                    merges += 1
                    previous_val = -1
                else:
                    pos = idx - merges
                    newkey = (key[0],pos)
                    if newkey != key:
                        self.tiles[newkey] = self.tiles[key]
                        del self.tiles[key]
                    previous_key = newkey
                    previous_val = self.tiles[newkey]

    def _find_empty_squares(self):
        empties = []
        for row in range(4):
            for col in range(4):
                if (row,col) not in self.tiles:
                    empties.append((row,col))
        return empties