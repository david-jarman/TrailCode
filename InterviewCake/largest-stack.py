from Stack import Stack

class MaxStack(Stack):
    def __init__(self):
        self.max_stack = []
        super(MaxStack, self).__init__()

    def push(self, item):
        if len(self.max_stack) == 0 or item >= self.max_stack[-1]:
            self.max_stack.append(item)

        super(MaxStack, self).push(item)

    def pop(self):
        item = super(MaxStack, self).pop()

        if len(self.max_stack) > 0 and item == self.max_stack[-1]:
            self.max_stack.pop()

        return item

    def get_max(self):
        return self.max_stack[-1] if len(self.max_stack) > 0 else None


s = MaxStack()

s.push(1)
s.push(2)
s.push(3)
s.push(5)
s.push(4)
print s.get_max()
s.pop()
print s.get_max()
s.pop()
print s.get_max()
