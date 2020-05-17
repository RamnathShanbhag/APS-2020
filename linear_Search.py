def linearSearch(arr, n, x): 
    for i in range (0, n): 
        if (arr[i] == x): 
            return i
    return -1; 

n=int(input())
array=list(map(int,input().split()))
k=int(input())
res=linearSearch(array,n,k)
if(res == -1): 
    print("Element is not present in array") 
else: 
    print("Element is present at index", res) 
