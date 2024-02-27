class Node:
    def __init__(self, data=None):
        self.data = data
        self.left = None
        self.right = None
class binarySearchTree(Node):
    
    def __init__(self, data):
            super().__init__(data)
            
    def insertData(self, node, data):
        if node == None:
            return Node(data) 
        if data < node.data:
            node.left = self.insertData(node.left, data)
        else:
            node.right = self.insertData(node.right, data)
        return node
    
    def inorderData(self, node):
        # left - root - right
        if node != None:
            self.inorderData(node.left)
            print(str(node.data) + "->", end=' ')
            self.inorderData(node.right)
        else:
            return None
        
    def findMinValue(self, node):
        current = node
        while(current.left != None):
            current = current.left
        return current
    
    def findMaxValue(self, node):
        current = node
        while(current.right != None):
            current = current.right
        return current
    
    def search(self, node, data): 
        if node is None:
            return 
        elif node.data == data:
            return node.data
        
        elif data < node.data:
            return self.search(node.left,data)
        else:
            return self.search(node.right,data)
        
    def delete(self, node, data):
        if node is None:
            return 
        # delete the root
        if data < node.data:
            node.left = self.delete(node.left, data)
            return node
        elif data > node.data:
            node.right = self.delete(node.right, data)
            return node
        else:
            # leafe node
            if node.left is None and node.right is None:
                node = None
            elif node.left is None:
                node.data = node.right.data
                del node.right
                node.right = None
            elif node.right is None:
                node.data = node.left.data
                del node.left
                node.left = None
            # the node has 2 child    
            else:
                current = self.findMinValue(node.right)
                node.data = current.data
                node.right = self.delete(node.right, current.data)
        return node