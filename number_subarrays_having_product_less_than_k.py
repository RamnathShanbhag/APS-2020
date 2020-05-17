def count_subarrays(array,n,k):
    count = 0
    for i in range(0, n): 
        if array[i] <= k: 
            count += 1
        mul = array[i] 
        for j in range(i + 1, n): 
            mul = mul * array[j]  
            if mul <= k:  
                count += 1
            else: 
                break
    return count 

n=int(input())
array=list(map(int,input().split()))
k=int(input())
res=count_subarrays(array,n,k)
print(res)
