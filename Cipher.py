def caesar_cipher_encrypt(text, shift):
    """
    Encrypts the input text using the Caesar Cipher algorithm with the given shift.
    
    Parameters:
    text (str): The input text to be encrypted.
    shift (int): The shift value for the Caesar Cipher.
    
    Returns:
    str: The encrypted text.
    """
    encrypted_text = ""
    for char in text:
        if char.isalpha():
            shift_amount = shift % 26
            char_code = ord(char)
            base = ord('A') if char.isupper() else ord('a')
            encrypted_char = chr(base + (char_code - base + shift_amount) % 26)
            encrypted_text += encrypted_char
        else:
            encrypted_text += char
    return encrypted_text


def caesar_cipher_decrypt(text, shift):
    """
    Decrypts the input text using the Caesar Cipher algorithm with the given shift.
    
    Parameters:
    text (str): The input text to be decrypted.
    shift (int): The shift value for the Caesar Cipher.
    
    Returns:
    str: The decrypted text.
    """
    return caesar_cipher_encrypt(text, -shift)


def main():
    """
    Main function to run the Caesar Cipher encryption and decryption.
    """
    while True:
        print("Caesar Cipher Program")
        print("1. Encrypt a message")
        print("2. Decrypt a message")
        print("3. Exit")
        choice = input("Enter your choice (1/2/3): ")
        
        if choice == '1':
            message = input("Enter the message to encrypt: ")
            shift = int(input("Enter the shift value: "))
            encrypted_message = caesar_cipher_encrypt(message, shift)
            print(f"Encrypted Message: {encrypted_message}\n")
        
        elif choice == '2':
            message = input("Enter the message to decrypt: ")
            shift = int(input("Enter the shift value: "))
            decrypted_message = caesar_cipher_decrypt(message, shift)
            print(f"Decrypted Message: {decrypted_message}\n")
        
        elif choice == '3':
            print("Exiting the program.")
            break
        
        else:
            print("Invalid choice. Please try again.\n")


if __name__ == "__main__":
    main()
