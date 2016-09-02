from BinaryTreeNode import BinaryTreeNode

right_case_root = BinaryTreeNode(5)
right_case_root.left = BinaryTreeNode(4)
#right_case_root.right = BinaryTreeNode(7)
#right_case_root.right.left = BinaryTreeNode(6)
#right_case_root.right.right = BinaryTreeNode(8)

def find_second_largest_element_cleaner(root):
    if not root.left and not root.right:
        raise Exception('Must at least have two elements in tree')

    node = root

    while node:
        if node.left and not node.right:
            return find_largest_element(node.left)

        if node.right and not node.right.left and not node.right.right:
            return node.value

        node = node.right

def find_largest_element(root):
    node = root
    while node:
        if not node.right:
            return node.value
        node = node.right

def find_second_largest_element(root):
    node = root
    parent = None
    largest_found = False

    while True:
        if node.right:
            parent = node
            node = node.right
        else:
            if largest_found:
                return node

            #found the nth largest largest element
            largest_found = True
        
            if node.left:
                parent = node
                node = node.left
            else:
                return parent

print find_second_largest_element(right_case_root).value
