#Selection sort(sir version)
L=list(map(int,input().split(" ")))
n=len(L)
# print(n)
for j in range(0,n):
    pos=j
    min=L[j]
    for i in range(j,n):
        if L[i]<min:
            min=L[i]
            pos=i
            L[j],L[pos]=L[pos],L[j] #swap
print(L)