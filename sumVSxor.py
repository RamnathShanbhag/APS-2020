def sumXor(n):
    if(n==0):
        return(1)
    val=bin(n)
    count=0
    for i in range(2,len(val)):
        if(val[i]=="0"):
            count+=1
    return(1<<count)

n=int(input())
print(sumXor(n))
