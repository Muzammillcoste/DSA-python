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
    
    
    
    
    
tree_tuple=((1,3,None), 2, ((None, 3, 4), 5, (6, 7, 8)))
tree = Tree.BuildTree(tree_tuple)
