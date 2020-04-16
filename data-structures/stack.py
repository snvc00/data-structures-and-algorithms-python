# Stack implemented in Python


class Stack:
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        if len(self.stack) < 1:
            return print("Calling: pop(self): Empty Stack")
        del self.stack[len(self.stack) - 1]

    def top(self):
        if len(self.stack) < 1:
            return print("Calling top(self): Empty Stack")
        return self.stack[len(self.stack) - 1]

    def size(self):
        return len(self.stack)

