def flippingBits(n):
    val=(2**32)-1
    return(val-n)

n=int(input())
print(flippingBits(n))
