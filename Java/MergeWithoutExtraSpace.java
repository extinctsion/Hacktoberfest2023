import java.util.Arrays;

public class MergeWithoutExtraSpace {

    public static void merge(long arr1[], long arr2[], int n, int m) 
    {
        // code here 
        int i=n-1,j=0;
       
       while(i>=0 && j<m)
       {
           
           if(arr1[i]>arr2[j])
           {
               long temp=arr1[i];
               arr1[i]=arr2[j];
               arr2[j]=temp;
           }
           i--;
           j++;
       }
       
       Arrays.sort(arr1);
       Arrays.sort(arr2);
    }

    public static void main(String[] args)
    {
        long[] arr1 = {1, 3, 5, 7};
        long[] arr2 = {0, 2, 6, 8, 9};
        int n = arr1.length;
        int m = arr2.length;
        merge(arr1, arr2, n, m);
        System.out.println(Arrays.toString(arr1));
        System.out.println(Arrays.toString(arr2));
    }
    
}
