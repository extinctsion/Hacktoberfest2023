#include <iostream>

int findMissingElement(int arr[], int N) {
    // Calculate the sum of all integers from 1 to N
    int totalSum = (N * (N + 1)) / 2;

    // Calculate the sum of elements in the array
    int arrSum = 0;
    for (int i = 0; i < N - 1; i++) {
        arrSum += arr[i];
    }

    // The missing element is the difference between the total sum and the array sum
    int missingElement = totalSum - arrSum;

    return missingElement;
}

int main() {
    int N;
    std::cout << "Enter the size of the array (N-1): ";
    std::cin >> N;

    int arr[N - 1];
    std::cout << "Enter " << N - 1 << " distinct integers in the range of 1 to " << N << ": ";
    for (int i = 0; i < N - 1; i++) {
        std::cin >> arr[i];
    }

    int missingElement = findMissingElement(arr, N);
    std::cout << "The missing element is: " << missingElement << std::endl;

    return 0;
}
