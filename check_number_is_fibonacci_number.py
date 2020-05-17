import math

def isPerfectSquare(x): 
    s = int(math.sqrt(x)) 
    return s*s == x 

def check_fibonacci(n):
	 return isPerfectSquare(5*n*n + 4) or isPerfectSquare(5*n*n - 4)

n=int(input())
res=check_fibonacci(n)
if(res):
	print("YES")
else:
	print("NO")
