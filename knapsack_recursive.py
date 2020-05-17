def knapSack(W , wt , val , n):  
    if n == 0 or W == 0 : 
        return 0
    if (wt[n-1] > W): 
        return knapSack(W , wt , val , n-1) 
    else: 
        return max(val[n-1] + knapSack(W-wt[n-1] , wt , val , n-1), 
                   knapSack(W , wt , val , n-1))

val=list(map(int,input().split()))
wt=list(map(int,input().split()))
w=int(input())
res=knapSack(w,wt,val,len(val))
print(res)
