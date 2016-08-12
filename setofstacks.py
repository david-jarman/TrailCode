#Imagine a (literal) stack of plates. If the stack gets too high, it might topple. Therefore, in real life, we would likely start a new stack when the previous stack exceeds some threshold. Implement a data structure SetOfStacks that mimics this. SetOfStacks should be composed of several stacks, and should create a new stack once the previous one exceeds capacity. SetOfStacks.push() and SetOfStacks.pop() should behave identically to a single stack (that is, pop() should return the same values as it would if there were just a single stack).
#FOLLOW UP
#Implement a function popAt(int index) which performs a pop operation on a specific sub-stack.

class SetOfStacks(object):
    def __init__(self, _height):
        self.height = _height
        self.stacks = [[]]
        
    def push(self, _data):

        currentStackIndex = len(self.stacks) - 1
        currentStack = self.stacks[currentStackIndex]

        if len(currentStack) == self.height:
            self.stacks.append([_data])
        else:
            currentStack.append(_data)

    def pop(self):
        currentStackIndex = len(self.stacks) - 1
        currentStack = self.stacks[currentStackIndex]

        element = currentStack.pop()
        if len(currentStack) == 0:
            self.stacks.pop()

        return element

    def __str__(self):
        string = ""
        for stack in self.stacks:
            for element in stack:
                string += ("-> %s" % element)
            string += "\n"

        return string

stack = SetOfStacks(5)

for x in range(1,14):
    stack.push(x)

print stack

for x in range(1,14):
    stack.pop()
    print stack
