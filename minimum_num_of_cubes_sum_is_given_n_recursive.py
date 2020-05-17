def minCubes(n):
	if(n<8):
		return n
	res=n
	for i in range(1,n+1):
		if((i*i*i)>n):
			return res
		res=min(res,minCubes(n-(i*i*i))+1)
	return res

n=int(input())
res=minCubes(n)
print(res)
