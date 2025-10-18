import java.util.HashSet;

public class Longestconsecutivesubsequence {
    // arr[] : the input array
    // N : size of the array arr[]
    
    //Function to return length of longest subsequence of consecutive integers.
	static int findLongestConseqSubseq(int arr[], int N)
	{
	   // add your code here
	   HashSet<Integer> set = new HashSet<>();
        
        // Adding all elements to the set
        for (int i = 0; i < N; i++) {
            set.add(arr[i]);
        }
        
        int maxLen = 0;
        
        // Checking each possible sequence from the start
        for (int i = 0; i < N; i++) {
            // If current element is the starting element of a sequence
            if (!set.contains(arr[i] - 1)) {
                int currNum = arr[i];
                
                // Counting the length of the consecutive sequence
                while (set.contains(currNum)) {
                    currNum++;
                }
                
                // Updating the maximum length
                maxLen = Math.max(maxLen, currNum - arr[i]);
            }
        }
        
        return maxLen;
	}
}
