#Rotate strinf alphabeticwise k number of times"

def encryptCaesar(s, k):
    output = list(s)
    k %= (ord('z') - ord('a') + 1)
     
    for idx, l in enumerate(output):
        if l.isalpha():
            if l.isupper():
                new_char = ord(l)+k
                if new_char > ord('Z'):
                    new_char = new_char - ord('Z') + ord('A') - 1
                output[idx] = chr(new_char)
            else:
                new_char = ord(l)+k
                if new_char > ord('z'):
                    new_char = new_char - ord('z') + ord('a') - 1
                output[idx] = chr(new_char)
    return ''.join(output)

s=input()
k=int(input())
print(encryptCaesar(s,k))

