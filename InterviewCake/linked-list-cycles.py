from LinkedList import LinkedListNode

def contains_cycle_N_space(root):
    node = root
    node_set = set()

    while node:
        if node in node_set:
            return True
        else:
            node_set.add(node)
            node = node.next

    return False

def contains_cycle(root):
    fast_runner = root
    slow_runner = root

    while fast_runner != None and fast_runner.next != None:
        slow_runner = slow_runner.next
        fast_runner = fast_runner.next.next

        if fast_runner == slow_runner:
            return True

    return False

l1 = LinkedListNode(1)
l2 = LinkedListNode(2)
l1.next = l2
l3 = LinkedListNode(3)
l2.next = l3
print contains_cycle(l1)
l3.next = l1

print contains_cycle(l1)
l3.next = l2
print contains_cycle(l1)
l3.next = l3
print contains_cycle(l1)
