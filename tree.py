class Tree:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
    
    @staticmethod
    def BuildTree(data):
        if data is None:
            node=None
        elif isinstance(data, tuple) and len(data)==3:
            node=Tree(data[1])
            node.left=node.BuildTree(data[0])
            node.right=node.BuildTree(data[2])
        else:
            node=Tree(data)
        return node
    
    def Inorder_traversal(self):
        if self is None:
            return []
        return Tree.Inorder_traversal(self.left)+[self.data]+Tree.Inorder_traversal(self.right)
    
    def Preorder_traversal(self):
        if self is None:
            return []
        return [self.data]+Tree.Preorder_traversal(self.left)+Tree.Preorder_traversal(self.right)
    
    def Postorder_traversal(self):
        if self is None:
            return []
        return Tree.Postorder_traversal(self.left)+Tree.Postorder_traversal(self.right)+[self.data]
    
    def Height(self):
        if self is None:
            return 0
        return 1+max(Tree.Height(self.left), Tree.Height(self.right))
    
    def no_of_node(self):
        if self is None:
            return 0
        return 1+Tree.no_of_node(self.left)+Tree.no_of_node(self.right)
    
    def min_node(self):
        if self.left is None:
            return self.data
        return self.left.min_node()
    
    def max_node(self):
        if self.right is None:
            return self.data
        return self.right.max_node()
    
    def find_sum(self): 
        if self.left:
            left_sum=self.left.find_sum()
        else:
            left_sum=+0
        if self.right:
            right_sum=self.right.find_sum()
        else:
            right_sum=+0
        return self.data+right_sum+left_sum
        
    
    def To_tuple(self):
        if self is None:
            return None
        elif self.left is None and self.right is None:
            return self.data
        return Tree.Preorder_traversal(self)
    
    
tree_tuple=((1,3,None), 2, ((None, 3, 4), 5, (6, 7, 8)))
tree = Tree.BuildTree(tree_tuple)
print(tree.Inorder_traversal())
print(tree.Preorder_traversal())
print(tree.Postorder_traversal())
print(tree.Height())
print(tree.no_of_node())
print(tree.min_node())
print(tree.max_node())
print(tree.To_tuple())
print(tree.find_sum())
