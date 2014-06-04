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

    def _find_groups(self, axis):
        primary = axis[0]
        secondary = axis[1]
        keys = self.tiles.keys()
        keys = sorted(keys, key=lambda x: x[primary])
        groups = []
        for k, group in groupby(keys, key=lambda x: x[primary]):
            groups.append(sorted(list(group), key=lambda x: x[secondary]))
        return groups, primary

    def _slide(self,axis):
        groups, primary = self._find_groups(axis)

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
                    newkey = (key[primary],pos) if primary == 0 else (pos,key[primary])
                    if newkey != key:
                        self.tiles[newkey] = self.tiles[key]
                        del self.tiles[key]
                    previous_key = newkey
                    previous_val = self.tiles[newkey]
