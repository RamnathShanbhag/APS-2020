from math import ceil,sqrt
def minSquares(n):
	table=[0,1,2,3]
	for i in range(4,n+1):
		table.append(i)
	for x in range(1,int(ceil(sqrt(i)))+1):
		temp=x*x
		if(temp>i):
			break
		else:
			table[i]=min(table[i],1+table[i-temp])
	return table[n]

n=int(input())
res=minSquares(n)
print(res)
