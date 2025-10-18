public class MergeSort {

    public static void mergeSort(int[] arr) {
        if (arr == null || arr.length <= 1) {
            return; // No need to sort an empty array or an array with one element.
        }
        
        int middle = arr.length / 2;
        int[] left = new int[middle];
        int[] right = new int[arr.length - middle];

        // Split the array into two halves
        for (int i = 0; i < middle; i++) {
            left[i] = arr[i];
        }
        for (int i = middle; i < arr.length; i++) {
            right[i - middle] = arr[i];
        }

        // Recursively sort the two halves
        mergeSort(left);
        mergeSort(right);

        // Merge the sorted halves back together
        merge(arr, left, right);
    }

    private static void merge(int[] arr, int[] left, int[] right) {
        int i = 0, j = 0, k = 0;

        while (i < left.length && j < right.length) {
            if (left[i] <= right[j]) {
                arr[k++] = left[i++];
            } else {
                arr[k++] = right[j++];
            }
        }

        while (i < left.length) {
            arr[k++] = left[i++];
        }

        while (j < right.length) {
            arr[k++] = right[j++];
        }
    }

    public static void main(String[] args) {
        int[] arr = {12, 11, 13, 5, 6, 7};
        System.out.println("Original array: " + Arrays.toString(arr));
        
        mergeSort(arr);
        
        System.out.println("Sorted array: " + Arrays.toString(arr));
    }
}
