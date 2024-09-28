class Main: 
    def __init__(self, key: dict) -> None:
        self.key = key

    def get_input(self) -> None: 
        while True:
            input_string = str(input("Enter the sentence: "))
            if input_string.replace(" ", "").isalpha():
                self.input_string = input_string.lower()
                break
            else:
                print("Input is not valid. Please enter alphabetic characters only, spaces are allowed.")
    
    def encrypt_string(self) -> str:
        output = ""
        for c in self.input_string:
            if c in self.key:
                output += self.key[c]
            elif c == " ":
                output += " "
        return output

    def decrypt_string(self) -> str:
        output = "" 
        for c in self.input_string:
            if c == " ":
                output += " "
            else:
                for k, v in self.key.items():
                    if v == c:
                        output += k
        return output

if __name__ == "__main__":
    key = {"a": "d", "b": "e", "c": "f", "d": "g", "e": "h", "f": "i", "g": "j", "h": "k", "i": "l", "j": "m", 
           "k": "n", "l": "o", "m": "p", "n": "q", "o": "r", "p": "s", "q": "t", "r": "u", "s": "v", "t": "w", 
           "u": "x", "v": "y", "w": "z", "x": "a", "y": "b", "z": "c"}
    
    choice = input("Do you want to encrypt or decrypt? ").lower()
    cipher = Main(key=key)
    
    if choice == "encrypt":
        cipher.get_input()
        encrypted = cipher.encrypt_string()
        print("Encrypted string:", encrypted)
    elif choice == "decrypt":
        cipher.get_input()
        decrypted = cipher.decrypt_string()
        print("Decrypted string:", decrypted)
    else:
        print("Invalid choice")