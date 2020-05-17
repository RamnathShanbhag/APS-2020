#Given an integer, n , find and print the number of letter a's in the first n letters of given infinite string.

def repeatedString(s, n):
    val=n%len(s)
    s1=s.count("a")
    count1=0
    if(val==0):
        return(s1*(int(n/len(s))))
    else:
        val1=int(n/len(s))
        count1=val1*s1
        for i in range(0,val):
            if(s[i]=="a"):
                count1+=1
        return(count1)

n=int(input())
s=input()
print(repeatedString(s,n))
