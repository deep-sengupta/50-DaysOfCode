def encrypt(text, shift_key):
    encrypted_text = ""

    for char in text:
        if char.isupper():
            encrypted_text += chr((ord(char) + shift_key - 65) % 26 + 65)
        elif char.islower():
            encrypted_text += chr((ord(char) + shift_key - 97) % 26 + 97)
        else:
            encrypted_text += char

    return encrypted_text

def decrypt(text, shift_key):
    decrypted_text = ""

    for char in text:
        if char.isupper():
            decrypted_text += chr((ord(char) - shift_key - 65) % 26 + 65)
        elif char.islower():
            decrypted_text += chr((ord(char) - shift_key - 97) % 26 + 97)
        else:
            decrypted_text += char

    return decrypted_text

def main():
    print("Welcome to the Caesar Cipher Text Encryptor/Decryptor")

    try:
        choice = int(input("\nSelect an option:\n1. Encrypt text\n2. Decrypt text\nEnter your choice (1 or 2): "))

        if choice not in [1, 2]:
            print("Invalid choice! Please select either 1 or 2.")
            return

        text = input("Enter the text: ")
        shift_key = int(input("Enter the shift key (numeric value for the cipher): "))

        if choice == 1:
            result = encrypt(text, shift_key)
            print(f"\nEncrypted Text: {result}")
        elif choice == 2:
            result = decrypt(text, shift_key)
            print(f"\nDecrypted Text: {result}")

    except ValueError:
        print("Error: Please enter valid numeric inputs for your choice and shift key.")

if __name__ == "__main__":
    main()