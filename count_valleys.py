#Print single integer that says number of valleys in the diven string of up(U) and down(D).

def countingValleys(n, s):
    v=0
    l=0
    for i in s:
        if(i=="U"):
            l=l+1
            if(l==0):
                v=v+1
        else:
            l=l-1
    return(v)

n=int(input())
s=input()
print(countingValleys(n,s))
