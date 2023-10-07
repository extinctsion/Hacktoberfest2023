public class KadanesAlgorithm {
    // arr: input array
    // n: size of array
    //Function to find the sum of contiguous subarray with maximum sum.
    long maxSubarraySum(int arr[], int n){
        
        // Your code here
            long sum = 0;
            long maxi =  Integer.MIN_VALUE;
            
            for (int i = 0; i<n; i++){
                sum = sum + arr[i];
                maxi = Math.max(maxi,sum);
                if(sum<0){
                    sum = 0;
                }
                
            }
            
            return maxi;
            
        
    }
       
}
