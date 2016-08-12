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

class Queue2(object):
    def __init__(self):
        self.s1 = []
        self.s2 = []
        
    def enqueue(self, _data):
        self.s1.append(_data)

    def dequeue(self):
        if len(self.s2) == 0:
            while len(self.s1) > 0:
                self.s2.append(self.s1.pop())
        
        if len(self.s2) > 0:
            return self.s2.pop()
        else:
            return None

    def __str__(self):
        string = ""
        for item in self.s1:
            string += " -> %s" % item

        for item in self.s2:
            string += " -> %s" % item
        return string

queue = Queue2()

for x in range(1, 11):
    queue.enqueue(x)

print queue

for x in range(1, 11):
    queue.dequeue()
    print queue
