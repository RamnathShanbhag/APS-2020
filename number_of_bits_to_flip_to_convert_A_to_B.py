def countSetBits( n ): 
    count = 0
    while n: 
        count += 1
        n &= (n-1) 
    return count 

def FlippedCount(a , b): 
    return countSetBits(a^b) 
  
a = int(input())
b = int(input())
print(FlippedCount(a, b)) 
