#recursion Factorial series
t=[0]
def fact(n):
    t[0]+=1
    if n==0:
        return 0
    if n==1:
        return 1
    return n*fact(n-1)

if __name__=="__main__":
    n=int(input())
    print(fact(n))
    print(t)