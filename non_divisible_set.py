#Given a set of distinct integers S, print the size of a maximal subset of S  where the sum of any  numbers in S'  is not evenly divisible by  k.

def nonDivisibleSubset(k, s): 
    f = [0 for i in range(k)] 
    for i in range(len(s)): 
        f[s[i] % k] += 1
    if (k % 2 == 0): 
        f[k//2] = min(f[k//2], 1) 
    res = min(f[0], 1) 
    for i in range(1,(k // 2) + 1): 
        res += max(f[i], f[k - i]) 
    return res 

n,k=map(int,input().split())
s=list(map(int,input().split()))
res=nonDivisibleSubset(k,s)
print(res)

