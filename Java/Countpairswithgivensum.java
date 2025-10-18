import java.util.HashMap;

public class Countpairswithgivensum {
    int getPairsCount(int[] arr, int n, int k) {
        // code here
        HashMap<Integer, Integer> freqMap = new HashMap<>();  // HashMap to store element frequencies
        int count = 0;  // Count of pairs

        // Traverse the array and populate the frequency map
        for (int num : arr) {
            // Increment the frequency of the current element
            freqMap.put(num, freqMap.getOrDefault(num, 0) + 1);
        }

        // Traverse the array again to find pairs
        for (int num : arr) {
            int complement = k - num;  // Calculate the complement of the current element

            // Check if the complement exists in the frequency map
            if (freqMap.containsKey(complement)) {
                count += freqMap.get(complement);  // Add the frequency of the complement to the count

                // If the current element is the same as the complement, decrement the count
                if (num == complement) {
                    count--;
                }
            }
        }

        return count / 2;  // Divide the count by 2 since each pair is counted twice
    }

    public static void main(String[] args) {
        int[] arr = {1, 5, 7, 1};
        int n = arr.length;
        int k = 6;
        Countpairswithgivensum obj = new Countpairswithgivensum();
        System.out.println(obj.getPairsCount(arr, n, k));
    }
}
