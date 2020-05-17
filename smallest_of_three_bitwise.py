CHAR_BIT = 8

def minimum(x, y): 
    return y + ((x - y) & ((x - y) >> (32 * CHAR_BIT - 1)))

def smallest(x, y, z): 
    return minimum(x, minimum(y, z))

a,b,c=map(int,input().split())
print(smallest(a,b,c))
