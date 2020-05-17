def pangrams(s):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    for char in alphabet: 
        if char not in s.lower(): 
            return("not pangram")
    return("pangram")

s=input()
res=pangrams(s)
print(res)
