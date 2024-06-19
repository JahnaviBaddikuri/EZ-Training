#merge Sort 


def merge(left,right):
    i=j=0
    temp=[]

    while i<len(left) and j<len(right):
        if left[i]<right[j]:
            temp.append(left[i])
            i+=1
        else:
            temp.append(right[j])
            j+=1
            
    while i<len(left):
        temp.append(left[i])
        i+=1
        
    while j<len(right):
        temp.append(right[j])
        j+=1

    return temp

def mergesort(L):
    if len(L) <= 1:
        return L
        
    mid = len(L)//2
    left=L[:mid] 
    right=L[mid:]
    
    left_sorted = mergesort(left)
    right_sorted = mergesort(right)
    
    return merge(left_sorted,right_sorted)


if __name__=="__main__":
    L=list(map(int,input().split())) # 4 7 8 3 2 9 1 5
    sorted=mergesort(L)

    print("Sorted Array = ",sorted)