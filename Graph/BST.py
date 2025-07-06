class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
    
    
class BST:
    def __init__(self):
        self.root = None
        
    
    def insert(self, data):
        
        node = TreeNode(data)
        if self.root is None:
            self.root = node
        else:
            current = self.root
            while current:
                if data < current.data:
                    if current.left is None:
                        current.left = node
                        break
                    else:
                        current = current.left
                else:
                    if current.right is None:
                        current.right = node
                        break
                    else:
                        current = current.right
                        
                        
    def search(self, key):
        current = self.root
        while current:
            if key == current.data:
                return "Found"   
            elif key < current.data:
                current = current.left
            else:
                current = current.right
        return "Not found"
    
    
    def delete(self, key):
        parent = None
        current = self.root
        
        while current and current.data != key:
            parent = current
            if key < current.data:
                current = current.left
            else:
                current = current.right
        
        if current is None:
            return "There is no node"
        
        if current.left and current.right:
            if parent is None:  
                self.root = None
            elif parent.left == current:
                parent.left = None
            else:
                parent.right = None
        
        elif current.left is None or current.right is None:
            child = current.left if current.left is not None else current.right
            if parent is None:  
                self.root = child
            elif parent.left == current:
                parent.left = child
            else:
                parent.right = child
        
        else:
            successor_parent = current
            successor = current.right
            while successor.left:
                successor_parent = successor
                successor = successor.left
            
            current.data = successor.data
            
            if successor_parent.left == successor:
                successor_parent.left = successor.right
            else:
                successor_parent.right = successor.right
        
        return "Delete successfully"
    

    #My function for printing the Tree:
    def print_tree(self):
        self.print_inorder(self.root)
        print()   

    def print_inorder(self, node):
        if node is not None:
            self.print_inorder(node.left)
            print(node.data, end=" ")  
            self.print_inorder(node.right)
            
            
bst = BST()
bst.insert(50)
bst.insert(60)
bst.insert(70)
bst.insert(20)
bst.insert(40)
bst.insert(30)
bst.insert(80)
bst.insert(10)
print("------------------------")
bst.print_tree()  
print("------------------------")
print(bst.delete(1))
bst.print_tree()
print("------------------------")
print(bst.delete(80))
bst.print_tree()
print("------------------------")
print(bst.search(10))

    