# Implementation of 0/1 Knapsack problem 
def knapsack(W_bag,s_a):                                 #function definition
    s_a=sorted(s_a,key=lambda i:i[1],reverse=True)       #sorting the dictionary using lambda function
    result=0                                             #variable for storing result
    for item in s_a:                                     #loop for iterating the value
        if item[0]<W_bag:
            W_bag=W_bag-item[0]                          #weight of bag will decrease by the weight of the item
            result=result+item[1]                        #increment in the value of result by adding value of item
    return result    


W_bag=int(input("Enter the bag size:"))
wt_item=input("Enter the weight of the items:").split()
wt_item=[int(item) for item in wt_item]                  #conversion of weight of item into int
val_item=input("Enter the value of the item:").split()
val_item=[int(item) for item in val_item]                #conversion of value of item into int
s_a=[[wt_item[i],val_item[i]] for i in range(3)]         #pairing weight of item to it's corresponding value
print (s_a)
print(knapsack(W_bag,s_a))                               #function call and printing the result 


