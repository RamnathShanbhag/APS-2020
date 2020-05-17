#Given an array of integers, find and print the maximum number of integers you can select from the array such that the absolute difference between any two of #the chosen integers is less than or equal to 

def count_int(a,n):
    d=1
    maxi=0
    for i in a:
        val1=a.count(i)
        val2=a.count(i-d)
        maxi=max(maxi,val1+val2)
    return maxi

n=int(input())
array=list(map(int,input().split()))
res=count_int(array,n)
print(res)
