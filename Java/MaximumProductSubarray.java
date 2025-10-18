public class MaximumProductSubarray {
    long maxProduct(int[] arr, int n) {
        // code here
        // Initialize variables to track the maximum and minimum product ending at the current index
        long max = arr[0], min = arr[0], ans = arr[0];
        for(int i=1; i<n; i++)
        {
            // If the current element is negative, swap the maximum and minimum product
            if(arr[i]<0)
            {
                long t = max;
                max = min;
                min = t;
            }
            // Update the maximum and minimum product at the current index
            max = Math.max(arr[i] , arr[i]*max);
            min = Math.min(arr[i] , arr[i]*min);
            // Update the maximum result
            ans = Math.max(ans, max);
        }
        return ans;
    }

    public static void main(String[] args) {
        MaximumProductSubarray obj = new MaximumProductSubarray();
        int[] arr = {6, -3, -10, 0, 2};
        int n = arr.length;
        System.out.println(obj.maxProduct(arr, n));
    }
}
