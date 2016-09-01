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

def is_super_balanced(root):
    max_depth = None
    min_depth = None

    stack = []
    stack.append([root, 0])

    while len(stack) > 0:
        node, current_depth = stack.pop()
        if node.is_leaf_node():
            max_depth =  max(max_depth, current_depth) if max_depth != None else current_depth
            min_depth = min(min_depth, current_depth) if min_depth != None else current_depth
        else:
            if node.left != None:
                stack.append([node.left, current_depth + 1])
            if node.right != None:
                stack.append([node.right, current_depth + 1])

    return (max_depth - min_depth) <= 1

root = BinaryTreeNode(1)
root.left = BinaryTreeNode(2)
root.right = BinaryTreeNode(3)
root.left.left = BinaryTreeNode(4)

print is_super_balanced(root)

root.left.left.left = BinaryTreeNode(5)

print is_super_balanced(root)
