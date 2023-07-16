class TreeNode:
    def __init__(self, val =0 , left=None , right=None):
        self.val = val
        self.left = None
        self.right = None

def BinaryTree(self,root) -> int:

    if root is None:
        return 0
    
    return 1 + max(self.BinaryTree(root.right),self.BinaryTree(root.left))












    

  


