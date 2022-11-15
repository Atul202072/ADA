def knapsack(k_size,item_no):
    for i in range(m):
        for j in range(n):
            if i==0:
                if w[i]<=j:
                    KM[i][j]