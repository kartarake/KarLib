class locojsonAlreadyExists(Exception):
    "The error raised when trying to create locojson in a path where one already exists."    
    def __init__(self, message):
        super().__init__(message)

class compartmentAlreadyExists(Exception):
    "The error raised when trying to create locojson in a path where one already exists."    
    def __init__(self, message):
        super().__init__(message)

class compartmentDoesNotExist(Exception):
    "The error raised when trying to create locojson in a path where one already exists."    
    def __init__(self, message):
        super().__init__(message)