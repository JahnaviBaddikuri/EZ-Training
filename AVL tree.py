#AVL tree
class node:
    def __init__(self,data):
        self.val=data
        self.left=None
        self.right=None
        self.height=1

def insert(root,super):
    if not root:
        return node(super)
    if super<root.val:
        root.left = insert(root.left,super)
    else:
        root.right=insert(root.right,super)

    root.height = 1 + max(ght(root.left),ght(root.right))

    BF=getBF(root)
    
    #RR Rotation
    if BF>1 and super<root.left.val:
        return rightRotate(root)
    #RL Rotation    
    if BF>1 and super>root.left.val:
        root.left=leftRotate(root.left)
        return rightRotate(root)

    #LL Rotation
    if BF<-1 and super>root.right.val:
        return leftRotate(root)
    #LR Rotation
    if BF<-1 and super<root.right.val:
        root.right=rightRotate(root.right)
        return leftRotate(root)
    return root
    
def ght(root):#returns the height of the root
    if not root: 
        return 0
    return root.height

def  getBF(root):#return the Balance Factor of the root
    if not root:
        return 0
    return ght(root.left)-ght(root.right)

def leftRotate(A):#Left rotation
    B=A.right
    temp=B.left

    B.left=A
    A.right=temp

    A.height = 1 + max(ght(A.left),ght(A.right))
    B.height = 1 + max(ght(B.left),ght(B.right))

    return B

def rightRotate(A):#Right rotation
    B=A.left
    temp=B.right

    B.right=A
    A.left=temp

    A.height = 1 + max(ght(A.left),ght(A.right))
    B.height = 1 + max(ght(B.left),ght(B.right))

    return B
    
    
def inorder(root):#prints the data in inorder format
    if not root:
        return
    inorder(root.left)
    print(root.val)
    inorder(root.right)

if __name__=="__main__":
    root=None
    VL=[19,99,75,7,21,34,38,27,134,100,29,0,12,17,143]
    for i in VL:
        root=insert(root,i)
    inorder(root)