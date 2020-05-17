def fibonacci(n):
    if (n < 1) : 
        return n 
    if (n == 1)  : 
        return 2
    return ((4 * fibonacci(n-1)) + fibonacci(n-2))

n=int(input())
res=fibonacci(n)
print(res)
