class Node(object):
    def __init__(self, _data):
        self.next = None
        self.data = _data

class Queue(object):
    def __init__(self):
        self.first = None
        self.last = None

    def enqueue(self, _data):
        n = Node(_data)

        if self.first == None:
            self.first = n
            self.last = n
        else:
            self.last.next = n
            self.last = n

    def dequeue(self):
        if self.first != None:
            data = self.first.data
            self.first = self.first.next
            return data
        
        return None

    def __str__(self):
        string = ""

        i = self.first
        while i != None:
            string = string + " -> "
            string = string + ("%s" % i.data)
            i = i.next

        return string


queue = Queue()

for x in range(1, 11):
    queue.enqueue(x)

print queue

for x in range(1, 11):
    queue.dequeue()
    print queue
