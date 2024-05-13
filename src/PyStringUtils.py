import math

class stats:
    def __init__(self, string, width = None, splitted = False) -> None:
        if not splitted:
            self.characters = len(string) - string.count('\n')        
            self.lines = string.count('\n') + 1
            self.linelist = string.split('\n')

        else:
            self.characters = sum([len(word) for word in string])
            self.lines = len(string)
            self.linelist = string

        self.maxcharinline = len(max(self.linelist, key=len))

        if not(width == None):
            self.width = width
        else:
            self.width = self.maxcharinline + 4

        self.height = self.lines + 2

    def fillspace(self, length, string):
        got = len(string)
        need = length
        fill = need - got

        del got, need
        return fill
    
    def splitspace(self, length, string):
        got = len(string)
        fill = length - got

        half = fill / 2
        split1 = math.floor(half)
        split2 = math.ceil(half)

        return (split1, split2)
        

def boxify(string, width = None, align = "left", listed = False):
    if not(width == None):
        stat = stats(string, width = width)
    else:
        stat = stats(string)

    belt = list()
    
    topline = '.' + ('-' * (stat.width - 2)) + '.'
    belt.append(topline)

    if align in ("left", "l"):
        for line in stat.linelist:
            bwline = '| ' + line + (' ' * stat.fillspace(stat.width - 4, line)) + ' |'
            belt.append(bwline)

    elif align in ("right", "r"):
        for line in stat.linelist:
            bwline = '| ' + (' ' * stat.fillspace(stat.width - 4, line)) + line + ' |'
            belt.append(bwline)

    elif align in ("centre", "center", "c"):
        for line in stat.linelist:
            bwline = '| ' + (' ' * stat.splitspace(stat.width - 4, line)[0]) + line + (' ' * stat.splitspace(stat.width - 4, line)[1]) + ' |'
            belt.append(bwline)

    else:
        raise ValueError('Invalid align method is passed.')

    bottomline = "'" + ('-' * (stat.width - 2)) + "'"
    belt.append(bottomline)

    if not listed:
        final = '\n'.join(belt)
        return final
    else:
        return belt
    
def combine(belt):
    return "\n".join(belt)

def tablify(grid, rowsplit = False):
    for row in grid:
        if not type(row) in (list, tuple):
            raise TypeError(f"Invalid row data type has been passed {row} type : {type(row)}")
    else:
        pass

    prevlength = None
    for row in grid:
        if (not (prevlength == None)) and (not (prevlength == len(row))):
            raise ValueError(f"Row doesn't follow the dimensions \n{row}")
        else:
            prevlength = len(row)

    tiltedgrid = []
    for columnindex in range(len(grid[0])):
        column = []
        for row in grid:
            column.append(row[columnindex])
        tiltedgrid.append(column)

    belt = [[] for i in range(len(grid))]

    for column in tiltedgrid:
        for i in range(len(column)):
            stat = stats(column, splitted = True)
            string = column[i] + (' '*stat.fillspace(stat.width, column[i])) + ' | '
            belt[i].append(string)

    belt2 = []
    for row in belt:
        string = ''.join(row)[:-2]
        belt2.append(string)

    if rowsplit:
        length = len(belt2[0])
        string = length * '-'

        for i in range(1, 2*len(belt2)-1, 2):
            belt2.insert(i, string)

    belt3 = '\n'.join(belt2)
    table = boxify(belt3)

    return table