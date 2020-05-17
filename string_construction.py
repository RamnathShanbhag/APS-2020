#Amanda has a string of lowercase letters that she wants to copy to a new string. She can perform the following operations with the given costs. She can perform them any number of times to construct a new string : p
# 1)Append a character to the end of string p at a cost of 1 dollar.
# 2)Choose any substring of p and append it to the end of p at no charge.

def stringConstruction(s):
    return(len(set(s)))

s=input()
print(stringConstruction(s))

