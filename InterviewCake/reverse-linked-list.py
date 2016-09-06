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

def reverse_list_out_of_place(head):
    if not head:
        return None
    if not head.next:
        return head

    prev = None
    cur = head

    while cur:
        new_node = LinkedListNode(cur.value)
        new_node.next = prev

        prev = new_node
        cur = cur.next

    return prev



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

new_new_head = reverse_list_out_of_place(new_head)
li_new = LinkedList()
li_new.root = new_new_head
print li_new
print li
