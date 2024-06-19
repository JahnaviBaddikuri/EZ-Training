#Bottom view
class node:
    def __init__(self,value):
        self.value=value
        self.left=None
        self.right=None
        
class node_data:
    def __init__(self,node,Hkey):
        self.node=node
        self.hkey=Hkey

def bottomview(root):
    temp=node_data(root,0)
    Q=[temp]
    Q.append(None)
    Key_Dict={}
    while len(Q)!=0:
        curr=Q.pop(0)
        if curr==None:
                if len(Q)==0:
                    break
                else:
                    Q.append(None)
        else:
            Key_Dict[curr.hkey]=curr.node.value
            if curr.node.left!=None:
                temp=node_data(curr.node.left,curr.hkey-1)
                Q.append(temp)
            if curr.node.right!=None:
                temp=node_data(curr.node.right,curr.hkey+1)
                Q.append(temp)
    for i in sorted(Key_Dict):
        print(Key_Dict[i])
    print(Key_Dict)
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
    bottomview(root)
        