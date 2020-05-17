N=1000001
visited = [0] * N
goesTo = [0] * N
  
def dfs(i) : 
    if (visited[i] == 1) : 
        return 0;  
    visited[i] = 1;  
    x = dfs(goesTo[i]);  
    return (x + 1); 

def no_of_transpositions(array,n):
    for i in range(1, n + 1) : 
        visited[i] = 0;  
    for i in range(n) : 
        goesTo[array[i]] = i + 1;  
    transpositions = 0;  
    for i in range(1, n + 1) : 
        if (visited[i] == 0) : 
            ans = dfs(i);  
            transpositions += ans - 1;  
    return transpositions;

n=int(input())
array=list(map(int,input().split()))
res=no_of_transpositions(array,n)
print(res)
