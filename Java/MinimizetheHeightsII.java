import java.util.Arrays;

public class MinimizetheHeightsII{
    int getMinDiff(int[] arr, int n, int k) {
        // code here
        // base case
        if(n==1)
            return 0;
        
        // Sort the array in non-decreasing order
        Arrays.sort(arr);
        
        // Calculate the initial difference
        int min_diff = arr[n-1] - arr[0];
        
        // Initialize min_height and max_height
        int max_height = 0;
        int min_height = 0;
        
        // Iterate through the array
        for (int i = 1; i < n; i++) {
            if(arr[i]-k<0)
                continue;
            int new_max_height = Math.max(arr[n-1] - k, arr[i-1] + k);
            int new_min_height = Math.min(arr[0] + k, arr[i] - k);
            int new_diff = new_max_height - new_min_height;
            
            min_diff = Math.min(min_diff, new_diff);
        }
        
        return min_diff;
    }

    public static void main(String[] args)
    {
        int[] arr = {1, 5, 8, 10};
        int n = arr.length;
        int k = 2;
        MinimizetheHeightsII obj = new MinimizetheHeightsII();
        System.out.println(obj.getMinDiff(arr, n, k));
    }
    
}