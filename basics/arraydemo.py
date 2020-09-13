# Inserting element in array
# Searching for element in array
from array import *

arr = array('i', [])
n = int(input("Enter the length of the array:"))
for i in range(n):
    x = int(input("Enter a number:"))
    arr.append(x)

print(arr)

val = int(input("Enter a number for search:"))
k = 0
for e in arr:
    if e == val:
        print("Element found at index:", k)
        break
    k += 1

#using function
print("Found element using function:", arr.index(val))
