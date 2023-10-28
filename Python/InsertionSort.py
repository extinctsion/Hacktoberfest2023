def insertion_sort(array):
    for i in range(0, len(array)):
        key = array[i]
        j = i - 1
        while(j >= 0 and array[j] > key):
            array[j + 1] = array[j]
            j -= 1
        array[j + 1] = key

def main():
    A = []
    size = int(input("Input size of array: "))

    for i in range(size):
        element = int(input("Input element:"))
        print("A[" + str(i) + "]=" + str(element))
        A.append(element)
    insertion_sort(A)
    print(A)

if __name__ == "__main__":
    main()