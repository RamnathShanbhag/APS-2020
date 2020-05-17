#Given two strings, determine if they share a common substring. A substring may be as small as one character.


def twoStrings(s1, s2):
    for i in s1:
        if i in s2:
            return("YES")
    return("NO")

s1=input()
s2=input()
print(twoStrings(s1,s2))
