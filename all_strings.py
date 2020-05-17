# Given a list of strings conatining characters from [a-z],print the number of characters which is present in all the characters.
def allStrings(arr):
    maximum=0
    s=list(set(arr[0]))
    re_count=1
    count=0
    for i in range(len(s)):
        re_count=1
        for j in range(1,len(arr)):
            if(s[i] in arr[j]):
                re_count+=1
        if(re_count==len(arr)):
            count+=1
    return(count)

n=int(input())
array=list(map(str,input().split()))
res=allStrings(array)
print(res)

