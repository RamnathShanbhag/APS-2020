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
        else : 
            sum -= arr[start] 
            start += 1
    return count 

n=int(input())
array=list(map(int,input().split()))
k=int(input())
res=count_subarrays(array,n,k)
print(res)
