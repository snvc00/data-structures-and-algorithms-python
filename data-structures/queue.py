# Queue implemented in Python


class Queue:
    def __init__(self):
        self.queue = []

    def push(self, item):
        self.queue.append(item)

    def pop(self):
        if len(self.queue) < 1:
            return print("Calling: pop(self): Empty Queue")
        self.queue.pop(0)

    def front(self):
        if len(self.queue) < 1:
            return print("Calling: front(self): Empty Queue")
        return self.queue[0]

    def back(self):
        if len(self.queue) < 1:
            return print("Calling: back(self): Empty Queue")
        return self.queue[len(self.queue) - 1]

    def size(self):
        return len(self.queue)

