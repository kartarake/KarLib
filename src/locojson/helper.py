import os
import json

from ..boxify import boxify

# Exceptions
from .exceptions import *

def fetchlocojsonver() -> str:
    with open("engine.py", "r") as f:
        return f.readline()[1:]

def islocojsonhere(path) -> bool:
    return os.path.exists(os.path.join(path, "locojson.mark"))

def marklocojsonhere(path) -> None:
    if islocojsonhere(path):
        raise locojsonAlreadyExists("locojson already exists")
    
    with open(os.path.join(path, "locojson.mark"), "w") as f:
        version = fetchlocojsonver()
        f.write(boxify(version))

    with open(os.path.join(path, "locojson.registry"), "r") as f:
        json.dump({}, f)

def fetchregistry(path) -> dict:
    with open(os.path.join(path, "locojson.registry"), "r") as f:
        return json.load(f)
    
def listcompartments(path) -> list:
    registry:dict = fetchregistry(path)
    return list(registry.keys())

def saveregistry(path, registry: dict) -> None:
    with open(os.path.join(path, "locojson.registry"), "w") as f:
        json.dump(registry, f)

def load_json(path) -> dict|list:
    with open(path, "r") as f:
        return json.load(f)
    
def save_json(path, data) -> None:
    with open(path, "w") as f:
        json.dump(data, f)

def structurepath(folder, name, splits=1) -> list[str]:
    paths:list = []
    
    if splits == 1:
        paths.append(os.path.join(folder, f"{name}.json"))
    else:
        for i in range(splits):
            paths.append(os.path.join(folder, f"{name}_{i}.json"))
    
    return paths