from ..pystack import pystack

def analysebranch(branch:dict, result:dict, keystack:pystack):
    branchresult = {}
    for key in branch:
        keystack.push(key)
        count = 0

        if type(branch[key]) == dict:
            subresult = analysebranch(branch[key], result, keystack)

        elif type(branch[key]) in (list, tuple, set):
            subresult = {"depth":len(branch[key])}
        
        else:
            subresult = {"depth":1}

        if subresult:
            keys = keystack.data
            indexstring = "".join([f"[{key}]" for key in keys])
            eval(f"result{indexstring}") = subresult

        count += 1
        keystack.pop()

def analyse(dictionary:dict):
    result = {}
    keystack = pystack()      


def chop(dictionary, n):
    pass