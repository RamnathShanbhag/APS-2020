def swapThree(a, b, c): 
    a = a + b + c  
    b = a - (b+c)
    c = a - (b+c) 
    a = a - (b+c)
    print("After swapping a =",a,", b =",b,", c =",c)

a,b,c=map(int,input().split())
print("Before swapping a =",a,", b =",b,", c =",c)
swapThree(a,b,c)
