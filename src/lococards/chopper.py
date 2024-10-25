from ..pystack import pystack

def analysedict(dictionary:dict) -> dict:
    result = {"weight":0, "sub-branches":{}}
    counter = 0

    for key in dictionary:
        if type(dictionary[key]) in (dict, list, tuple, set):
            subresult = analysedict(dictionary[key])
        
        else:
            subresult = {"weigth": 1}

        result["sub-branches"][key] = subresult
        counter += subresult["weigth"]
        counter += 1

    result["weigth"] = counter
    return result

def totalweight(analysis:dict) -> int:
    var = 0
    for key in analysis["sub-branches"]:
        var += analysis["sub-branches"][key]["weigth"]
    return var

def chopdict(d:dict, n:int) -> list:
    analysis = analysedict(d)
    total_weight = totalweight(analysis)

    each_split_weight = total_weight // n
    each_split_weight_now = [0 for i in range(n)]

    for key in d:
        if 