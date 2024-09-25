# locoJSON v0.0.0

import json
import time

from .helper import *
from .exceptions import *

class JSONtrain:
    def __init__(self, path, password=None) -> None:
        self.path = path
        self.registry_path = os.path.join(path, "locojson.registry")
        self.registry = {}
        self.registry.update(fetchregistry(self.registry_path))

        @property
        def compartments(self) -> list:
            return listcompartments(self.registry_path)

        self.current = None
        self.data = None

    def newCompartment(self, name, splits=1) -> None:
        if name in self.registry:
            raise compartmentAlreadyExists(f"Compartment {name} already exists")
        
        self.registry[name] = {
            "time_created":time.ctime(),
            "splits":splits,
            "path":structurepath(self.path, name, splits)
        }

        saveregistry(self.registry_path, self.registry)
        self.current = name
        self.data = None

    def changeCompartment(self, name) -> None:
        if name not in self.registry:
            raise compartmentDoesNotExist(f"Compartment {name} does not exist")
        
        self.data = load_json(self.registry[name]["path"])
        self.current = name