#BST
class node:
    def __init__(self,data):
        self.value=data
        self.left=None
        self.right=None

def ins_bst(root,val):
    if root==None:
        return node(val)
    if val<root.value:
        root.left=ins_bst(root.left,val)
    if val>root.value:
        root.right=ins_bst(root.right,val)
    return root

def inorder(root):
    if root:
        inorder(root.left)
        print(root.value)
        inorder(root.right)
list=[4,6,7,3,8,2,5,9,1]
root=node(list.pop(0))
for i in list:
    ins_bst(root,i)
inorder(root)

    