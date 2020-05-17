def binomialCoefficient(n , k): 
    if k==0 or k ==n : 
        return 1
    return binomialCoefficient(n-1 , k-1) + binomialCoefficient(n-1 , k) 

n=int(input())
k=int(input())
print("The coefficient value is",binomialCoefficient(n,k))
