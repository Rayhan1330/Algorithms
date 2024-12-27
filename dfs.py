#DFS for graph

def dfs(adj,visit,i):
    print(i)
    visit[i] = True
    for j in range(len(adj)):
            if(adj[i][j]!=0 and visit[j]==False):
                dfs(adj,visit,j)


a =  [[0,3,0,0,6,5],[3,0,1,0,0,4],[0,1,0,6,0,4],[0,0,6,0,8,5],[6,0,0,8,0,2],[5,4,4,5,2,0]]
v=[]
for i in range(len(a)):
    v.append(False)

dfs(a,v,0)
