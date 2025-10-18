import java.util.ArrayList;

public class Commonelements {
    ArrayList<Integer> commonElements(int A[], int B[], int C[], int n1, int n2, int n3) 
    {
        // code here
        ArrayList<Integer> result = new ArrayList<>();  // To store the common elements

        // Initialize three pointers for each array
        int i = 0, j = 0, k = 0;

        // Iterate until any of the pointers reaches the end of its respective array
        while (i < n1 && j < n2 && k < n3) {
            // If the current elements in all three arrays are the same
            if (A[i] == B[j] && B[j] == C[k]) {
                // Add the common element to the result list
                if (result.isEmpty() || result.get(result.size() - 1) != A[i]) {
                    result.add(A[i]);
                }
                // Move all three pointers to the next element
                i++;
                j++;
                k++;
            }
            // If the current element in array A is smaller, move its pointer to the next element
            else if (A[i] < B[j]) {
                i++;
            }
            // If the current element in array B is smaller, move its pointer to the next element
            else if (B[j] < C[k]) {
                j++;
            }
            // If the current element in array C is smaller, move its pointer to the next element
            else {
                k++;
            }
        }

        return result;
    }

    public ArrayList<Integer> findCommonElements(int[] A, int[] B, int[] C) {
    ArrayList<Integer> set = new ArrayList<>();
        int i=0,j=0,k=0;
        while(i<n1 && j<n2 && k<n3){
            if(A[i]==B[j] && B[j]==C[k]){
                if(!set.contains(A[i])){
                    set.add(A[i]);
                }
                
                i++;j++;k++;
            }
            else if(A[i]<B[j]) i++;
            else if(B[j]<C[k]) j++;
            else k++;
            
        }
        return set;
    }

    public static void main(String[] args) {
        int[] A = {1, 5, 10, 20, 40, 80};
        int[] B = {6, 7, 20, 80, 100};
        int[] C = {3, 4, 15, 20, 30, 70, 80, 120};
        int n1 = A.length;
        int n2 = B.length;
        int n3 = C.length;
        Commonelements obj = new Commonelements();
        ArrayList<Integer> result = obj.commonElements(A, B, C, n1, n2, n3);
        System.out.println(result);
    }



}