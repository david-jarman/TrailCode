class BinaryTreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert_left(self, value):
        self.left = BinaryTreeNode(value)
        return self.left

    def insert_right(self, value):
        self.right = BinaryTreeNode(value)
        return self.right

    def is_leaf_node(self):
        return self.left == None and self.right == None

def is_binary_search_tree_2(root):
    elements = []
    stack = []
    node = root
    done = False

    while not done:
         if node != None:
             stack.append(node)
             node = node.left
         else:
             if len(stack) > 0:
                 node = stack.pop()
                 elements.append(node.value)
 
                 node = node.right
             else:
                 done = True

    comp_node = elements[0]
    for node in elements[1:]:
        if comp_node > node:
            return False
        else:
            comp_node = node

    return True

def is_binary_search_tree(root):
    stack = []
    stack.append(root)

    while len(stack) > 0:
        node = stack.pop()
        if node.is_leaf_node() == False:
            if node.left != None:
                valid = is_subtree_less_than_root_element(node.value, node.left)
                if valid == False:
                    return False
                else:
                    stack.append(node.left)
            if node.right != None:
                valid = is_subtree_greater_than_root_element(node.value, node.right)
                if valid == False:
                    return False
                else:
                    stack.append(node.right)

    return True

def compare_subtree_to_root_element(element, subtree, cmp_func):
    if subtree.is_leaf_node():
        return True if cmp_func(element, subtree.value) else False

    if cmp_func(element, subtree.value):
        answer = True
        if subtree.left != None:
            answer = compare_subtree_to_root_element(element, subtree.left, cmp_func)
            if answer == False:
                return False
        if subtree.right != None:    
            answer = compare_subtree_to_root_element(element, subtree.right, cmp_func)

        return answer
    else:
        return False

def is_subtree_less_than_root_element(element, subtree):
    return compare_subtree_to_root_element(element, subtree, lambda x,y : y < x)

def is_subtree_greater_than_root_element(element, subtree):
    return compare_subtree_to_root_element(element, subtree, lambda x,y : y > x)

root = BinaryTreeNode(50)
root.left = BinaryTreeNode(30)
root.right = BinaryTreeNode(80)
root.left.left = BinaryTreeNode(20)
root.left.right = BinaryTreeNode(60)
root.right.left = BinaryTreeNode(70)
root.right.right = BinaryTreeNode(90)

print is_binary_search_tree(root)
print is_binary_search_tree_2(root)
