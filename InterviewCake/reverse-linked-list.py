from LinkedList import LinkedListNode
from LinkedList import LinkedList

def reverse_list_inplace(head):
    if not head:
        return None
    if not head.next:
        return head

    prev = None
    cur = head
    next = cur.next

    while True:
        cur.next = prev
        if next:
            prev = cur
            cur = next
            next = next.next
        else:
            return cur

head = LinkedListNode(1)
head.next = LinkedListNode(2)
head.next.next = LinkedListNode(3)
head.next.next.next = LinkedListNode(4)

li = LinkedList()
li.root = head
print li

new_head = reverse_list_inplace(head)
li.root = new_head
print li
