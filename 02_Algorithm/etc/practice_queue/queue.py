class Queue:

    def __init__(self):
        self.data = []

    def enqueue(self, item):
        self.data.append(item)

    def dequeue(self):
        if self.data:
            return self.data.pop(0)

    def is_empty(self):
        return False if self.data else True

    def get_front(self):
        if self.data:
            return self.data[0]

    def get_rear(self):
        if self.data:
            return self.data[-1]



q = Queue()

q.enqueue(1)  # None, q.data => [1]
q.enqueue(2)  # None, q.data => [1, 2]

q.get_front()  # 1
q.get_rear()   # 2

q.dequeue()   # 1, q.data => [2]
q.dequeue()   # 2, q.data => []

