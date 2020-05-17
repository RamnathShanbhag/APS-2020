import math  
def checkPerfectcube(n): 
    cube_root = n**(1./3.) 
    if round(cube_root) ** 3 == n: 
        return True
    else: 
        return False

def largestPerfectcubeNumber(a, n): 
    maxi = -1
    for i in range(0, n, 1): 
        if (checkPerfectcube(a[i])): 
            maxi = max(a[i], maxi) 
    return maxi; 

n=int(input())
array=list(map(int,input().split()))
print(largestPerfectcubeNumber(array,n))
