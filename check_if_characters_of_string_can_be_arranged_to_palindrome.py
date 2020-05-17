def check_string(st):
    nochar=256
    count = [0] *(nochar) 
    for i in range( 0, len(st)) : 
        count[ord(st[i])] = count[ord(st[i])] + 1
    odd=0
    for i in range(0, nochar ) : 
        if (count[i] & 1) : 
            odd = odd + 1
        if (odd > 1) : 
            return False
    return True

str=input()
if(check_string(str)):
	print("Yes")
else:
	print("No")
