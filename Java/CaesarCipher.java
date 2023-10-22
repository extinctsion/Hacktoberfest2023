import java.util.Scanner;

public class CaesarCipher {

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        // Input
        System.out.print("Enter the text to be encoded: ");
        String text = scanner.nextLine();

        System.out.print("Enter the shift value: ");
        int shift = scanner.nextInt();

        // Function to encode text
        String encodedText = caesarCipher(text, shift);

        // Output
        System.out.println("Encoded text: " + encodedText);
    }

    public static String caesarCipher(String text, int shift) {
        StringBuilder result = new StringBuilder();

        for (int i = 0; i < text.length(); i++) {
            char currentChar = text.charAt(i);

            // Check if the character is an uppercase letter
            if (Character.isUpperCase(currentChar)) {
                result.append((char) ((currentChar - 'A' + shift) % 26 + 'A'));
            }
            // Check if the character is a lowercase letter
            else if (Character.isLowerCase(currentChar)) {
                result.append((char) ((currentChar - 'a' + shift) % 26 + 'a'));
            }
            // Leave non-alphabetic characters unchanged
            else {
                result.append(currentChar);
            }
        }

        return result.toString();
    }
}
