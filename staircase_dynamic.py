def countWaysUtil(n,m):
    res = [0 for x in range(n)]  
    res[0],res[1] = 1,1
      
    for i in range(2,n): 
        j = 1
        while j<=m and j<=i: 
            res[i] = res[i] + res[i-j] 
            j = j + 1 
    return res[n-1] 

def count_stairs(n,m):
	return countWaysUtil(n+1, m)

n,m=map(int,input().split())
res=count_stairs(n,m)
print(res)
