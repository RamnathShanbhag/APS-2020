#Given an array of integers. Print the maximum and minimum sum which can be formed using (n-1) integers
n=int(input())
array=list(map(int,input().split()))
max_array=array.copy()
min_array=array.copy()
max_array.remove(min(array))
min_array.remove(max(array))
print("Minimum sum =",sum(min_array))
print("Maximum sum =",sum(max_array))

