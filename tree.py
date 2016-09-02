from Queue import Queue

class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def __str__(self):
        return "%s" % self.value

class BinaryTree(object):
    def __init__(self):
        self.root = None

    def set_root(self, node):
        self.root = node

    def isBalanced(self):
        heights = self.in_order_traverse(self.root, 0, 0, 0)

        print heights[0]
        print heights[1]

        if heights[0] > heights[1] + 1:
            return False
        else:
            return True
              
    #Implement a function to check if a tree is balanced. For the purposes of this question, 
    #a balanced tree is defined to be a tree such that no two leaf nodes differ in distance 
    #from the root by more than one.
    def in_order_traverse(self, node, max_height, max_height_2, current_height):
        if node.left == None and node.right == None:
            if current_height > max_height:
                max_height_2 = max_height
                max_height = current_height
            elif current_height > max_height_2 and current_height <= max_height:
                max_height_2 = current_height
            
            return [max_height, max_height_2]

        heights = [max_height, max_height_2]

        if node != None and node.left != None:
            heights = self.in_order_traverse(node.left, heights[0], heights[1], current_height + 1)
            max_height = heights[0]
            max_height_2 = heights[1]

        if node != None and node.right != None:
            heights = self.in_order_traverse(node.right, heights[0], heights[1], current_height + 1)

        return heights

    def pre_order_print(self, node):
        if node == None:
            return

        print node.value

        self.pre_order_print(node.left)

        self.pre_order_print(node.right)

    def in_order_print(self, node):
        if node == None:
            return

        self.in_order_print(node.left)

        print node.value

        self.in_order_print(node.right)

    def post_order_print(self, node):
        if node == None:
            return

        self.post_order_print(node.left)
        self.post_order_print(node.right)

        print node.value

    def breadth_first_print(self):
        q = Queue()

        q.put(self.root)
        current = None

        while q.empty() == False:
            current = q.get()
            print current.value

            if current.left != None:
                q.put(current.left)
            if current.right != None:
                q.put(current.right)


#Given a sorted (increasing order) array, write an algorithm to create a binary tree with minimal height.
def create_binary_tree(sorted_array):
    tree = BinaryTree()

    if len(sorted_array) == 0:
        return None

    return create_binary_tree_recursive(sorted_array, None, 0, len(sorted_array) - 1)

def create_binary_tree_recursive(sorted_array, node, left, right):
    if left >= right:
        return None

    index = ((right - left) // 2) + left

    value = sorted_array[index]
    new_node = Node(value)

    if node != None:
        if value < node.value:
            node.left = new_node
        else:
            node.right = new_node

    create_binary_tree_recursive(sorted_array, new_node, left, index)
    create_binary_tree_recursive(sorted_array, new_node, index+1, right)
        
    return new_node

def in_order_traverse_iterative(root):
    stack = []
    stack.append([root, False])

    while len(stack):
        node, visited = stack[-1]
        if node and visited == False:
            stack.append([node.left, False])
        elif node and visited == True:
            print node.value
            stack.pop()
            stack.append([node.right, False])
        else:
            stack.pop()
            if len(stack):
                stack[-1][1] = True

def in_order_traverse_iterative_2(root):
    stack = []
    stack.append(root)
    done = False
    node = root

    while not done:
        if node:
            stack.append(node)
            node = node.left
        else:
            if len(stack) == 0:
                done = True
            else:
                node = stack.pop()
                print node.value
                node = node.right


#import pdb

#pdb.set_trace()


sorted_array = range(25)

root = create_binary_tree(sorted_array)

tree = BinaryTree()
tree.set_root(root)

#tree.in_order_print(root)

print "our latest"
in_order_traverse_iterative_2(root)
