class pystack:
    def __init__(self, import_data = []) -> None:
        self.data = []
        self.data.extend(import_data)

    def push(self, item):
        self.data.append(item)

    def pop(self):
        if len(self.data) == 0:
            raise IndexError("Stack is empty")
        return self.data.pop()
    
    def peek(self):
        if len(self.data) == 0:
            raise IndexError("Stack is empty")
        return self.data[-1]