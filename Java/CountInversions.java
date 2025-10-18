public class CountInversions {
    // arr[]: Input Array
    // N : Size of the Array arr[]
    //Function to count inversions in the array.
    static long inversionCount(long arr[], long N)
    {
        // Your Code Here
        return mergeSortAndCount(arr, 0, N - 1);
    }
    static long mergeSortAndCount(long arr[], long l, long r) {
        long count = 0;

        if (l < r) {
            long m = (l + r) / 2;

            // Count inversions in the left subarray
            count += mergeSortAndCount(arr, l, m);

            // Count inversions in the right subarray
            count += mergeSortAndCount(arr, m + 1, r);

            // Merge the two sorted subarrays and count inversions
            count += mergeAndCount(arr, l, m, r);
        }

        return count;
    }

    static long mergeAndCount(long arr[], long l, long m, long r) {
        long[] left = new long[(int) (m - l + 1)];
        long[] right = new long[(int) (r - m)];

        // Copy elements to the left subarray
        for (int i = 0; i < left.length; i++) {
            left[i] = arr[(int) (l + i)];
        }

        // Copy elements to the right subarray
        for (int i = 0; i < right.length; i++) {
            right[i] = arr[(int) (m + 1 + i)];
        }

        long count = 0;
        int i = 0, j = 0, k = (int) l;

        // Merge the left and right subarrays and count inversions
        while (i < left.length && j < right.length) {
            if (left[i] <= right[j]) {
                arr[k++] = left[i++];
            } else {
                arr[k++] = right[j++];
                count += (m - l + 1) - i;
            }
        }

        // Copy the remaining elements from the left subarray
        while (i < left.length) {
            arr[k++] = left[i++];
        }

        // Copy the remaining elements from the right subarray
        while (j < right.length) {
            arr[k++] = right[j++];
        }

        return count;
    }
    

    public static void main(String[] args) {
        long[] arr = {2, 4, 1, 3, 5};
        long N = arr.length;
        System.out.println(inversionCount(arr, N));
    }
}
