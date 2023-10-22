#include <iostream>
#include <string>

void caesarCipher(std::string& text, int shift);

int main() {
    std::string text;
    int shift;

    // Input
    std::cout << "Enter the text to be encoded: ";
    std::getline(std::cin, text);

    std::cout << "Enter the shift value: ";
    std::cin >> shift;

    // Function to encode text
    caesarCipher(text, shift);

    // Output
    std::cout << "Encoded text: " << text << std::endl;

    return 0;
}

void caesarCipher(std::string& text, int shift) {
    for (size_t i = 0; i < text.length(); ++i) {
        char currentChar = text[i];

        // Check if the character is an uppercase letter
        if (std::isupper(currentChar)) {
            text[i] = ((currentChar - 'A' + shift) % 26) + 'A';
        }
        // Check if the character is a lowercase letter
        else if (std::islower(currentChar)) {
            text[i] = ((currentChar - 'a' + shift) % 26) + 'a';
        }
        // Leave non-alphabetic characters unchanged
    }
}
