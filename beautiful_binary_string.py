#Alice has a binary string. She thinks a binary string is beautiful if and only if it doesn't contain the substring "010" .
#In one step, Alice can change a 0 to a 1 or vice versa. Count and print the minimum number of steps needed to make Alice see the string as beautiful.

def beautifulBinaryString(b):
    return(b.count("010"))

b=input()
res=beautifulBinaryString(b)
print(res)
