# Python program for implementation of Selection
# Sort
import sys

A=[]
n=int(input("Enter total number of elemnets in the list"))
for i in range(n):
    a=int(input("enter elemnet"))
    A.append(a)

# Traverse through all array elements
for i in range(len(A)):

    # Find the minimum element in remaining
    # unsorted array
    min_idx = i
    for j in range(i + 1, len(A)):
        if A[min_idx] > A[j]:
            min_idx = j

    # Swap the found minimum element with
    # the first element
    A[i], A[min_idx] = A[min_idx], A[i]

# Driver code to test above
print("Sorted array")
for i in range(len(A)):
    print("%d" % A[i]),


print("----------------------------------------")
print("Program by Nishit Gautam, 0832CS191114")