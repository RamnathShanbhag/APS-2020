from math import log2
def findNum(array,n):
	itr=array[0]
	for i in range(n):
		if(array[i]>itr):
			itr=array[i]
	p=int(log2(itr))+1
	x=0
	for i in range(p):
		count=0
		for j in range(n):
			if(array[j]&(1<<i)):
				count+=1
		if(count>int(n/2)):
			x+=(1<<i)
	sum1=0
	for i in range(n):
		sum1+=(x^array[i])
	return(x,sum1)
			
n=int(input())
array=list(map(int,input().split()))
res1,res2=findNum(array,n)
print("number = ",res1)
print("Sum =",res2)
