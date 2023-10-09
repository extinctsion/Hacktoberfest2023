class vehicle{
    void run(){
        System.out.println("vehicle");
    }
}
class bike extends vehicle{
    void run(){
        System.out.println("Bike");
    }
}
class scooty extends vehicle{
    void run(){
        System.out.println("Scooty");
    }
}
public class methodoverriding {
    public static void main(String[] args) {
        bike b=new bike();
        b.run();
        scooty s=new scooty();
        s.run();
    }
}
