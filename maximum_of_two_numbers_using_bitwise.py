def maximum(x,y):
	return x ^ ((x ^ y) & -(x < y))

a,b=map(int,input().split())
res=maximum(a,b)
print(res)
