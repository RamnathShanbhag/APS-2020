def count(array,n,m):
	if(m==0):
		return 1
	if(m<0):
		return 0
	if(n<=0 and m>=1):
		return 0
	return count(array,n-1,m)+count(array,n,m-array[n-1])

n=int(input())
array=list(map(int,input().split()))
t_sum=int(input())
res=count(array,n,t_sum)
print(res)
