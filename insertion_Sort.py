def insertionSort(arr): 
    for i in range(1, len(arr)): 
        key = arr[i] 
        j = i-1
        while j >= 0 and key < arr[j] : 
                arr[j + 1] = arr[j] 
                j -= 1
                print(arr)	
        arr[j + 1] = key 

n=int(input())
array=list(map(int,input().split()))
insertionSort(array)
print("sorted array is")
for i in array:
	print(i,end=" ")
print()
