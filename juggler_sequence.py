import math
def Juggler(n):
	a=n
	print(a)
	while(a!=1):
		b=0
		if(a%2==0):
			b=math.floor(math.sqrt(a))
		else:
			b=math.floor(math.sqrt(a)**3)
		print(b)
		a=b

n=int(input())
Juggler(n)
