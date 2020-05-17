from math import sqrt 
MAX = 10000
prefix = [0 for i in range(MAX + 1)] 
# Function to build the prefix sum array 
def buildPrefix(): 
    # Create a boolean array "prime[0..n]". A 
    # value in prime[i] will finally be false 
    # if i is Not a prime, else true. 
    prime = [True for i in range(MAX + 1)] 
    for p in range(2,int(sqrt(MAX)) + 1, 1): 
        # If prime[p] is not changed, then 
        # it is a prime 
        if (prime[p] == True): 
            # Update all multiples of p 
            for i in range(p * 2, MAX + 1, p): 
                prime[i] = False
    # Build prefix array 
    prefix[0] = 0
    prefix[1] = 0
    for p in range(2, MAX + 1, 1): 
        prefix[p] = prefix[p - 1] 
        if (prime[p]): 
            prefix[p] += p 
  
# Function to return sum of prime in range 
def sumPrimeRange(L, R): 
    buildPrefix() 
    return prefix[R] - prefix[L - 1]

l,r=map(int,input().split())
print(sumPrimeRange(l,r))
