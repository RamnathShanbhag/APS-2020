def binomialCoefficient(x,y):
	if(y>(x-y)):
		y=x-y
	result=1
	for i in range(y):
		result=result*(x-i)
		result=result/(i+1)
	return result
		
def catalan(n):
	cn=binomialCoefficient(2*n,n)
	return(int(cn/(n+1)))

n=int(input())
for i in range(n):
	res=catalan(i)
	print(res)
