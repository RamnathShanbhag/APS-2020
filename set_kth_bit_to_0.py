def turnOffK(n,k): 
    if (k <= 0):  
        return n 
    return (n & ~(1 << (k - 1)))

n,k=map(int,input().split())
print(turnOffK(n,k))
