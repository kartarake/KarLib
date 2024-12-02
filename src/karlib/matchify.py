def simplify(string):
    return string.lower().strip()

def countmap(string):
    map = {}
    for char in string:
        if char in map:
            map[char] += 1
        else:
            map[char] = 1
    return map

def countmapsimilarity(string1, string2):
    map1 = countmap(string1)
    map2 = countmap(string2)

    similarity = 1
    for key in map1:
        if key in map2 and map1[key] == map2[key]:
            similarity *= 1.5
        elif key in map2:
            similarity *= 1.25
        else:
            pass

    return similarity

def smallstr(string1, string2):
    if len(string1) < len(string2):
        return string1
    else:
        return string2

def possimilarity(string1, string2):
    similar = 0
    for i in range(len(smallstr(string1, string2))):
        if string1[i] == string2[i]:
            similar += 1

    return similar/len(string1)*2

def similarity(string1, string2):
    constant = 1
    string1 = simplify(string1)
    string2 = simplify(string2)

    if string1[0] == string2[0]:
        constant *= 1.5
    if string1[-1] == string2[-1]:
        constant *= 1.5
    constant *= countmapsimilarity(string1, string2)
    constant *= possimilarity(string1, string2)
    return constant
    
def matchify(iterable, string):
    consmap = {}
    for reference in iterable:
        wordsimilarity = similarity(string, reference)
        consmap[reference] = wordsimilarity
    
    currentmax = None
    consmap[currentmax] = -1
    for key in consmap:
        if currentmax is None or consmap[key] > consmap[currentmax]:
            currentmax = key

    return currentmax