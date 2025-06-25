class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def preorder(root):
    if root is None:
        return
    print(root.data, end=" ")
    if root.left is not None:
        preorder(root.left)
    if root.right is not None:
        preorder(root.right)

def inorder(root):
    if root is None:
        return
    inorder(root.left)
    print(root.data, end=" ")
    inorder(root.right)

def postorder(root):
    if root is None:
        return
    postorder(root.left)
    postorder(root.right)
    print(root.data, end=" ")


A_node = TreeNode('A')
B_node = TreeNode('B')
C_node = TreeNode('C')
D_node = TreeNode('D')
E_node = TreeNode('E')
F_node = TreeNode('F')
G_node = TreeNode('G')

A_node.left = B_node
A_node.right = C_node

B_node.left = D_node
B_node.right = E_node

C_node.left = F_node
C_node.right = G_node


print("Preorder: ", end="")
preorder(A_node)

print("\nInorder: ", end="")
inorder(A_node)

print("\nPostorder: ", end="")
postorder(A_node)
