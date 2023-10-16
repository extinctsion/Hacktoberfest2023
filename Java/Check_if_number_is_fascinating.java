/*
You are given an integer n that consists of exactly 3 digits.

We call the number n fascinating if, after the following modification, the resulting number contains all the digits from 1 to 9 exactly once and does not contain any 0's:

Concatenate n with the numbers 2 * n and 3 * n.
Return true if n is fascinating, or false otherwise.

Concatenating two numbers means joining them together. For example, the concatenation of 121 and 371 is 121371.

Example 1:

Input: n = 192
Output: true
Explanation: We concatenate the numbers n = 192 and 2 * n = 384 and 3 * n = 576. The resulting number is 192384576. This number contains all the digits from 1 to 9 exactly once. 
*/

class Solution {
    public boolean isFascinating(int n) {
        String str = String.valueOf(n) + String.valueOf(2*n) + String.valueOf(3*n);
        HashSet<Integer> set = new HashSet<>();
        System.out.println(str);
        for(int i=0;i<str.length();i++){
            int ch = str.charAt(i)-'0';      
            if(ch == 0){   
                return false;
            }else{
                if(set.contains(ch)){
                    return false;
                }else{
                    set.add(ch);
                if(set.size()==9) return true;
                }
            }
            
        }
        return false;
    }
}