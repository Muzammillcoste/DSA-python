class BinarySearchTree:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
        
    def add_child(self,child):
        if child==self.data:
            return
        
        elif child<self.data:
            if self.left:
                self.left.add_child(child)
            else:
                self.left=BinarySearchTree(child)
        else:
            if self.right:
                self.right.add_child(child)
            else:
                self.right=BinarySearchTree(child)
                
    def Search_element(self,element):
        if element==self.data:
            return True
        elif element<self.data:
            if self.left:
                return self.left.Search_element(element)
            else:
                return False
        else:
            if self.right:
               return self.right.Search_element(element)
            else:
               return False

    def Inorder_Traversal(self):
        if self is None:
            return []
        return (BinarySearchTree.Inorder_Traversal(self.left)+[self.data]+
                BinarySearchTree.Inorder_Traversal(self.right))       

                
                
def buildtree(elements):
    if len(elements)==0:
        raise Exception('list is empty')
    
    root=BinarySearchTree(elements[0])
    for i in range(1,len(elements)):
        root.add_child(elements[i])
        
    return root

tree_list=[10,4,6,7,9,17,18,0,3,-1,3]
tree=buildtree(tree_list)
tree.add_child(5)
print(tree.Search_element(5))
print(tree.Inorder_Traversal())
