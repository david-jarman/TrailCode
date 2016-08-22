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

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)

tree = BinaryTree()
tree.set_root(root)

tree.breadth_first_print()
