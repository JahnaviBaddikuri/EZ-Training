class Stack:
    def __init__(self):
        self.items = []
    def push(self,data):
        self.items.append(data)
    def pop(self):
        return self.items.pop()
    def size(self):
        return len(self.items)
    def top(self):
        return self.items[-1]

        
L= [3,5,2,14,5,3,7,9,4,6,9,4,2,5,3]
O=[0]*len(L)
s= Stack()
for i in range(len(L)-1,-1,-1):
    if s.size() != 0:
        while s.size() !=0 and s.top()<=L[i]:
            if s.top() <= L[i]:
                s.pop()
    if s.size() == 0:
        O[i]=-1
    else:
        O[i]=s.top()
    s.push(L[i])
print(O)