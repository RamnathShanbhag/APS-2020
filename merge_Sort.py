def mergeSort(arr): 
    if len(arr) >1: 
        mid = len(arr)//2  
        L = arr[:mid] 
        R = arr[mid:]  
        mergeSort(L) 
        mergeSort(R)  
        i = j = k = 0
        while i < len(L) and j < len(R): 
            if L[i] < R[j]: 
                arr[k] = L[i] 
                i+=1
            else: 
                arr[k] = R[j] 
                j+=1
            k+=1
        while i < len(L): 
            arr[k] = L[i] 
            i+=1
            k+=1     
        while j < len(R): 
            arr[k] = R[j] 
            j+=1
            k+=1

n=int(input())
array=list(map(int,input().split()))
mergeSort(array)
print("sorted array is")
for i in array:
	print(i,end=" ")
print()
