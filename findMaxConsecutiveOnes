class Solution {
public:
    int findMaxConsecutiveOnes(vector<int>& arr) {
        
        // code here
        
        int n = arr.size();
        int maxCount = 0, count = 0;
        
        
        for(int i =0; i<n;i++){
            if(arr[i]==1){
                count++;
            }
            else{
                maxCount = max(maxCount ,count);
                count = 0;
            }
        }
        
        return max(maxCount,count) ;
    
        
    }
};
