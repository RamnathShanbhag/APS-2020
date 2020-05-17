#Given a list of unsorted integers, arr, find the pair of elements that have the smallest absolute difference between them. If there are multiple pairs, find them all.
import sys
def closestNumbers(arr):
    arr.sort()
    minimum=sys.maxsize
    result=[]
    for i in range(len(arr)-1):
        if(abs(arr[i+1]-arr[i])>minimum):
            continue
        if(abs(arr[i+1]-arr[i])<minimum):
            minimum=abs(arr[i+1]-arr[i])
            result=[]
            result.append(arr[i])
            result.append(arr[i+1])
        elif(abs(arr[i+1]-arr[i])==minimum):
            result.append(arr[i])
            result.append(arr[i+1])
    return(result)

n=int(input())
array=list(map(int,input().split()))
res=closestNumbers(array)
print(res)
