import json
import os

def chop(d:dict, n:int) -> list:
    encodeddict = json.dumps(d)

    length = len(encodeddict)
    each_split = length // n

    result = []
    for i in range(n):
        start = i * each_split
        end = (i+1) * each_split
        result.append(encodeddict[start:end])
    
    return result


def chop_and_save(d:dict, n:int, name:str, folder:str|bytes):
    chopped = chop(d, n)
    os.makedirs(folder, exist_ok=True)

    for i in range(1, len(chopped)+1):
        path = os.path.join(folder, f"{name}_{i}.pjson")
        with open(path, "w") as f:
            f.write(chopped[i-1])


def join(name:str, folder:str|bytes) -> dict:
    paths = os.listdir(folder)
    filtered_paths = [path for path in paths if path.startswith(name) and path.endswith(".pjson")]
    filtered_paths.sort()

    belt = []
    for path in filtered_paths:
        with open(os.path.join(folder, path), "r") as f:
            belt.append(f.read())

    return json.loads(''.join(belt))