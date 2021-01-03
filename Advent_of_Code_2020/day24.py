"""
---PART ONE---
"""

class Position(object):
    def __init__(self, x = 0, y = 0):
        self.x = x
        self.y = y

    def __str__(self):
        return '(' + str(self.x) + ', ' + str(self.y) + ')'

    def get_coord(self):
        return (self.x, self.y)

    def __eq__(self, other):
        return self.get_coord() == other.get_coord()
    
    # to make position an hashable type
    def __hash__(self):
        return self.get_coord().__hash__()

    def move(self, direction):
        if len(direction) == 1:
            if direction == 'e':
                self.x += 1
            else: # w
                self.x -= 1
        # two letters
        else: 
            for el in direction:
                if el == 'e':
                    self.x += 0.5
                elif el == 'w':  # w
                    self.x -= 0.5
                elif el == 'n':
                    self.y += 0.5
                elif el == 's':
                    self.y -= 0.5


def parse(line):
    line = list(line)

    res = []
    i = 0
    while 1:
        if i >= len(line): break
        if line[i] == 'e' or line[i] == 'w':
            res.append(line[i])
        else:   
            res.append(line[i] + line[i + 1])
            i += 1
        i += 1
        
    return res


def play(fd):
    lines = fd.read().rstrip().split('\n')
    # contains black tiles
    black_tiles = set(())
    for line in lines:
        position = Position()
        # parse line separating instructions
        instrs = parse(line)
        for instr in instrs:
            position.move(instr)

        if position in black_tiles:
            # it means that I flipped the tile two times, so it's
            # not black anymore
            black_tiles.remove(position)
        else:
            black_tiles.add(position)
    
    return len(black_tiles)


fd = open("day24.txt")
print(play(fd))