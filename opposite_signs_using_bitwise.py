def oppositeSigns(x, y): 
    return ((x ^ y) < 0)

x = int(input())
y = int(input())
  
if (oppositeSigns(x, y) == True): 
    print("Signs are opposite")
else: 
    print("Signs are not opposite")
