def diagonalDifference(arr):
    # Write your code here
    sum1=0
    sum2=0
    for i in range(len(arr)):
        sum1=sum1+arr[i][i]
        sum2=sum2+arr[i][len(arr)-i-1]
    return(abs(sum1-sum2))

n=int(input())
array=[]
for i in range(n):
	li=list(map(int,input().split()))
	array.append(li)
print(diagonalDifference(array))
