import java.util.*;
public class Palindrome {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        System.out.print("Enter a string: ");
        String input = sc.nextLine();

        if (Palindrome(input)) {
            char middleCharacter = findMiddleCharacter(input);
            System.out.println("Middle Character: " + middleCharacter);
        } else {
            String palindrome = convertToPalindrome(input);
            char middleCharacter = findMiddleCharacter(palindrome);
            System.out.println("Converted Palindrome: " + palindrome);
            System.out.println("Middle Character: " + middleCharacter);
        }
    }    
}
public static boolean Palindrome(String str) {
    int left = 0;
    int right = str.length() - 1;

    while (left < right) {
        if (str.charAt(left) != str.charAt(right)) {
            return false;
        }
        left++;
        right--;
    }

    return true;
}

public static String convertToPalindrome(String str) {
    StringBuilder palindromeBuilder = new StringBuilder(str);

    for (int i = str.length() - 2; i >= 0; i--) {
        palindromeBuilder.append(str.charAt(i));
    }

    return palindromeBuilder.toString();
}

public static char findMiddleCharacter(String str) {
    int length = str.length();
    int middleIndex = length / 2;

    // If the length is odd, the middle character is at the middle index
    if (length % 2 != 0) {
        return str.charAt(middleIndex);
    }

    // If the length is even, the middle character is at the (middleIndex - 1) index
    return str.charAt(middleIndex - 1);
}
