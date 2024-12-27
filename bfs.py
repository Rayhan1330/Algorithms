#DFS for graph

def dequeue(l):
    e = l[0]
    l.remove(e)
    return e

def queue(l,e):
   l.append(e)

def bfs(adj,q,visit):
    if(q==[]):
        return 0
    i = dequeue(q)
    print(i+1)
    visit[i] = True
    for j in range(len(adj)):
            if(adj[i][j]!=0 and visit[j]==False and j not in q):
                queue(q,j)
    bfs(adj,q,visit)


a =  [[0,3,0,0,6,5],[3,0,1,0,0,4],[0,1,0,6,0,4],[0,0,6,0,8,5],[6,0,0,8,0,2],[5,4,4,5,2,0]]
v=[]
for i in range(len(a)):
    v.append(False)
q = [0,]
s = bfs(a,q,v)

