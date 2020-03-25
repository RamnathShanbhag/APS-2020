import sys
def kadane(li,n):
    max1=-sys.maxsize-1
    tmax=0
    for i in range(n):
        tmax+=li[i]
        if(max1<tmax):
            max1=tmax
        if(tmax<0):
            tmax=0
    return(max1)
n=int(input())
li=list(map(int,input().split()))
res=kadane(li,n)
print(res)
