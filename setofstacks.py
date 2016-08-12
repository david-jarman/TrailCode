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

        if len(currentStack) > 0:
            element = currentStack.pop()
        
        if len(currentStack) == 0:
            if len(self.stacks) > 1:
                self.stacks.pop()

        return element

    def popAt(self, _index):
        if _index < len(self.stacks):
            stack = self.stacks[_index]
            element = stack.pop()           

            if len(stack) == 0:
                if len(self.stacks) > 1:
                    self.stacks.pop(_index)
                return
 
            #rollover other stacks if necessary
            if len(self.stacks) > _index + 1:
                for stackIndex in range(_index, len(self.stacks)-1):
                    currentStack = self.stacks[stackIndex]
                    nextStack = self.stacks[stackIndex+1]
                    currentStack.append(nextStack.pop(0))
                    if len(nextStack) == 0:
                        if len(self.stacks) > 1:
                            self.stacks.pop(stackIndex+1)

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

for x in range(1,6):
    stack.popAt(2)
    print stack

#for x in range(1,13):
#    stack.pop()
#    print stack
