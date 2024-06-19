#Leaf nodes
class node:
    def __init__(self,data):
        self.value=data
        self.left=None
        self.right=None
        
def leafnode(root):
     L=[]
     if root.left==None and root.right==None:
        print(root.value)
     if root.left!=None:
         leafnode(root.left)
     if root.right!=None:
         leafnode(root.right)
                    
if __name__=="__main__":
    root=node(1)
    root.left=node(2)
    root.right=node(5)
    root.left.left=node(3)
    root.left.right=node(4)
    root.left.right.left=node(9)
    root.left.right.left.right=node(10)
    root.left.right.left.right.left=node(14)
    root.right.right=node(6)
    root.right.right.left=node(7)
    root.right.right.right=node(8)
    root.right.right.left.right=node(11)
    root.right.right.left.right.left=node(12)
    root.right.right.left.right.left.right=node(13)
    # print(f"The Height of this tree : {node.height(root)}")
    leafnode(root)
    
    