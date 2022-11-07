# function to find Duplicate values in the List
def func(arr):                                           #function definition
    result=set([])                                       #empty set for storing the result
    for i in range(len(arr)):                            # iterative approach for solution
        for j in range(len(arr)):
            if arr[i]==arr[j] and i!=j:
                result.add(arr[i])                       #adding each result into the empty set
    return result       

arr=[1,2,2,3,4,5,8,1,3]                                            
print(func(arr))                                         #function call