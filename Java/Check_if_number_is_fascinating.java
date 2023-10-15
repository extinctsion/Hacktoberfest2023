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