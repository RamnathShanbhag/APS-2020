def selectionSort(A):
	for i in range(len(A)): 
            min_idx = i 
            for j in range(i+1, len(A)): 
                if A[min_idx] > A[j]: 
                    min_idx = j      
            A[i], A[min_idx] = A[min_idx], A[i] 

n=int(input())
array=list(map(int,input().split()))
selectionSort(array)
print("sorted array is")
for i in array:
	print(i,end=" ")
print()
