#prim's algorithm
graph=[
    [0,7,-1,-1,-1,-1,-1,2,-1,-1],
    [7,0,4,1,-1,5,-1,-1,-1,-1],
    [-1,4,0,-1,-1,-1,-1,8,-1,-1],
    [-1,1,-1,0,6,8,3,3,-1,-1],
    [-1,-1,-1,6,0,-1,-1,6,8,-1],
    [-1,5,-1,8,-1,0,-1,-1,-1,-1],
    [-1,-1,-1,3,-1,-1,0,-1,9,2],
    [2,-1,8,3,6,-1,-1,0,-1,-1],
    [-1,-1,-1,-1,8,-1,9,-1,0,-1],
    [-1,-1,-1,-1,-1,-1,2,-1,-1,0],
]
visited=[False]*len(graph)
min=float('inf')
x=y=-1
# print(min)
for i in range(len(graph)):
    for j in range(len(graph[i])):
        if graph[i][j]==0 or graph[i][j]==-1:
            continue
        elif min>graph[i][j]:
            min=graph[i][j]
            x=i
            y=j
# print(x+1,y+1,min)
visited[x]=True
visited[y]=True
MST=[]
MST.append(tuple((x+1,y+1,min)))
while False in visited:
    min=float('inf')
    for i in range(len(visited)):
        if visited[i]==True:
            for j in range(len(graph[i])):
                if graph[i][j]==0 or graph[i][j]==-1 or visited[j]==True:
                    continue
                elif min>graph[i][j]:
                    min=graph[i][j]
                    x=i
                    y=j
    visited[y]=True
    MST.append(tuple((x+1,y+1,min)))
for i in MST:
    print(i)