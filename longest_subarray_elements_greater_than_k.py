def subarray(array,n,k):
	count=0
	length=0
	for i in range(n):
		if(array[i]>k):
			count+=1
		else:
			length=max(length,count)
			count=0
	if(count>0):
		length=max(length,count)
	return(length)	

n=int(input())
array=list(map(int,input().split()))
k=int(input())
res=subarray(array,n,k)
print(res)
