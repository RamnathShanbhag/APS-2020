def check(array):
	result=array[0]
	for i in array:
		result^=array[i]
	return(result)
n=int(input())
array=list(map(int,input().split()))
res=check(array)
print(res)
