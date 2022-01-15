# Python program for implementation of Insertion Sort

# Function to do insertion sort
def insertionSort(arr):

	# Traverse through 1 to len(arr)
	for i in range(1, len(arr)):

		key = arr[i]

		# Move elements of arr[0..i-1], that are
		# greater than key, to one position ahead
		# of their current position
		j = i-1
		while j >= 0 and key < arr[j] :
				arr[j + 1] = arr[j]
				j -= 1
		arr[j + 1] = key


# Driver code to test above
arr=[]
n=int(input("Enter total number of elemnets in the list"))
for i in range(n):
    a=int(input("enter elemnet"))
    arr.append(a)
insertionSort(arr)

print("sorted array")
for i in range(len(arr)):
	print ("% d" % arr[i])

print("----------------------------------------")
print("Program by Nishit Gautam, 0832CS191114")

