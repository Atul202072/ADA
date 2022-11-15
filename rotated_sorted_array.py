def Rst(arr,key):
    low=0
    high=len(arr)-1
    while low<=high:
        mid=(low+high)//2
        if arr[mid]==key:
            return mid
        elif arr[low]<=arr[mid]:
            if key >=arr[low] and key <arr[mid]:
                high=mid-1
            else:
                low=mid+1
        else:
            if key>arr[mid] and key<=arr[high]:
                low=mid+1
            else:
                high=mid-1
    #return 1

arr=[5,6,7,1,2,3,4]
key=6
print(Rst(arr,key))
# result=Rst(arr,key)
# if result!=1:
#     print("The index of",key,"in the array is:",result)
# else:
#     print("Out of range value!")

