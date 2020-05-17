def Add(x, y): 
    while (y != 0): 
        carry = x & y 
        x = x ^ y 
        y = carry << 1
    return x 

a,b=map(int,input().split())
print(Add(a,b))
