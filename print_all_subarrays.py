def printSubarray(arr,start,end):
    if end == len(arr): 
        return
    elif start > end: 
        return printSubarray(arr, 0, end + 1) 
    else: 
        print(arr[start:end + 1]) 
        return printSubarray(arr, start + 1, end) 

n=int(input())
array=list(map(int,input().split()))
printSubarray(array,0,0)

