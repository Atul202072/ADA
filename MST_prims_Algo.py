#function that return the MST using PRIM's Algorithm
INF = 9999999
N = 5                                                          # number of vertices in graph
G = [[0, 10, 20, 30, 40],                                      #creating graph by adjacency matrix method
     [10, 0, 50, 60, 70],
     [20, 50, 0, 80, 90],
     [30, 60, 80, 0, 100],
     [40, 70, 90, 100, 0]]
selected_node = [0, 0, 0, 0, 0]                                #To select node
no_edge = 0
selected_node[0] = True
print("Edge : Weight\n")                                       # printing for edge and weight
while (no_edge < (N - 1)):                                     #exit condition 
    minimum = INF
    a = 0
    b = 0
    for m in range(N):
        if selected_node[m]:
            for n in range(N):
                if ((not selected_node[n]) and G[m][n]):  
                    # not in selected and there is an edge
                    if minimum > G[m][n]:
                        minimum = G[m][n]
                        a = m
                        b = n
    print(str(a) + "-" + str(b) + ":" + str(G[a][b]))
    selected_node[b] = True
    no_edge = no_edge+1


