#Quick sort
#best case:O(n), worst case:O(n log (n))

def divide(L,Low,High):
    P=L[High]
    Pi=High
    j=Low-1
    for i in range(Low,High):
        if L[i]<=P:
            j+=1
            L[i],L[j]=L[j],L[i]
    j+=1
    L[j],L[Pi]=L[Pi],L[j]
    Pi=j
    return Pi
def quick_sort(L,Low,High):
    if Low<High:
        Pi=divide(L,Low,High)
        quick_sort(L,Low,Pi-1)
        quick_sort(L,Pi+1,High)
    return  
if __name__=="__main__":
    L=list(map(int,input().split(" ")))
    quick_sort(L,0,len(L)-1)
    print("sorted array=",L)
