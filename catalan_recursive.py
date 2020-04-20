def catalan(n):
	if(n<=1):
		return 1
	result=0
	for i in range(n):
		result+=catalan(i)*catalan(n-i-1)
	return result
		
n=int(input())
for i in range(n):
	res=catalan(i)
	print(res)
