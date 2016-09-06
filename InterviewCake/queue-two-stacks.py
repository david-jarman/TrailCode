class Queue:
    def __init__(self):
        self.stack_1 = []
        self.stack_2 = []

    def enqueue(self, value):
        self.stack_1.append(value)

    def dequeue(self):
        if len(self.stack_1) == 0 and len(self.stack_2) == 0:
            raise Exception('Nothing to dequeue')

        if len(self.stack_2) == 0:
            while len(self.stack_1) > 0:
                self.stack_2.append(self.stack_1.pop())

        return self.stack_2.pop()


q = Queue()

q.enqueue(5)
q.enqueue(4)
q.enqueue(3)
q.enqueue(2)
q.enqueue(1)
q.enqueue(0)


print q.dequeue()
print q.dequeue()
print q.dequeue()

q.enqueue(10)
q.enqueue(11)
q.enqueue(12)

print q.dequeue()
print q.dequeue()
print q.dequeue()
print q.dequeue()
print q.dequeue()
print q.dequeue()
print q.dequeue()

