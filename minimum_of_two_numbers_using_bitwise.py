def minimum(x,y):
	return y ^ ((x ^ y) & -(x < y))

a,b=map(int,input().split())
res=minimum(a,b)
print(res)
