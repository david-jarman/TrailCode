from LinkedList import LinkedListNode
from LinkedList import LinkedList

head = LinkedListNode('Angel Food')
b = LinkedListNode('Bundt')
c = LinkedListNode('Cheese')
d = LinkedListNode('Devils Food')
e = LinkedListNode('Eccles')

head.next = b
b.next = c
c.next = d
d.next = e

def kth_to_last_node(k, head):
    count = 0
    node = head

    while node:
        node = node.next
        count += 1

    if k > count:
        raise Exception('k is larger than the list size')

    stop_at = count - k

    node = head
    i = 0
    while i < stop_at:
        node = node.next
        i += 1

    return node

print kth_to_last_node(2, head).value
