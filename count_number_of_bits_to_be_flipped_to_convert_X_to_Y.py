def countSetBits(n):
    count = 0
    while n: 
        count += 1
        n &= (n-1) 
    return count 

def flippedBits(x,y):
    return countSetBits(x^y) 

x=int(input())
y=int(input())
res=flippedBits(x,y)
print(res)
