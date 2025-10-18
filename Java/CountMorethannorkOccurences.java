import java.util.HashMap;

public class CountMorethannorkOccurences {
    public int countOccurence(int[] arr, int n, int k) 
    {
        HashMap<Integer,Integer> map=new HashMap<Integer,Integer>();
        // your code here,return the answer
        int count=0;
        for(int i=0;i<n;i++){
            if(!map.containsKey(arr[i])){
                map.put(arr[i],1);
            }
            else{
                int value=map.get(arr[i]);
                if(value!=0){
                map.put(arr[i],value+1);
                }
                
                if(value+1>n/k ){
                    count++;
                    map.put(arr[i],0);
                }
                
            }
        }
        return count;
    }

    public static void main(String[] args) {
        CountMorethannorkOccurences obj=new CountMorethannorkOccurences();
        int[] arr={3,1,2,2,1,2,3,3};
        int n=arr.length;
        int k=4;
        System.out.println(obj.countOccurence(arr, n, k));
    }
}
