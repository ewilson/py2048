from itertools import groupby

class Board(object):
    def __init__(self):
        self.tiles = {}

    def slide_left(self):
        self._slide()

    def slide_right(self):
        self._flip_horiz()
        self._slide()
        self._flip_horiz()

    def slide_up(self):
        self._transpose()
        self._slide()
        self._transpose()

    def slide_down(self):
        self._transpose()
        self._flip_horiz()
        self._slide()
        self._flip_horiz()
        self._transpose()

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

    def _slide(self):
        groups = self._find_groups()

        for group in groups:
            previous_val = -1
            previous_key = None
            merges = 0
            for idx, key in enumerate(group):
                print previous_val
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
