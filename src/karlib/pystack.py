"""Simple stack implementation"""
class pystack:
    def __init__(self, import_data = []) -> None:
        self.data = []
        self.data.extend(import_data)

    def push(self, item):
        self.data.append(item)

    def pop(self):
        if len(self.data) == 0:
            raise IndexError("Underflow")
        return self.data.pop()
    
    def peek(self):
        if len(self.data) == 0:
            raise IndexError("Underflow")
        return self.data[-1]
    
    def popmany(self, n):
        if n == "*":
            n = len(self.data)     
        if len(self.data) < n:
            raise IndexError("Underflow")
        return [self.pop() for i in range(n)]