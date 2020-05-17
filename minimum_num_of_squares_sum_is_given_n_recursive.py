def minSquares(n):
	if(n<=3):
		return n
	result=n
	for x in range(1,n+1):
		temp=x*x
		if(temp>n):
			break
		else:
			result=min(result,1+minSquares(n-temp))
	return result

n=int(input())
res=minSquares(n)
print(res)
