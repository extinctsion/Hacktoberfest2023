import java.util.HashSet;

public class Subarraywith0sum {
    static boolean findsum(int arr[],int n)
    {
        //Your code here
        HashSet<Integer> hash = new HashSet<>();
        int sum = 0;
        for (int i = 0; i < n; i++) {
            sum += arr[i];
            if (sum == 0)                   
                return true;
            if (hash.contains(sum))         
                return true;
            
            hash.add(sum);
        }
        
        return false;
    }


    public static void main(String[] args) {
        int[] arr = {4, 2, -3, 1, 6};
        int n = arr.length;
        System.out.println(findsum(arr, n));
    }
}


// explanation

// The idea is to iterate through the array and for every element arr[i], 
//calculate sum of elements form 0 to i (this can simply be done as sum += arr[i]).
// If the current sum has been seen before, then there is a zero-sum array. 
//Hashing is used to store the sum values, 
//so that we can quickly store sum and find out whether the current sum is seen before or not.
// Time Complexity: O(n) in average case.