#Given an integer, for each digit that makes up the integer determine whether it is a divisor. Count the number of divisors occurring within the integer.
def findDigits(n):
    n1=str(n)
    #print(n1)
    count=0
    for i in n1:
        #print(i)
        c=int(i)
        if(c==0):
            continue
        if(n%c==0):
            count+=1
    return count

n=int(input())
print(findDigits(n))
