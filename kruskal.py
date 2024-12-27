import copy

def floyd(a):
    p = copy.deepcopy(a)
    for i in range(len(a)):
        for j in range(len(a)):
            if(p[i][j]==0):
                p[i][j] = 9999
    for k in range(len(a)):
        for i in range(len(a)):
            for j in range(len(a)):
                if(p[i][j]>p[i][k]+p[k][j]):
                    p[i][j] = p[i][k] + p[k][j]
    return p

def kruskal(a,p,visit,count):
    if(count == len(a)-1):
        return p
    else:
        min = 9999
        for i in range(len(a)):
            for j in range(len(a)):
                im = floyd(p)
                if(a[i][j]<min and a[i][j]!=0 and im[i][j]==9999):
                    min = a[i][j]
                    min_i = i
                    min_j = j
    p[min_i][min_j] = min
    p[min_j][min_i] = min
    visit[min_i] = 1
    visit[min_j] = 1
    return kruskal(a,p,visit,count+1)
        
a =  [[0,3,0,0,6,5],[3,0,1,0,0,4],[0,1,0,6,0,4],[0,0,6,0,8,5],[6,0,0,8,0,2],[5,4,4,5,2,0]]
n = len(a)
p = []
for i in range(len(a)):
    l = []
    for j in range(len(a)):
        l.append(0)
    p.append(l)
visit = [0 for _ in range(n)]
print(kruskal(a,p,visit,0))
#print(floyd(a))
#print(a)
