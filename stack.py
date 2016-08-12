class Node(object):
    def __init__(self, _data):
        self.data = _data
        self.next = None


class Stack(object):
    def __init__(self):
        self.top = None

    def push(self, data):
        t = Node(data)
        t.next = self.top
        self.top = t

    def pop(self):
        if self.top != None:
            t = self.top
            self.top = self.top.next
            return t
        else:
            return None

    def __str__(self):
        string = ""
        t = self.top
        while t != None:
            string = string + " -> "
            string = string + ("%s" % t.data)
            t = t.next

        return string

stack = Stack()

for x in range(1,11):
    stack.push(x)

print stack

for x in range(1,11):
    stack.pop()
    print stack
