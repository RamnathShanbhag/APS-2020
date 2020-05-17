#To determine whether a string is funny, create a copy of the string in reverse e.g. abc->cba. Iterating through each string, compare the absolute difference in #the ascii values of the characters at positions 0 and 1, 1 and 2 and so on to the end. If the list of absolute differences is the same for both strings, they are funny.

def funnyString(s):
    #rev="".join(reversed(s))
    list1=[]
    list2=[]
    result_list1=[]
    result_list2=[]
    for i in s:
        list2.append(ord(i))
    list1=list2.copy()
    list2.reverse()
    for i in range(len(list1)-1):
        result_list1.append(abs(list1[i+1]-list1[i]))
    for i in range(len(list2)-1):
        result_list2.append(abs(list2[i+1]-list2[i]))
    if(result_list1==result_list2):
        return("Funny")
    else:
        return("Not Funny")

s=input()
res=funnyString(s)
print(res)
