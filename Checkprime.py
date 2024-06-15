def check_point(h):
    flag=False
    for i in range(1,len(h)):
        m=h[i]
        left=[]
        right=[]
        left=h[0:i]
        right=h[i:]
        if sum(left)==sum(right):
            p=i
            return (h[p])
            flag=True
    if flag==False:
        m=len(h)//2
        return (h[m])

dic={}
for i in range(7):
    i=list(map(int,input().split(" ")))
    dic[f'gate{i}']=check_point(i)
print(dic)  