import sys
def minCubes(n):
	table=[0]*(n+1)
	j=1
	t=1
	table[0]=0
	for i in range(1,n+1):
		table[i]=sys.maxsize
		while(j<=i):
			if(j==i):
				table[i]=1
			elif(table[i]>table[i-j]):
				table[i]=table[i-j]+1
			t+=1
			j=t*t*t
		t=j=1
	return(table[n])

n=int(input())
res=minCubes(n)
print(res)
