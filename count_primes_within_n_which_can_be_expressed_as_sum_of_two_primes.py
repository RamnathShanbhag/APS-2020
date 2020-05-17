MAX = 100005
prime = [True for i in range(MAX)] 
def SieveOfEratosthenes(): 
    prime[0] = False
    prime[1] = False
    for p in range(MAX): 
        if(p * p > MAX): 
            break
        if (prime[p]): 
            for i in range(2 * p, MAX, p): 
                prime[i] = False

def countPrimes(n): 
    SieveOfEratosthenes() 
    cnt = 0
    for i in range(2, n): 
        if (prime[i] and prime[i - 2]): 
            cnt += 1
    return cnt 

n=int(input())
print(countPrimes(n))
