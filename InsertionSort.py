def input_array(size):
    arr = []
    print(f"Enter {size} values for the array:")
    for _ in range(size):
        try:
            element = int(input())
            arr.append(element)
        except ValueError:
            print("Invalid input. Please enter integers.")
            return None
    return arr

def display_array(arr):
    if arr:
        print("Array values:", end=" ")
        for element in arr:
            print(element, end=" ")
        print()
    else:
        print("Array is empty.")

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

def main():
    try:
        size = int(input("Enter the size of the array: "))
        if size <= 0:
            print("Invalid input. Please enter a positive integer for the size of the array.")
            return

        arr = input_array(size)
        if arr:
            insertion_sort(arr)
            display_array(arr)
    except KeyboardInterrupt:
        print("\nProgram terminated by the user.")

if __name__ == "__main__":
    main()
