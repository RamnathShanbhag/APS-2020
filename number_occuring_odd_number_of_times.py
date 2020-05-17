def findOdd(array,n):
	val=0
	for i in range(n):
		val^=array[i]
	return(val)

n=int(input())
array=list(map(int,input().split()))
res=findOdd(array,n)
print(res)
