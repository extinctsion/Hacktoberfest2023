import java.util.ArrayList;

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





class Solution {
public:
    vector<int> rearrangeArray(vector<int>& nums) {
        int n = nums.size();
        vector<int> ans, neg, pos;
        for(auto num : nums){
            if(num > 0){
                pos.push_back(num);
            }
            else if(num < 0){
                neg.push_back(num);
            }
        }
        for(int i=0; i<neg.size(); i++){
            ans.push_back(pos[i]);
            ans.push_back(neg[i]);
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
};
