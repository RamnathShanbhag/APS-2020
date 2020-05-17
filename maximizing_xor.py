def maximizingXor(l, r):
    li=[]
    for i in range(l,r+1):
        for j in range(l,r+1):
            val=i^j
            li.append(val)
    return max(li)

l,r=map(int,input().split())
print(maximizingXor(l,r))
