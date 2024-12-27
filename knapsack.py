#0/1 Knapsack

p = [0,1,2,5,6] #profits
w = [0,2,3,4,5] #weights

max_weight = 8

a = [] #bottom up table
for i in range(5):
    l=[]
    for j in range(max_weight+1):
        l.append(0)
    a.append(l)
    

for i in range(5):
    for j in range(max_weight+1):
        if(i==0 or j==0):
            a[i][j] = 0;
        else:
            ind = j - w[i]
            if(ind<0):
                a[i][j] = a[i-1][j]
            else:
                a[i][j] = max(a[i-1][j],(a[i-1][ind] + p[i]))

max = a[4][8]
i = 4
j = 8

selected = [0,0,0,0]
while(True): #backtracking
    if(max==0):
        break
    if(a[i][j]==max):
        if(a[i-1][j]==max):
            i = i-1
            continue
        else:
            selected[i-1] = 1
            max = max - p[i]
            for k in range(j):
                if(a[i][k] == max):
                    j = k
                    continue
    else:
        j = j-1
        continue

for i in range(5):
    for j in range(max_weight+1):
        print(a[i][j],end = " ")
    print("\n")
    

print("Selected elements:",selected)
    
    
    
            
