import java.util.Scanner;

public class arrayque {
    public static void main(String[] args) {
        Scanner sc=new Scanner(System.in);
        int n=sc.nextInt();
        int arr[]=new int[n+1];
        for(int i=0;i<n;i++){
            arr[i]=sc.nextInt();
        }
        System.out.println(arr);
    }
}
