import math

def count_subsequences(arr,n):
    pos_count = 0;  
    neg_count = 0
    for i in range (n): 
        if (arr[i] > 0) : 
            pos_count += 1
        if (arr[i] < 0):  
            neg_count += 1
    result = int(math.pow(2, pos_count))  
    if (neg_count > 0): 
        result *= int(math.pow(2, neg_count - 1))  
    result -= 1  
    return result 

n=int(input())
array=list(map(int,input().split()))
res=count_subsequences(array,n)
print(res)
