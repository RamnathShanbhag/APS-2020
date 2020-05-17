l = [[0 for i in range(1001)] for j in range(1001)] 
def initialize(): 
    l[0][0] = 1
    for i in range(1, 1001): 
        l[i][0] = 1
        for j in range(1, i + 1): 
            l[i][j] = (l[i - 1][j - 1] + l[i - 1][j]) 

def nCr(n, r):  
    return l[n][r] 


initialize() 
n = int(input())
r = int(input())
print(nCr(n, r))
