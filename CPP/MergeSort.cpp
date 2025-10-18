#include <iostream>

using namespace std;

// Function to perform the merge sort
void mergeSort(int arr[], int l, int r)
{
    if (l >= r)
        return; // Base case: If the array has 0 or 1 elements, it is already sorted.

    int m = l + (r - l) / 2; // Calculate the middle index of the array.

    // Recursively sort the left and right halves of the array.
    mergeSort(arr, l, m);
    mergeSort(arr, m + 1, r);

    int i = l, j = m + 1;
    int tmp[r - l + 1], ind = 0;

    // Merge the two sorted subarrays into a single sorted array.
    while (i <= m && j <= r)
    {
        if (arr[i] <= arr[j])
            tmp[ind++] = arr[i++]; // Compare elements from both subarrays and merge them.
        else
            tmp[ind++] = arr[j++];
    }

    // Copy any remaining elements from the left subarray.
    while (i <= m)
    {
        tmp[ind++] = arr[i++];
    }

    // Copy any remaining elements from the right subarray.
    while (j <= r)
    {
        tmp[ind++] = arr[j++];
    }

    // Copy the merged elements back to the original array.
    for (i = l; i <= r; i++)
        arr[i] = tmp[i - l];
}

int main()
{
    int n;
    cout << "Enter value of n : ";
    cin >> n;

    int arr[n];
    cout << "Enter n elements for array : ";
    for (int i = 0; i < n; i++)
        cin >> arr[i];

    mergeSort(arr, 0, n - 1); // Call the mergeSort function to sort the array.

    cout << "Sorted elements are - \n[";
    for (int i = 0; i < n; i++)
        cout << arr[i] << ","[i == n - 1];
    cout << "]\n";

    return 0;
}
