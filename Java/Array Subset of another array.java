public class Array Subset of another array{
    public String isSubset( long a1[], long a2[], long n, long m) {
        // Sort both arrays if they are unsorted
        Arrays.sort(a1);
        Arrays.sort(a2);

        int i = 0, j = 0;

        while (i < n && j < m) {
            // If the current elements are equal, move both pointers
            if (a1[i] == a2[j]) {
                i++;
                j++;
            }
            // If a1[i] is smaller, move the pointer for a1[]
            else if (a1[i] < a2[j]) {
                i++;
            }
            // If a1[i] is greater, a2[] is not a subset of a1[]
            else {
                return "No";
            }
        }

        // If all elements of a2[] are processed, it is a subset
        if (j == m) {
            return "Yes";
        }

        return "No";
        
    }
}