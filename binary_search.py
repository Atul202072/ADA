# Binary Search in Python

def binary_search(list, key):   #defining a function
    low = 0
    high = len(list) - 1
    mid = 0
    while low <= high:              # Repeat until the pointers low and high meet each other
        mid = (high + low) // 2
        if list[mid] < key:         # Check If key is present at mid
          low = mid + 1
        elif list[mid] > key:       # If key is greater, compare to right of mid
           high = mid + 1
        else:                       # If key is smaller, compare to left of mid
           return mid
    return 1

list = [121,135,168,243,220,154,144,232,440]          #creting a list
key = 220
result = binary_search(list, key)                     #function call
if result != 1:
    print("The required key is present in the list at position:", str(result+1))
else:
    print("The required key is not present in the list")
