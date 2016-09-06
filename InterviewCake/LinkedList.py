class LinkedListNode:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.root = None

    def __str__(self):
        string = ""

        node = self.root
        while node:
            string = string + str(node.value) + " -> "
            node = node.next

        return string

    def insert(self, value):
        if not self.root:
            self.root = LinkedListNode(value)
        else:
            current = self.root
            
            while current.next:
                current = current.next

            current.next = LinkedListNode(value)

    def delete(self, value):
        next_node = self.root
        current = None

        if not self.root:
            return False

        if self.root.value == value:
            self.root = self.root.next
            return True

        while next_node:
            if next_node.value == value:
                current.next = next_node.next
                return True
            else:
                current = next_node
                next_node = next_node.next

        return False

def test_list():
    l_list = LinkedList()
    
    for i in range(0,10):
        l_list.insert(i)
        print l_list
    
    l_list.delete(5)
    print l_list
    
    l_list.delete(0)
    print l_list
    
    l_list.delete(9)
    print l_list
    
    l_list.delete(10)
    print l_list

    for i in range(10, -1, -1):
        l_list.delete(i)
        print l_list

test_list()
