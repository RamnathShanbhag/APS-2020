def count_subarrays(arr,n,k):
    start = 0
    end = 0
    count = 0
    sum = arr[0]
    while (start < n and end < n) :
        if (sum < k) :
            end += 1
            if (end >= start):
                count += end - start
            if (end < n):
                sum += arr[end]
        else:
            sum-=arr[start]
            start+=1
    return(count%1000000007)

t=int(input())
for i in range(t):
	n,m,k=map(int,input().split())
	array=list(map(int,input().split()))
	array*=m
	result=count_subarrays(array,len(array),k)
	print(result)
