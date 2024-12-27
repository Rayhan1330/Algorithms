import copy



def prims(a,p,visit,count):
    if(count == len(a)-1):
        return p
    min = 9999
    if(count==0):
        for i in range(len(a)):
            for j in range(len(a)):
                if(a[i][j]<min and a[i][j]!=0):
                    min = a[i][j]
                    min_i = i
                    min_j = j
    else:
        for i in range(len(a)):
            for j in range(len(a)):
                if(a[i][j]<min and a[i][j]!=0 and (visit[i]==1 or visit[j]==1) and not(visit[i]==1 and visit[j]==1)):
                    min = a[i][j]
                    min_i = i
                    min_j = j
    print(min,min_i,min_j)
    visit[min_i] = 1
    visit[min_j] = 1
    p[min_i][min_j] = min
    p[min_j][min_i] = min
    count = count+1
    return prims(a,p,visit,count)


a =  [[0,3,0,0,6,5],[3,0,1,0,0,4],[0,1,0,6,0,4],[0,0,6,0,8,5],[6,0,0,8,0,2],[5,4,4,5,2,0]]
n = len(a)
p = []
for i in range(len(a)):
    l = []
    for j in range(len(a)):
        l.append(0)
    p.append(l)
visit = [0 for _ in range(n)]
print(prims(a,p,visit,0))
