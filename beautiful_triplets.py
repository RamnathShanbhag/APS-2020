#Given an array of integers,find the count of beautiful triplets. A triplet (a[i],a[j],a[k]) is beautiful if
# 1) i<j<k
# 2) a[j]-a[i]=a[k]-a[j]=d
#Given an increasing sequenc of integers and the value of d, count the number of beautiful triplets in the sequence.

def beautifulTriplets(d, arr):
    count=0
    for i in range(len(arr)):
        if(arr[i]+d in arr and arr[i]+2*d in arr):
            count+=1
    return(count)

n,d=map(int,input().split())
array=list(map(int,input().split()))
res=beautifulTriplets(d,array)
print(res)
