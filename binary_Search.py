def binarySearch (arr, l, r, x): 
    if r >= l: 
        mid = l + (r - l) // 2
        if arr[mid] == x: 
            return mid 
        elif arr[mid] > x: 
            return binarySearch(arr, l, mid-1, x) 
        else: 
            return binarySearch(arr, mid + 1, r, x)  
    else:  
        return -1

n=int(input())
array=list(map(int,input().split()))
k=int(input())
res=binarySearch(array,0,n-1,k)
if(res == -1): 
    print("Element is not present in array") 
else: 
    print("Element is present at index", res) 
