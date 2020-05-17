def frequency(a, x): 
    count = 0
    for i in a: 
        if i == x: count += 1
    return count 
  
a = list(map(int,input().split()))
x = int(input())
print("User defined = ",frequency(a, x))
print("Inbuilt function = ",a.count(x))
