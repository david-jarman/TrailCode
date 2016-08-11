class Node( object ):
    
    def __init__(self, _data):
        self.next = None
        self.data = _data

    def appendToEnd(self, _data):
        end = Node(_data)
        iterator = self

        while iterator.next != None:
            iterator = iterator.next

        iterator.next = end

    def __str__(self):
        iterator = self
        string = ""
        string = string + ('%s' % self.data)

        while (iterator.next != None):
            iterator = iterator.next
            string = string + " -> "
            string = string + ('%s' % iterator.data)

        return string

def deleteFromLinkedList(_head, _data):
    if _head.data == _data:
        return _head.next

    iterator = _head
    while iterator.next != None:
        if iterator.next.data == _data:
            iterator.next = iterator.next.next
            return _head

        iterator = iterator.next

    return _head

def removeDuplicates(_head):
    if _head != None or _head.next == None:
        return _head

    dataMap = {}
    
    current = _head
    prev = _head

    while current != None:
        if dataMap.exists(current.data):
            prev.next = current.next
        else:
            dataMap[current.data] = True

        prev = current
        current = current.next

    return _head

def removeDuplicatesWithoutBuffer(_head):
    if _head == None or _head.next == None:
        return _head

    iterator = _head
    while iterator != None:
        compare = iterator.next
        prev = iterator
        while compare != None:
            if compare.data == iterator.data:
                prev.next = compare.next
            else:
                prev = compare
            compare = compare.next
        iterator = iterator.next

    return _head

head = Node(0)

for x in range(1,10):
    head.appendToEnd(x)

print head

