def catalan(n):
	if(n==0 or n==1):
		return 1
	catalan=[0]*(n+1)
	catalan[0]=1
	catalan[1]=1
	for i in range(2,n+1):
		catalan[i]=0
		for j in range(i):
			catalan[i]=catalan[i]+catalan[j]*catalan[i-j-1]
	return catalan[n]
	
n=int(input())
catalan_array=[]
for i in range(n):
	res=catalan(i)
	catalan_array.append(res)
array=list(map(int,input().split()))
count=0
for i in range(n):
	if(array[i]!=catalan_array[i]):
		array[i]=catalan_array[i]
		count+=1
print(array)
print(count)
