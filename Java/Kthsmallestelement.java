public class Kthsmallestelement {

    public static int kthSmallest(int[] arr, int l, int r, int k) {
        // Your code here
        
        //Using Quick Sort
        int pivot = arr[r]; 
        int i = l-1;
        for(int j=l;j<r;j++){
            if(arr[j]<pivot){
                i++;
                int temp = arr[i];  
                arr[i]=arr[j];
                arr[j]=temp;
            }
        }
        int temp = arr[i+1];
        arr[i+1]=arr[r];
        arr[r]=temp;

        if(i+1==k-1){
            return arr[i+1];
        }
        else if(i+1>k-1){
            return kthSmallest(arr,l,i,k);
        }
        else{
            return kthSmallest(arr,i+2,r,k);
        }
    }  
}



//Kth smallest element

// arr : given array
// l : starting index of the array i.e 0
// r : ending index of the array i.e size-1
// k : find kth smallest element and return using this function

// Quick Sort Solution
// Code Explanation
// We are using Quick Sort to sort the array and then returning the kth element from the sorted array.
// The idea is to find the pivot element and place it at its correct position in the sorted array
// and then check if the pivot element is at the kth position or not.
// If the pivot element is at the kth position then we return the pivot element.
// If the pivot element is not at the kth position then we check if the pivot element is greater than kth position or not.
// If the pivot element is greater than kth position then we recursively call the function for the left subarray.
// If the pivot element is smaller than kth position then we recursively call the function for the right subarray.
// The time complexity of this solution is O(n^2) in the worst case and O(n) in the best case.
// The space complexity of this solution is O(1).


// Simple Solution
// class Solution {
//     public int kthSmallest(int[] arr, int l, int r, int k) {
//         // Your code here
//         Arrays.sort(arr);
//         return arr[k-1];
//     }
// }