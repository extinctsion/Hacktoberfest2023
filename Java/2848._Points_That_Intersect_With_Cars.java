//https://leetcode.com/problems/points-that-intersect-with-cars/description/

class Solution {
    public int numberOfPoints(List<List<Integer>> nums) {

        int count = 0 ;
        int n = nums.size();
        Set<Integer> set = new HashSet<>();

        for(List<Integer> temp : nums){
            
            int s = temp.get(0);
            int e = temp.get(1);

            for(int i = s ; i<=e ; i++){
                set.add(i);
            }
        }
        return set.size();
    }
} 
