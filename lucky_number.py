def isLucky(n): 
    # Function attribute will act as static variable 
    # just for readability, can be removed and used n instead 
    next_position = n 
    if isLucky.counter > n: 
        return 1
    if n % isLucky.counter == 0: 
        return 0
    # Calculate next position of input number 
    next_position = next_position - next_position / isLucky.counter      
    isLucky.counter = isLucky.counter + 1    
    return isLucky(next_position) 

isLucky.counter = 2
n=int(input())
if(isLucky(n)):
	print(n," is a lucky number")
else:
	print(n," is not a lucky number")

