#Design a class that accommodates all the Tree traversal types (Inorder, Preorder, Postorder)

class Node:                                           #class to define the tree for traversal
    def __init__(self, value):
        self.left = None                              # left root of the tree
        self.right = None                             # right root of the tree
        self.val = value

def inorder(root):                                   # function for inorder traversal
    if root:
        # Traverse left
        inorder(root.left)
        # Traverse root
        print(str(root.val) + "->", end='')
        # Traverse right
        inorder(root.right)

def postorder(root):                                # function for post order traversal
    if root:
        # Traverse left
        postorder(root.left)
        # Traverse right
        postorder(root.right)
        # Traverse root
        print(str(root.val) + "->", end='')

def preorder(root):                                 # function for preorder traversal

    if root:
        # Traverse root
        print(str(root.val) + "->", end='')
        # Traverse left
        preorder(root.left)
        # Traverse right
        preorder(root.right)

root = Node(5)
root.left = Node(10)
root.right = Node(15)
root.left.left = Node(20)
root.left.right = Node(25)

print("Inorder traversal ")                           # function call for inorder traversal
inorder(root)

print("\nPreorder traversal ")                        # function call for preorder traversal
preorder(root)

print("\nPostorder traversal ")                       # function for post order traversal
postorder(root)