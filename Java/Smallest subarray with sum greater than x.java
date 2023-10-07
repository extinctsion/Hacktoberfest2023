public class Smallest subarray with sum greater than x {
    public static int smallestSubWithSum(int a[], int n, int x) {
        // Your code goes here 
          int minLength = n + 1; // Initialize the minimum length to a value greater than the array size
        int currentSum = 0;
        int start = 0;
        int end = 0;

        while (end < n) {
            // Keep adding elements to the current sum until it becomes greater than x
            while (currentSum <= x && end < n) {
                if (currentSum <= 0 && x > 0) {
                    // Reset the start index and current sum if the current sum becomes non-positive
                    start = end;
                    currentSum = 0;
                }
                currentSum += a[end];
                end++;
            }

            // Update the minimum length if the current subarray length is smaller
            while (currentSum > x && start < n) {
                if (end - start < minLength) {
                    minLength = end - start;
                }
                currentSum -= a[start];
                start++;
            }
        }

        // If minLength is still greater than n, no subarray was found
        if (minLength > n) {
            return 0;
        }

        return minLength;
    }
}
