# JSONcards v0.0.0

import json
import time

from .helper import *
from .exceptions import *

class JSONcard:
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

    def newCard(self, name, splits=1) -> None:
        if name in self.registry:
            raise compartmentAlreadyExists(f"Compartment {name} already exists")
        
        paths = structurepath(self.path, name, splits)
        makepaths(paths)
        
        self.registry[name] = {
            "time_created":time.ctime(),
            "splits":splits,
            "path": paths
        }

        saveregistry(self.registry_path, self.registry)
        self.current = name
        self.data = None

    def changeCard(self, name) -> None:
        if name not in self.registry:
            raise compartmentDoesNotExist(f"Compartment {name} does not exist")
        
        compartment_registry = self.registry[name]
        if compartment_registry["splits"] == 1:
            self.data = load_json(compartment_registry["path"][0])
        else:
            self.data.clear()
            for path in compartment_registry["path"]:
                self.data.update(load_json(path))

        self.current = name