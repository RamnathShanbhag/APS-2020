#Given a number n. If the absolute disfference between the number and its reverse is divisible by k,then the number is beautiful. Given the range of two numbers find the count of beautiful numbers.

def beautifulDays(i, j, k):
    count=0
    m=i
    while(m<=j):
        res = list(map(int, str(m)))
        res.reverse()
        res1 = int("".join(map(str, res)))
        if(abs(res1-m)%k==0):
            count+=1
        m+=1
    return(count)  

n=int(input())
m=int(input())
k=int(input())
print(beautifulDays(n,m,k))
