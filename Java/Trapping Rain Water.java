public class Trapping Rain Water {
    // arr: input array
    // n: size of array
    // Function to find the trapped water between the blocks.
    static long trappingWater(int arr[], int n) { 
        // Your code here
        int[] leftMax = new int[n]; // Array to store the maximum height on the left side of each block
        int[] rightMax = new int[n]; // Array to store the maximum height on the right side of each block

        leftMax[0] = arr[0]; // The first block has no left side, so its maximum height is itself
        rightMax[n - 1] = arr[n - 1]; // The last block has no right side, so its maximum height is itself

        // Compute the maximum height on the left side of each block
        for (int i = 1; i < n; i++) {
            leftMax[i] = Math.max(leftMax[i - 1], arr[i]);
        }

        // Compute the maximum height on the right side of each block
        for (int i = n - 2; i >= 0; i--) {
            rightMax[i] = Math.max(rightMax[i + 1], arr[i]);
        }

        long waterTrapped = 0; // Variable to store the total trapped water

        // Compute the water trapped between the blocks
        for (int i = 0; i < n; i++) {
            int minHeight = Math.min(leftMax[i], rightMax[i]); // Find the minimum height on both sides of the current block
            waterTrapped += minHeight - arr[i]; // Compute the difference in height and add it to the total trapped water
        }

        return waterTrapped;
}
