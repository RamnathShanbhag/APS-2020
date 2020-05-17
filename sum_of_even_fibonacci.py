def sum_fibonacci(n):
    if (n < 2) : 
        return 0
    ef1 = 0
    ef2 = 2
    sm= ef1 + ef2  
    while (ef2 <= n) : 
        ef3 = 4 * ef2 + ef1  
        if (ef3 > n) : 
            break
        ef1 = ef2 
        ef2 = ef3 
        sm = sm + ef2 
    return sm 

n=int(input())
res=sum_fibonacci(n)
print(res)
