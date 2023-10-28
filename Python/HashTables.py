M = 6  # Define the size of the hash table
n = 6  # Define the number of elements to be used

class Node:
    def __init__(self):
        self.data = 0
        self.s = "NIL"
        self.next = None
        self.previous = None

# Hash function to calculate the position in the hash table
def HashFunction(k, i):
    a = k % M
    return a

# Function to insert an element into the hash table using open addressing
def HashInsert(T, k):
    i = 0
    while i != M:
        j = HashFunction(k, i)
        if T[j].s == "NIL" or T[j].s == "DEL":
            T[j].data = k
            T[j].s = "FIL"
            return
        elif T[j].s == "FIL":
            while T[j].s == "FIL":
                j += 1
            T[j].data = k
            T[j].s = "FIL"
            return
        i += 1
    if i == M:
        print("Hash table is full")
    return

# Function to search for an element in the hash table using open addressing
def HashSearch(T, k):
    i = 0
    while i != M:
        for y in range(M):
            if T[y].data == k and T[y].s == "FIL":
                return y
        i += 1
    return i

# Function to delete an element from the hash table using open addressing
def HashDelete(T, k):
    i = HashSearch(T, k)
    if i != M:
        T[i].s = "DEL"
    else:
        print("Element not found")
    return

# Function to perform hashing using separate chaining
def ChainedHashMassive(T, A):
    arr = [None] * M

    for m in range(n):
        j = HashFunction(A[m], 0)
        if arr[j] is None:
            arr[j] = []
        arr[j].append(A[m])

    for i in range(M):
        print(i, end=": ")
        if arr[i] is not None:
            for element in arr[i]:
                print(element, end=" ")
        print()

# Function to search for an element in the hash table using separate chaining
def ChainedHashSearch(T, k, A):
    arr = [None] * M

    i = 0
    while i != M:
        for m in range(n):
            j = HashFunction(A[m], i)
            if arr[j] is None:
                arr[j] = []
            arr[j].append(A[m])
        for y in range(M):
            if arr[y] is not None:
                for val in arr[y]:
                    if val == k:
                        return y
        i += 1

    return i

# Function to delete an element from the hash table using separate chaining
def ChainedHashDelete(T, k, A):
    n = 6
    pos = 0
    for m in range(n):
        if A[m] == k:
            pos = m

    for i in range(pos, n - 1):
        A[i] = A[i + 1]
    n -= 1

# Initialize the hash table
T = [Node() for _ in range(M)]
A = [0] * n

while True:
    print("\nChoose an action:")
    choice = int(input("1. Hashing with open addressing\n2. Chained hashing\n3. Exit\n"))

    if choice == 1:
        ch = int(input("\n1. Insert\n2. Delete\n3. Show table\n4. Search\n5. Exit\n"))
        if ch == 1:
            a = int(input("Enter element to insert: "))
            HashInsert(T, a)
        elif ch == 2:
            a = int(input("Enter element to delete: "))
            HashDelete(T, a)
        elif ch == 3:
            for i in range(M):
                print(T[i].s, end=" ")
                if T[i].s == "FIL":
                    print(T[i].data, end=" ")
                print()
        elif ch == 4:
            a = int(input("Enter element to search: "))
            i = HashSearch(T, a)
            print(f"Element {a} is in the table at position {i}")
        elif ch == 5:
            break

    elif choice == 2:
        vybir = int(input("\n1. Insert\n2. Delete\n3. Search\n4. Exit\n"))
        if vybir == 1:
            print("Enter elements to insert (6): ")
            for i in range(n):
                A[i] = int(input())
            ChainedHashMassive(T, A)
        elif vybir == 2:
            a = int(input("Enter element to delete: "))
            ChainedHashDelete(T, a, A)
            n -= 1
            ChainedHashMassive(T, A)
        elif vybir == 3:
            a = int(input("Enter element to search: "))
            i = ChainedHashSearch(T, a, A)
            print(f"Element {a} is in the table at position {i}")
        elif vybir == 4:
            break

    elif choice == 3:
        break
