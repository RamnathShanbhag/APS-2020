#You are given a string containing characters A and B  only. Your task is to change it into a string such that there are no matching adjacent characters. To do this, #you are allowed to delete zero or more characters in the string.
#Your task is to find the minimum number of required deletions.

def alternatingCharacters(s):
    count=0
    for i in range(len(s)-1):
        if(s[i]==s[i+1]):
            count+=1
    return(count)


s=input()
res=alternatingCharacters(s)
print(res)
