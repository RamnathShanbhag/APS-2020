INT_BITS = 32
def leftRotate(n, d): 
    return (n << d)|(n >> (INT_BITS - d)) 
 
def rightRotate(n, d): 
    return (n >> d)|(n << (INT_BITS - d)) & 0xFFFFFFFF
  
n = int(input())
d = int(input())
print("Left rotation = ",leftRotate(n, d)) 
print("Right rotation = ",rightRotate(n, d)) 
