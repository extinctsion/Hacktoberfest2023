def input_array(N):
    try:
        arr = []
        print(f"Enter values of {N} array:")
        for i in range(N):
            arr.append(int(input()))
        return arr
    except ValueError:
        print("Invalid input. Please enter integers.")
        exit(1)

def display_array(arr):
    print("Values of the array are:", end=" ")
    for element in arr:
        print(element, end=" ")
    print()

def sort_array(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

def main():
    try:
        size = int(input("Enter the size of the array: "))
        if size <= 0:
            print("Invalid input. Please enter a positive integer for the size of the array.")
            exit(1)

        arr = input_array(size)
        sort_array(arr)
        display_array(arr)
    except KeyboardInterrupt:
        print("\nProgram terminated by user.")
        exit(1)

if __name__ == "__main__":
    main()
