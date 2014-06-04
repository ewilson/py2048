from itertools import groupby

class Board(object):
    def __init__(self):
        self.tiles = {}

    # def __repr__(self):
    #     return repr(self.m)

    def slide_left(self):
        self._slide((0,1))

    def slide_right(self):
        self._flip_horiz()
        self._slide((0,1))
        self._flip_horiz()

    def slide_up(self):
        self._slide((1,0))

    def slide_down(self):
        self._flip_vert()
        self._slide((1,0))
        self._flip_vert()

    def _flip_horiz(self):
        self.tiles = {(x,3-y):self.tiles[(x,y)] for (x,y) in self.tiles}

    def _flip_vert(self):
        self.tiles = {(3-x,y):self.tiles[(x,y)] for (x,y) in self.tiles}

    def _slide(self,axis):
        primary = axis[0]
        secondary = axis[1]
        keys = self.tiles.keys()
        keys = sorted(keys, key=lambda x: x[primary])
        groups = []
        for k, group in groupby(keys,key=lambda x: x[primary]):
            groups.append(sorted(list(group), key=lambda x: x[secondary]))

        for row in groups:
            for idx, key in enumerate(row):
                newkey = (key[primary],idx) if primary == 0 else (idx,key[primary])
                if newkey != key:
                    self.tiles[newkey] = self.tiles[key]
                    del self.tiles[key]

