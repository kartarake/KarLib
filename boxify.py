class stats:
    def __init__(self,string) -> None:
        self.characters = len(string) - string.count('\n')
        self.lines = string.count('\n') + 1

        self.linelist = string.split('\n')
        self.maxcharinline = len(max(self.linelist, key=len))

        self.width = self.maxcharinline + 4
        self.height = self.lines + 2

    def fillspace(self, length, string):
        got = len(string)
        need = length
        fill = need - got

        del got, need
        return fill
        

def boxify(string):
    stat = stats(string)
    belt = list()
    
    topline = '.' + ('-' * (stat.maxcharinline + 2)) + '.'
    belt.append(topline)

    for line in stat.linelist:
        bwline = '| ' + line + (' ' * stat.fillspace(stat.maxcharinline, line)) + ' |'
        belt.append(bwline)

    bottomline = "'" + ('-' * (stat.maxcharinline + 2)) + "'"
    belt.append(bottomline)

    final = '\n'.join(belt)
    return final