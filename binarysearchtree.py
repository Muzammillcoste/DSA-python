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
        
    def Preorder_Traversal(self):
        if self is None:
            return []
        return ([self.data]+BinarySearchTree.Preorder_Traversal(self.left)+
                BinarySearchTree.Preorder_Traversal(self.right))

    def Postorder_Traversal(self):
        if self is None:
            return []
        return (BinarySearchTree.Postorder_Traversal(self.left)+
                BinarySearchTree.Postorder_Traversal(self.right)+[self.data])
    
    def Height(self):
        if self is None:
            return 0
        return 1+max(BinarySearchTree.Height(self.left),BinarySearchTree.Height(self.right))
    
    def No_of_Nodes(self):
        if self is None:
            return 0
        return 1+BinarySearchTree.No_of_Nodes(self.left)+BinarySearchTree.No_of_Nodes(self.right)
    
    def Mini_depth(self):
        if self is None:
            return 0
        return 1+min(BinarySearchTree.Mini_depth(self.left),BinarySearchTree.Mini_depth(self.right))
                                
def buildtree(elements):
    print('BinarySearchTree',elements)
    if len(elements)==0:
        raise Exception('list is empty')
    
    root=BinarySearchTree(elements[0])
    for i in range(1,len(elements)):
        root.add_child(elements[i])
        
    return root

tree_list=[3,9,20,15,7]
tree=buildtree(tree_list)

print(tree.Inorder_Traversal())
print(tree.Preorder_Traversal())
print(tree.Postorder_Traversal())
print(tree.Height())
print(tree.No_of_Nodes())
print(tree.Mini_depth())
