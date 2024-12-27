#LCS Problem Using Recursion

def lcs(a,b,i,j):
    if(i == len(a) or j == len(b)):
        return 0
    if(a[i] == b[j]):
        return 1 + lcs(a,b,i+1,j+1)
    else:
        return max(lcs(a,b,i+1,j),lcs(a,b,i,j+1))
        
s = input("Enter string: ")
sub = input("Enter substring: ")

print(lcs(s,sub,0,0))
