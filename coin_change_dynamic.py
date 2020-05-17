def count(array,n,m):
	table=[0]*(m+1)
	table[0]=1
	for i in range(0,n):
		for j in range(array[i],m+1):
			table[j]+=table[j-array[i]]
	return table[m]

n=int(input())
array=list(map(int,input().split()))
t_sum=int(input())
res=count(array,n,t_sum)
print(res)
