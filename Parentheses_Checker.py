class Stack():
    def __init__(self):
        self.l=[]
    def push(self,d):
        self.l.append(d)
    def pop(self):
        self.l.pop()
    def size(self):
        return len(self.l)
e="[3+7{52/11(3+5)}]"
S=Stack()
OB="[{("
CB=")}]"
flag=0
for i in e:
    if i in OB:
        S.push("[")
        if i in CB:
            x=S.pop()
            if x=='(' or i==')':
                pass
            elif x=='{' or i=='}':
                pass
            elif x=='[' or i==']':
                pass
            else:
                flag=1
                break

if flag==0 and S.size()==0:
    print("Valid")
else:
    print("invalid")