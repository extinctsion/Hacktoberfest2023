public class Triplet Sum in Array {
    //Function to find if there exists a triplet in the 
    //array A[] which sums up to X.
    public static boolean find3Numbers(int A[], int n, int X) { 
    
       // Your code Here
       Arrays.sort(A); // Sort the array in ascending order

        // Fix the first element and find the other two elements
        for (int i = 0; i < n - 2; i++) {
            int left = i + 1; // Pointer for the second element
            int right = n - 1; // Pointer for the third element

            while (left < right) {
                int sum = A[i] + A[left] + A[right];

                if (sum == X) {
                    return true; // Triplet found
                } else if (sum < X) {
                    left++; // Increment the left pointer
                } else {
                    right--; // Decrement the right pointer
                }
            }
        }

        return false; // Triplet not found
    
    }
}