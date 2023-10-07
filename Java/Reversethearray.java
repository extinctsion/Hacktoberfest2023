public class Reversethearray{
    public static void main(String[] args) {
        // Using Swap method
        int[] arr = {1,2,3,4,5};
        int start = 0;
        int end = arr.length-1;
        while(start<end){
            int temp = arr[start];
            arr[start] = arr[end];
            arr[end] = temp;
            start++; 
            end--;
        }
        for(int i=0;i<arr.length;i++){
            System.out.print(arr[i]+" ");
        }
    }
}


// Explanation
// 1. We have taken an array of 5 elements and we have to reverse it.
// 2. We have taken two variables start and end and initialized them with 0 and arr.length-1 respectively.
// 3. We have used a while loop and we have checked if start is less than end.
// 4. If it is true then we have swapped the elements at start and end and incremented start and decremented end.
// 5. We have printed the array after reversing it.
// 6. The time complexity of this program is O(n) and the space complexity is O(1).
