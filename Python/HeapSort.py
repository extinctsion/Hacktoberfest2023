def parent(i):
    return i // 2

def left(i):
    return 2 * i

def right(i):
    return 2 * i + 1

def max_heapify(A, i, heap_size):
    p = left(i)
    q = right(i)
    largest = i
    if p <= heap_size and A[p - 1] > A[i - 1]:
        largest = p
    if q <= heap_size and A[q - 1] > A[largest - 1]:
        largest = q
    if largest != i:
        A[i - 1], A[largest - 1] = A[largest - 1], A[i - 1]
        max_heapify(A, largest, heap_size)

def min_heapify(A, i, heap_size):
    p = left(i)
    q = right(i)
    smallest = i
    if p <= heap_size and A[p - 1] < A[i - 1]:
        smallest = p
    if q <= heap_size and A[q - 1] < A[smallest - 1]:
        smallest = q
    if smallest != i:
        A[i - 1], A[smallest - 1] = A[smallest - 1], A[i - 1]
        min_heapify(A, smallest, heap_size)

def build_min_heap(A, n):
    heap_size = n
    for i in range(n // 2, 0, -1):
        min_heapify(A, i, heap_size)

def build_max_heap(A, n):
    heap_size = n
    for i in range(n // 2, 0, -1):
        max_heapify(A, i, heap_size)

def heap_sort_max(A, n, heap_size):
    build_max_heap(A, n)
    for i in range(n - 1, 0, -1):
        A[0], A[i] = A[i], A[0]
        heap_size -= 1
        max_heapify(A, 1, heap_size)

def heap_sort_min(A, n, heap_size):
    build_min_heap(A, n)
    for i in range(n - 1, 0, -1):
        A[0], A[i] = A[i], A[0]
        heap_size -= 1
        min_heapify(A, 1, heap_size)

def heap_maximum(A, heap_size):
    heap_sort_max(A, len(A), heap_size)
    return A[heap_size - 1]

def heap_increase_key(A, i, key):
    if key < A[i]:
        print("New key is smaller than the current key")
        return
    A[i] = key
    while i > 0 and A[parent(i)] < A[i]:
        A[i], A[parent(i)] = A[parent(i)], A[i]
        i = parent(i)

if __name__ == "__main__":
    n = int(input("Enter size: "))
    B = [int(input(f"Enter element A[{i}]: ")) for i in range(n)]

    while True:
        a = int(input("Select action: \n1) Sort in ascending order\n2) Sort in descending order\n3) Find maximum element\n4) Delete maximum element\n5) Increase element\n6) Insert new element\n7) Exit\n"))

        if a == 1:
            print("Heap Sort in ascending order: ")
            heap_sort_max(B, n, n)
            print(B)
        elif a == 2:
            print("Heap Sort in descending order: ")
            heap_sort_min(B, n, n)
            print(B)
        elif a == 3:
            m = heap_maximum(B, n)
            print(f"MAX: {m}")
        elif a == 4:
            max_val = heap_maximum(B, n)
            if max_val in B:
                B.remove(max_val)
                n -= 1
                print(f"Deleted {max_val}")
        elif a == 5:
            y = int(input("Enter index to increase element: "))
            x = int(input("Enter number to change to: "))
            if 0 <= y < n:  # Check if the index is within the valid range of the list
                heap_increase_key(B, y, x)
        elif a == 6:
            x = int(input("Enter number to insert: "))
            B.append(x)
            n += 1
        elif a == 7:
            break
        else:
            print("Invalid option")

    print("\n")