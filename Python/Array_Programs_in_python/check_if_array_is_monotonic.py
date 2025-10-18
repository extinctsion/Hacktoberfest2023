def isMonotonic(arr):
	if len(arr) <= 2:
		return True
	direction = arr[1] - arr[0]
	for i in range(2, len(arr)):
		if direction == 0:
			direction = arr[i] - arr[i - 1]
			continue
		if (direction > 0 and arr[i] < arr[i - 1]) or (direction < 0 and arr[i] > arr[i - 1]):
			return False
	return True

# Example usage
arr1 = [1, 2, 3, 4, 5] # True
arr2 = [5, 4, 3, 2, 1] # True
arr3 = [1, 2, 2, 3, 4] # True
arr4 = [1, 2, 3, 4, 5, 4] # False

print(isMonotonic(arr1)) # should return True
print(isMonotonic(arr2)) # should return True
print(isMonotonic(arr3)) # should return True
print(isMonotonic(arr4)) # should return False
