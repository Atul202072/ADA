def selection_Sort(arr):
    for i in range(0,len(arr)-1):
        current_pointer=i
        for j in range(i+1,len(arr)):
            if arr[j]<arr[current_pointer]:
                current_pointer=j

        arr[i],arr[current_pointer]=arr[current_pointer],arr[i]

a=[10 ,50, 60, 80, 40, 30, 90, 10 ]
selection_Sort(a)
print(a)                
