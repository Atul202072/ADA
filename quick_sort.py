# def quick_sort(arr,low,high):
#     if (low<high):
#         pi=partition(arr,low,high)

#         quick_sort(arr,low,pi-1)
#         quick_sort(arr,pi+1,high)

# def partition(arr,low,high):
#     pivot = arr[high]
#     i=low-1
#     for j in range(low,high):
#         if(arr[j]<=pivot):
#             i+=1
#             arr[i],arr[j]=arr[j],arr[i]

#     arr[i+1],arr[high]=arr[high],arr[i+1]

#     return i+1

# a=[10,20,21,17,82,22]
# quick_sort(a,0,len(a)-1)
# print(a)































# def quick_sort(arr,low,high):
#     if low<high:
#         partition_point=partition(arr,low,high)

#         quick_sort(arr,low,partition_point-1)
#         quick_sort(arr,partition_point+1,high)

# def partition(arr,low,high):
#     pivot=arr[high]
#     i=low-1

#     for j in range (low,high):
#         if arr[j]<=pivot:
#             i+=1
#             arr[i],arr[j]=arr[j],arr[i]
#     arr[i+1],arr[high]=arr[high],arr[i+1]    
#     return i+1

# a=[10,20,21,17,82,22]
# quick_sort(a,0,len(a)-1)
# print(a)


def quick_sort(arr,low,high):
    if low<high:
        pi=partition(arr,low,high)
        
        quick_sort(arr,low,pi-1)
        quick_sort(arr,pi+1,high)
        
def partition(arr,low,high):
    pivot=arr[high]
    i=low-1
    
    for j in range(low,high):
        if arr[j]<=pivot:
            i+=1
            arr[i],arr[j]=arr[j],arr[i]
    arr[i+1],arr[high]=arr[high],arr[i+1]
    return i+1
    
arr=[10,50,60,80,40,20,30,90,70]
quick_sort(arr,0,len(arr)-1)
print(arr)

