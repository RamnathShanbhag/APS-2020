#You will be given two arrays of integers and asked to determine all integers that satisfy the following two conditions:
# 1)The elements of the first array are all factors of the integer being considered
# 2)The integer being considered is a factor of all elements of the second array
#These numbers are referred to as being between the two arrays. You must determine how many such numbers exist.

def getTotalX(a, b):
    # Write your code here
    count=0
    for i in range(max(a),min(b)+1):
        for j in a:
            if i%j!=0:
                break
        else:
            for k in b:
                if k%i!=0:
                    break
            else:
                count+=1
    return(count)

n,m=map(int,input().split())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
print(getTotalX(a,b))
