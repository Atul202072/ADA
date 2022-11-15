#function to find the shortest path
INF=9999                                                              #infinite point for matrix
def Sortest_Path(node,arr):                                           #function for finding the minimum cost
    if node<0:
        print("Please enter the node length [greater than 0]")
    else:    
        for k in range (node):                                        #k is intermediate node 
            for i in range (node):                                    #i is source   
                for j in range (node):                                #j is destination
                        arr[i][j]=min(arr[i][j],arr[i][k]+arr[k][j])  #least cost of the node is added in the i,j cell of the matrix
                        print(arr[i][j],end=" ")
                print(" ")  

        
        
arr=[[0,5,2,INF],                                                     #user defined matrix
     [INF,0,4,3],
     [3,INF,0,3],
     [INF,INF,INF,0]]
     
# if no node is selected
node=0                                                                #number of nodes
Sortest_Path(node,arr)                                                #function call

#if node selected
node=4
Sortest_Path(node,arr)                                                







    