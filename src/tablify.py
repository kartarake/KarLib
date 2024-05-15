import math
from boxify import boxify

class stats:
    def __init__(self, grid):
        self.grid = self.convtolist(grid)
        self.tiltedgrid = self.tiltgrid(grid)
        self.maxcharmap = self.getmaxcharmap(self.tiltedgrid)
        self.width = 1 + len(self.tiltedgrid) * 3 + sum([self.maxcharmap[key] for key in self.maxcharmap])

        self.alignmap = self.getalignmap(grid)
        self.widthmap = self.getwidthmap(grid)

    def getmaxcharmap(self, tiltedgrid):
        maxcharmap = {}
        i = 0
        for column in tiltedgrid:
            maxchar = max(column, key=len)
            maxcharmap[i] = len(maxchar)
            i += 1
        return maxcharmap
    
    def getwidthmap(self, grid):
        header = grid[0]
        widthmap = {}
        i = 0
        for item in header:
            if type(item) == str:
                widthmap[i] = self.maxcharmap[i]

            elif type(item) == dict and not "text" in item:
                raise ValueError(f"Item : {item} \nThis item doesn't have any keyword 'text' to represent in table")
            
            elif (type(item) == dict) and ("width" in item) and (item["width"] < self.maxcharmap[i]):
                raise ValueError(f"ValueError : {item["text"]} has been assigned only {item["width"]}. But there is a character of {self.maxcharmap[i]} chars.")

            elif type(item) == dict and "width" in item:
                widthmap[i] = item["width"]
                self.grid[0][i] = item["text"]

            elif type(item) == dict:
                widthmap[i] = self.maxcharmap[i]
                self.grid[0][i] = item["text"]

            else:
                raise TypeError(f"Item : {item} \nUnsupported data type has been passed.Data type : {type(item)}.")
            
            i += 1
        return widthmap
    
    def getalignmap(self, grid):
        alignmap = {}
        header = grid[0]
        i = 0
        for item in header:
            if type(item) == dict and "align" in item:
                alignmap[i] = item["align"]
            else:
                alignmap[i] = "left"
            i += 1
        return alignmap
                

    def fillspace(self, length, string):
        got = len(string)
        return " "*(length - got)
    
    def centerstring(self, length, string):
        got = len(string)
        need = length - got
        first = math.floor(need/2)
        second = math.ceil(need/2)
        return " " * first + string + " " * second
    
    def tiltgrid(self, grid):
        tiltedgrid = [[] for i in range(len(grid))]
        for i in range(len(grid)):
            for row in grid:
                tiltedgrid[i].append(row[i])
        return tiltedgrid
    
    def convtolist(self, grid):
        grid2 = []
        
        for row in grid:
            if type(row) == tuple:
                grid2.append(list(row))
            else:
                grid2.append(row)
        
        return grid2

def tablify(grid):

    start = True
    prevcount = None
    for row in grid:
        if start and not (type(row) in (tuple, list)):
            raise TypeError(f"Row : <{row}> is of unsupported data type {type(row)}")
        
        elif not (type(row) in (tuple, list)):
            raise TypeError(f"Row : <{row}> is of unsupported data type {type(row)}")

        else:
            pass

        if prevcount == None:
            prevcount = len(row)

        else:
            if not (len(row) == prevcount):
                raise ValueError(f"Row : <{row}> is not of format.")
            else:
                prevcount = len(row)

    stat = stats(grid)
    grid = stat.grid

    header = []; i = 0
    for item in grid[0]:
        if stat.alignmap[i] == "left":
            string = item + stat.fillspace(stat.widthmap[i], item)

        elif stat.alignmap[i] in ("centre", "center"):
            string = stat.centerstring(stat.widthmap[i], item)

        elif stat.alignmap[i] == "right":
            string = stat.fillspace(stat.widthmap[i], item) + item

        else:
            raise ValueError(f"Invalid alignment mode < {stat.widthmap[i]} > has been passed")
        
        header.append(string)
        i += 1
    header = ' | '.join(header)
    
    grid2 = []
    skip = True
    for row in grid:
        if skip:
            skip = False
            continue

        belt = [] ; i = 0
        for item in row:
            if stat.alignmap[i] == "left":
                string = item + stat.fillspace(stat.widthmap[i], item)

            elif stat.alignmap[i] in ("centre", "center"):
                string = stat.centerstring(stat.widthmap[i], item)

            elif stat.alignmap[i] == "right":
                string = stat.fillspace(stat.widthmap[i], item) + item

            else:
                raise ValueError(f"Invalid alignment mode < {stat.widthmap[i]} > has been passed")
            
            belt.append(string)
            i += 1
        string = ' | '.join(belt)
        grid2.append(string)
    
    grid3 = '\n'.join(grid2)
    
    header = boxify(header) + "\n"
    grid3 = boxify(grid3)

    table = header + grid3
    return table
