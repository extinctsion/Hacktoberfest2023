import java.util.Arrays;
//Does not work for long arrays
public class Sortanarrayof012 {
    public static void sort012(int arr[], int n)
    {
        // code here 
        int low=0;
        int mid=0;
        int high=n-1;
        while(mid<=high){
            if(arr[mid]==0){
                int temp = arr[low];
                arr[low]=arr[mid];
                arr[mid]=temp;
                low++;
                mid++;
            }
            else if(arr[mid]==1){
                mid++;
            }
            else{
                int temp = arr[high];
                arr[high]=arr[mid];
                arr[mid]=temp;
                high--;
            }
        }
    }
    
    public static void main(String[] args) {
        int[] arr = {0,2,1,2,0};
        sort012(arr, arr.length);
        System.out.println(Arrays.toString(arr));
    }
}

// Code Explanation
// We are using Dutch National Flag Algorithm to sort the array.
// We are using three pointers low, mid and high.
// The low pointer points to the index where we have to place the next 0.
// The mid pointer points to the index where we have to place the next 1.
// The high pointer points to the index where we have to place the next 2.
// We are iterating the array from left to right.
// If the mid pointer is pointing to 0 then we swap the elements at low and mid and increment both low and mid.
// If the mid pointer is pointing to 1 then we increment the mid pointer.
// If the mid pointer is pointing to 2 then we swap the elements at mid and high and decrement the high pointer.
// The time complexity of this solution is O(n).
// The space complexity of this solution is O(1).




// Simple Solution Trick
// class Solution
// {
//     public static void sort012(int a[], int n)
//     {
//         // code here
//         Arrays.sort(arr);
//     }
// }
