class stats:
    def __init__(self, string, width = None) -> None:
        self.characters = len(string) - string.count('\n')
        self.lines = string.count('\n') + 1

        self.linelist = string.split('\n')
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
        

def boxify(string, width = None):
    if not(width == None):
        stat = stats(string, width = width)
    else:
        stat = stats(string)

    belt = list()
    
    topline = '.' + ('-' * (stat.width - 2)) + '.'
    belt.append(topline)

    for line in stat.linelist:
        bwline = '| ' + line + (' ' * stat.fillspace(stat.width - 4, line)) + ' |'
        belt.append(bwline)

    bottomline = "'" + ('-' * (stat.width - 2)) + "'"
    belt.append(bottomline)

    final = '\n'.join(belt)
    return final