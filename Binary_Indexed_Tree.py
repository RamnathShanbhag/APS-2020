def query(BIT,i):
	i+=1
	sum=0
	while(i>0):
		sum+=BIT[i]
		i-=i&(-i)
	return sum

def updateBIT(BIT,n,i,val):
	i+=1
	while(i<=n):
		BIT[i]+=val
		i+=i&(-i)
	return BIT

def constructBIT(array,n):
	BIT=[0]*(n+1)
	for i in range(n):
		BIT=updateBIT(BIT,n,i,array[i])
	return BIT

n=int(input())
array=list(map(int,input().split()))
BIT=constructBIT(array,n)
for i in range(2):
	m=int(input())
	print(query(BIT,m))
for i in range(2):
	j=int(input())
	val=int(input())
	BIT=updateBIT(BIT,n,j,val)
print(BIT)
