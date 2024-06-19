#Right View
class node:
    def __init__(self,data):
        self.value=data
        self.left=None
        self.right=None
        
    def rightview(root):
        Q=[root]
        Q.append(None)
        # print(root.value)
        while len(Q)>0:
            curr=Q.pop(0)
            if curr==None:
                if len(Q)==0:
                    return
                else:
                    print()
                    Q.append(None)
            else:
                if Q[0]==None:
                    print(curr.value,end=" ")
                if curr.left!=None:
                    Q.append(curr.left)
                if curr.right!=None:
                    Q.append(curr.right)
        
    
    
if __name__=="__main__":
    root=node(1)
    root.left=node(2)
    root.right=node(3)
    root.left.left=node(4)
    root.left.right=node(5)
    root.right.left=node(6)
    root.right.right=node(7)
    root.left.right.left=node(9)
    root.left.right.right=node(10)
    root.right.right.right=node(11)
    root.left.right.left.left=node(12)
    root.left.right.left.right=node(13)
    node.rightview(root)