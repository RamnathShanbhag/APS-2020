#Minimum number of elements to be deleted to make the array equal

def equalizeArray(arr):
    count=[]
    for i in range(len(arr)):
        count.append(arr.count(arr[i]))
    return(len(arr)-max(count))

n=int(input())
array=list(map(int,input().split()))
print(equalizeArray(array))

