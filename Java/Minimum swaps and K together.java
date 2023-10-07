public class Minimum swaps and K together{
       // Function for finding maximum and value pair
    public static int minSwap (int arr[], int n, int k) {
        //Complete the function
         int count = 0; // Count of elements less than or equal to k
        for (int i = 0; i < n; i++) {
            if (arr[i] <= k) {
                count++;
            }
        }

        // Find the count of elements greater than k in the first window of size 'count'
        int greaterCount = 0;
        for (int i = 0; i < count; i++) {
            if (arr[i] > k) {
                greaterCount++;
            }
        }

        int minSwaps = greaterCount;
        for (int i = 0, j = count; j < n; i++, j++) {
            if (arr[i] > k) {
                greaterCount--;
            }
            if (arr[j] > k) {
                greaterCount++;
            }
            minSwaps = Math.min(minSwaps, greaterCount);
        }

        return minSwaps;
    }
}