def isSafe(graph,color):
    for i in range(len(graph)):
        for j in range(i+1,len(graph)):
            if graph[i][j]==1 :
                return False
    return True            

def saveSol(graph,ans):
    temp=[]
    for i in range(n):
        for j in range(n):
            temp.append(graph[i][j])
    ans.append(temp)

def graph(graph,color,n,i):
    if i==n:
        if isSafe(graph,color):
            return True
    return False
    for j in range(1,n+1):
        color[i]=j


def display():
    for i in range(n):
        print[color[i], end=" "]

graph=[[0,1,1,0],
       [1,0,0,1],
       [1,0,0,1],
       [0,1,1,0]]
n=4
ans=[]
color=[0 for i in range(4)]
