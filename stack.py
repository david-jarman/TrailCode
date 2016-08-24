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

    def peek(self):
        if self.top != None:
            return self.top.data
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

    def is_empty(self):
        return self.top == None

#Write a program to sort a stack in ascending order. You should not make any assumptions about how the stack is implemented. The following are the only functions that should be used to write this program: push | pop | peek | isEmpty.
def sort(stack):
    return_stack = Stack()

    while stack.is_empty() == False:
        tmp = stack.pop()
        
        while return_stack.is_empty() == False and return_stack.peek() < tmp.data:
            stack.push(return_stack.pop().data)

        return_stack.push(tmp.data)

    return return_stack

stack = Stack()

stack.push(1)
stack.push(3)
stack.push(2)
stack.push(4)

print stack

sorted_stack = sort(stack)

print sorted_stack

#for x in range(1,11):
#    stack.push(x)

#print stack

#for x in range(1,11):
#    stack.pop()
#    print stack
