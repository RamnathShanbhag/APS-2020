def  countSetBits(n): 
    count = 0
    while (n): 
        count += n & 1
        n >>= 1
    return count 

n=int(input())
res=countSetBits(n)
print(res)
