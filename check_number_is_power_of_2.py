def check(n):
	return(n and (not(n&(n-1))))

n=int(input())
res=check(n)
if(res==1):
	print("YES")
else:
	print("NO")
