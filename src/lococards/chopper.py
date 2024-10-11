def analysebranch(branch:dict):
    branchresult = {"weight":0, "sub-branches":{}}
    counter = 0

    for key in branch:
        if type(branch[key]) in (dict, list, tuple, set):
            subresult = analysebranch(branch[key])
        
        else:
            subresult = {"weigth": 1}

        branchresult["sub-branches"][key] = subresult
        counter += 1

    branchresult["weigth"] = counter
    return branchresult


def analyse(dictionary:dict):
    analysis_graph = analysebranch(dictionary)  


def chop(dictionary, n):
    pass