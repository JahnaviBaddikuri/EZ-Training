def check_prime(m):
    flag=0
    if m<1:
        flag=1
    elif m==1:
        flag=0
    for i in range(2,(m//2)+1):
        if m%i==0:
            flag=1
    if(flag==0):
        return 1
    else:
        return 0    

n=int(input(""))
flag=0
result=[]
k=n+1
while(flag<1):
    flag=check_prime(k)
    if flag==1:
        result.append(k)
    else:
        k=k+1
sum=0
for i in range(n+1,k):
    sum+=i
result.append(sum)
p1=k
flag=0
k=p1+1
while(flag<1):
    flag=check_prime(k)
    if flag==1:
        p2=k
    else:
        k=k+1
p3=p1*p2
flag=check_prime(p3)
if flag==0:
    result.append(False)
else:
    result.append(True)
Prime_key=tuple(result)
print(Prime_key)