class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key


# A utility function to insert a new node with the given key
def insert(root, node):
    if root is None:
        root = node
    else:
        if root.val < node.val:
            if root.right is None:
                root.right = node
            else:
                insert(root.right, node)
        else:
            if root.left is None:
                root.left = node
            else:
                insert(root.left, node)

# inorder tree traversal


def inorder(root):
    if root:
        inorder(root.left)
        print(root.val)
        inorder(root.right)

# preorder tree traversal

def preorder(root):
    if root:
        print(root.val)
        preorder(root.left)
        preorder(root.right)

# postorder tree traversal

def postorder(root):
    if root:
        postorder(root.left)
        postorder(root.right)
        print(root.val)
# a function to search a given key in BST
def search(root, key):
    if root is None or root.val == key:
        return root
    if root.val < key:
        return search(root.right, key)
    return search(root.left, key)


r = Node(50)
insert(r, Node(30))
insert(r, Node(20))
insert(r, Node(40))
insert(r, Node(70))
insert(r, Node(60))
insert(r, Node(80))

inorder(r)
preorder(r)
postorder(r)
