#Longest Common Subsequence Problem Using Dynamic Programming

s = input("Enter a string: ")
sub_s = input("Enter the substring: ")

s = '0' + s
sub_s = '0' + sub_s

table = [] #bottom up table
for i in range(len(sub_s)):
    l = []
    for j in range(len(s)):
        l.append(0)
    table.append(l);

for i in range(len(sub_s)):
    for j in range(len(s)):
        if(i==0 or j==0):
            table[i][j] = 0
        else:
            if(s[j] == sub_s[i]):
                table[i][j] = table[i-1][j-1] + 1
            else:
                table[i][j] = max(table[i-1][j],table[i][j-1])
            
i = len(sub_s) - 1
j = len(s) - 1
max = table[i][j]

str = " "

while(True): #backtracking
    if(max == 0):
        break
    if(max == table[i][j]):
        if(table[i-1][j] == max):
            i = i-1
            continue
        elif(table[i][j-1]==max):
            j = j-1
            continue
        else:
            max = max - 1
            str = sub_s[i] + str
            continue
    else:
        j = j-1
        continue

for i in range(len(sub_s)):
    for j in range(len(s)):
        print(table[i][j],end = " ")
    print("\n")

print("Subsequence is:",str)
