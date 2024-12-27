#Dijkstra's Algorithm to find single source shortest path

def min_dist(dist,path):
    min = 9999
    for i in range(len(dist)):
        if(dist[i]<min and path[i] == False):
            min = dist[i]
            min_ind = i
    return min_ind

def dijkstra(adj,src,dist,path):
    dist[src] = 0
    for i in range(len(adj)):
        u = min_dist(dist,path)
        path[u] = True
        for j in range(len(adj)):
            if(adj[u][j]!=0):
                dist[j] = min(dist[j],dist[u] + adj[u][j])
                


a = [ [ 0, 8, 0, 0, 0, 5, 0, 2, 0 ],
      [ 7, 0, 5, 0, 0, 0, 0, 11, 0 ],
      [ 0, 8, 0, 7, 0, 6, 0, 0, 2 ],
      [ 0, 0, 7, 0, 9, 14, 0, 0, 0 ],
      [ 0, 0, 0, 9, 0, 10, 0, 0, 0 ],
      [ 0, 0, 5, 14, 10, 0, 2, 0, 0 ],
      [ 0, 0, 4, 0, 0, 2, 0, 1, 6 ],
      [ 5, 15, 0, 0, 0, 0, 3, 0, 9 ],
      [ 0, 0, 1, 0, 0, 0, 6, 8, 0 ]]

dist = []
path = []
for i in range(len(a)):
    dist.append(9999)
    path.append(False)
src = int(input("Enter source vertex: "))
dijkstra(a,src,dist,path)
for i in range(len(dist)):
    print("Vertex:",i,"Distance:",dist[i])
