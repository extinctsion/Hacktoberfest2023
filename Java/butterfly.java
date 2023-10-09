public class butterfly{
    public static void main(String[] args) {
        // int n = 4;
        // for(int i=1;i<=n;i++){
        //     for(int j=1;j<=i;j++){
        //         System.out.print("*");

        //     }
        //     int spaces=2*(n-i);
        //     for(int j=1;j<=spaces;j++){
        //         System.out.print(" ");
        //     }
        //     for(int j=1;j<=i;j++){
        //         System.out.print("*");

        //     }
        //     System.out.println();
            
        // }
        // for(int i=n;i>=1;i--){
        //     for(int j=1;j<=i;j++){
        //         System.out.print("*");

        //     }
        //     int spaces=2*(n-i);
        //     for(int j=1;j<=spaces;j++){
        //         System.out.print(" ");
        //     }
        //     for(int j=1;j<=i;j++){
        //         System.out.print("*");

        //     }
        //     System.out.println();
            
        // }

        //another ques
        // int n=5;
        // for(int i=1;i<=n;i++){
        //     int spaces=n-i;
        //     for(int j=1;j<=spaces;j++){
        //         System.out.print(" ");
        //     }
            
        //     for(int j=1;j<=n;j++){
        //         System.out.print("*");
        //     }
        //     System.out.println();
            

        // }
        

        //another ques
        // int n=5;
        // for(int i=1;i<=n;i++){
        //     int spaces=n-i;
        //     for(int j=1;j<=spaces;j++){
        //         System.out.print(" ");
        //     }

        //     for(int j=1;j<=i;j++){
        //         System.out.print(i+" ");
        //     }
        //     System.out.println();
        // }


        //diamond
        int n=5;
        for(int i=1;i<=n;i++){
            for(int j=1;j<=n-i;j++){
                System.out.print(" ");
            }
            for(int j=1;j<=(2*i-1);j++){
                System.out.print("*");
            }
            System.out.println();
        }
        for(int i=n;i>=1;i--){
            for(int j=1;j<=n-i;j++){
                System.out.print(" ");
            }
            for(int j=1;j<=(2*i-1);j++){
                System.out.print("*");
            }
            System.out.println();
        }

    }
}
