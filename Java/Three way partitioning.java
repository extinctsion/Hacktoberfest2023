public class Three way partitioning {
    public void threeWayPartition(int array[], int a, int b)
    {
        // code here 
        int n = array.length;
        int start = 0;
        int end = n - 1;

        // Move all elements smaller than 'a' to the beginning
        for (int i = 0; i <= end; ) {
            if (array[i] < a) {
                swap(array, i, start);
                i++;
                start++;
            } else if (array[i] > b) {
                // Move all elements greater than 'b' to the end
                swap(array, i, end);
                end--;
            } else {
                // Elements in the range [a, b] are already in the correct position
                i++;
            }
        }
    }
    
    private void swap(int[] array, int i, int j) {
        int temp = array[i];
        array[i] = array[j];
        array[j] = temp;
    }
}
