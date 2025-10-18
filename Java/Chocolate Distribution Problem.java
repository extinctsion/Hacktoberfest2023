public class Chocolate Distribution Problem {
    public long findMinDiff (ArrayList<Integer> a, int n, int m)
    {
        // your code here
        // Sort the array in ascending order
        Collections.sort(a);

        int start = 0;
        int end = m - 1; //m - 1 which is equivalent to n - 1 because there are always at least two elements in an ArrayList<Integer>  
        long minDifference = Long.MAX_VALUE;

        // Iterate through the array
        while (end < n) {
            long difference = a.get(end) - a.get(start);

            // Update minDifference if the current difference is smaller
            if (difference < minDifference) {
                minDifference = difference;
            }

            // Move the window
            start++;
            end++;
        }

        return minDifference;
    }
}
