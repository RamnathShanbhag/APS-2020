def bubbleSort(arr,n): 
    for i in range(n): 
        swapped = False
        for j in range(0, n-i-1): 
            if arr[j] > arr[j+1] : 
                arr[j], arr[j+1] = arr[j+1], arr[j] 
                swapped = True
        if swapped == False: 
            break

n=int(input())
array=list(map(int,input().split()))
bubbleSort(array,n)
print("sorted array is")
for i in array:
	print(i,end=" ")
print()
