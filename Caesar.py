import sys


def main():
    Input = sys.argv
    # Check if there is exactly 2 inputs of strings
    if len(Input) == 2:
        # Check if input are of integer type
        try:
            val = int(sys.argv[1])
        except ValueError:
            # Gives user correct instruction for the input
            print("Usage: ./caesar key")
            exit(1)
        # Assigning input to key
        key = int(sys.argv[1])
        # Prompt for user's input of the text that needs to be ciphered
        text = input("plaintext: ")
        # Execute cipher function
        caesarCipher(key, text)
        exit(0)
    else:
        # Gives user correct instruction for the input
        print("Usage: ./caesar key")
        exit(1)


def caesarCipher(Key, Text):
    # Prints the ciphered text based on the rotation of the characters in user's text input alphabetically according to user's input of a key that marks the number of rotation
    print("ciphertext: ", end='')
    for character in Text:
        # Check if the single character in the loop belongs to the cap'd group
        if character >= 'A' and character <= 'Z':
            # Calculate and print the new character
            print(chr(65 + ((ord(character) - 65 + Key) % 26)), end='')
        # Check if the single character in the loop belongs to the lowercased group
        elif character >= 'a' and character <= 'z':
            # Calculate and print the new character
            print(chr(97 + ((ord(character) - 97 + Key) % 26)), end='')
        else:
            # Print the character as it is (usually a special character like punctuations)
            print(character, end='')
    print()


if __name__ == "__main__":
    main()
