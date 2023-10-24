import java.util.ArrayList;
import java.util.List;

import javax.swing.plaf.nimbus.State;

public class Alternatepositiveandnegativenumbers {
    void rearrange(int arr[], int n) {
        // code here
       ArrayList<Integer> pos = new ArrayList<>();
ArrayList<Integer> neg = new ArrayList<>();

// Separate positive and negative integers into different ArrayLists
for (int i = 0; i < n; i++) {
    if (arr[i] >= 0) {
        pos.add(arr[i]); // Add positive integers to 'pos'
    } else {
        neg.add(arr[i]); // Add negative integers to 'neg'
    }
}

int i = 0, j = 0, k = 0;

// Merge positive and negative integers back into the original array
while (i < pos.size() && j < neg.size()) {
    arr[k++] = pos.get(i++); // Add positive integer at 'i' to 'arr' and increment both 'i' and 'k'
    arr[k++] = neg.get(j++); // Add negative integer at 'j' to 'arr' and increment both 'j' and 'k'
}

// If there are any remaining positive integers, add them to 'arr'
while (i < pos.size()) {
    arr[k++] = pos.get(i++); // Add positive integer at 'i' to 'arr' and increment both 'i' and 'k'
}

// If there are any remaining negative integers, add them to 'arr'
while (j < neg.size()) {
    arr[k++] = neg.get(j++); // Add negative integer at 'j' to 'arr' and increment both 'j' and 'k'
}

        
    }
    
}




// Second Approach
public class Solution {
public List<Integer> reArrangeArray(int[] arr){

        int n = arr.length;
        List<Integer> ans = new ArrayList<>();
        List<Integer> neg = new ArrayList<>();
        List<Integer> pos = new ArrayList();
        for(int num : arr){
            if(num > 0){
                pos.add(num);
            }
            else if(num < 0){
                neg.add(num);
            }
        }
          while (i < neg.size() && i < pos.size()) {
            ans.add(pos.get(i));
            ans.add(neg.get(i));
            i++;
        }

        // Add any remaining positive numbers (if any)
        while (i < pos.size()) {
            ans.add(pos.get(i));
            i++;
        }

        // Add any remaining negative numbers (if any)
        while (i < neg.size()) {
            ans.add(neg.get(i));
            i++;
        }

        return ans;
    }


    //
    public static void main(String[] args){
        int[] arr = {1, 2, 3, -4, -1, 4};
        int n = arr.length;
        rearrange(arr, n);
        System.out.println(Arrays.toString(arr));
    }
}
