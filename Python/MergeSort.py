import sys

def merge(A, p, q, r):
    n1 = q - p + 1
    n2 = r - q
    L = [0] * (n1 + 1)
    R = [0] * (n2 + 1)

    for i in range(n1):
        L[i] = A[p + i - 1]

    for j in range(n2):
        R[j] = A[q + j]

    L[n1] = sys.maxsize
    R[n2] = sys.maxsize
    i = 0
    j = 0

    for k in range(p - 1, r):
        if L[i] <= R[j]:
            A[k] = L[i]
            i += 1
        else:
            A[k] = R[j]
            j += 1

def merge_sort(A, p, r):
    if p < r:
        q = (p + r) // 2
        merge_sort(A, p, q)
        merge_sort(A, q + 1, r)
        merge(A, p, q, r)

if __name__ == "__main__":
    n = int(input("Enter the size of the array: "))
    B = [0] * n

    print("Enter the elements of the array:")
    for i in range(n):
        B[i] = int(input(f"B[{i}] = "))

    merge_sort(B, 1, n)

    print("Sorted Array:")
    for i in range(n):
        print(B[i], end=" ")

    print()
