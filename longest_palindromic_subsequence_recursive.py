def longestPalindromicSubsequence(seq, i, j): 
    if (i == j): 
        return 1
    if (seq[i] == seq[j] and i + 1 == j): 
        return 2
    if (seq[i] == seq[j]): 
        return longestPalindromicSubsequence(seq, i + 1, j - 1) + 2
    return max(longestPalindromicSubsequence(seq, i, j - 1),  
               longestPalindromicSubsequence(seq, i + 1, j)) 

string=input()
n=len(string)
res=longestPalindromicSubsequence(string,0,n-1)
print(res)
