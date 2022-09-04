#function for merge sort 

def merge_sort(arr):                                              #function decleration
    if len(arr) > 1:
        left_arr=arr[:len(arr)//2]                                #dividing the list into half
        right_arr=arr[len(arr)//2:]

        merge_sort(left_arr)                                      #recursion function for splitting array
        merge_sort(right_arr)    
   
        i=j=k=0                                                    #initilising indexes
        while i<len(left_arr) and j<len(right_arr):                # checking conditions for iteration
            if left_arr[i] < right_arr[j]:
                arr[k]=left_arr[i]
                i+=1
            else:
                arr[k]=right_arr[j]
                j+=1
            k+=1
            
        while i<len(left_arr):                                     # loop for first half of list items remain, if any
            arr[k]=left_arr[i]
            i+=1
            k+=1

        while j<len(right_arr):                                    # loop for another half of list items remain, if any
            arr[k]=right_arr[j]
            j+=1
            k+=1        

#my_arr=[2,5,7,4,8,33,55,1,0]                                       predefined values for list

# num=int(input("Enter number of element needed: "))
# list=(int(input("")) for x in range(num))
# print(list)

my_arr=[]
my_arr=[int(x) for x in input("Elements: ").split()]
print(my_arr)
 
merge_sort(my_arr)
print(my_arr)  
 
  
