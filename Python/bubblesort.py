def bubble_sort(arr):
    n = len(arr)
    for i in range(n - 1):
        # last i elements are already sorted
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                # swap
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr


# Example usage
numbers = [64, 34, 25, 12, 22, 11, 90]
sorted_numbers = bubble_sort(numbers)
print("Sorted list:", sorted_numbers)
