from manage import AES256
from savepass import Saver
import os
import pyfiglet

saver = Saver("passwords.txt")
passwords = saver.read()
master_password_file = "master_password.txt"

def display_header():
    clear_screen()
    ascii_banner = pyfiglet.figlet_format("LockBox")
    print(ascii_banner)

def clear_screen():
    os.system("clear" if os.name == "posix" else "cls")

def get_choice():
    try:
        choice = int(input("\nEnter your choice (1-5): "))
        if choice < 1 or choice > 5:
            raise ValueError
        return choice
    except ValueError:
        print("Invalid input! Please enter a number between 1 and 5.")
        return None

def get_application_name():
    app = input("Enter Application Name: ").strip()
    if not app:
        print("Application name cannot be empty.")
        return None
    return app

def initialize_master_password():
    if not os.path.exists(master_password_file) or os.stat(master_password_file).st_size == 0:
        print("Create a new Master Password: ", end="")
        master_password = input().strip()
        if not master_password:
            print("Master password cannot be empty. Exiting.")
            exit()
        encrypter = AES256(master_password)
        encrypted_master_password = encrypter.encrypt(master_password).decode()
        with open(master_password_file, "w") as file:
            file.write(encrypted_master_password)
        print("Master Password created successfully. Please remember it for future logins.")
    else:
        print("Enter your Master Password: ", end="")
        master_password = input().strip()
        with open(master_password_file, "r") as file:
            encrypted_master_password = file.read().strip()
        encrypter = AES256(master_password)
        if encrypter.encrypt(master_password).decode() != encrypted_master_password:
            print("Incorrect Master Password. Exiting.")
            exit()
        print("Logged in successfully.")
    return encrypter

clear_screen()
display_header()
encrypter = initialize_master_password()

while True:
    display_header()
    print("Password Manager")
    print("1. Retrieve Password")
    print("2. Save New Password")
    print("3. Remove Password")
    print("4. Change Master Password")
    print("5. Exit")

    choice = get_choice()
    if choice is None:
        input("Press Enter to continue...")
        continue

    if choice == 5:
        print("Exiting Password Manager. Goodbye!")
        break

    if choice == 4:
        print("Enter new Master Password: ", end="")
        new_master_password = input().strip()
        if not new_master_password:
            print("Master password cannot be empty.")
            input("Press Enter to continue...")
            continue
        encrypter = AES256(new_master_password)
        with open(master_password_file, "w") as file:
            file.write(encrypter.encrypt(new_master_password).decode())
        print("Master Password changed successfully.")
        input("Press Enter to continue...")
        continue

    app = get_application_name()
    if app is None:
        input("Press Enter to continue...")
        continue

    if choice == 1:
        found = False
        for entry in passwords:
            if app in encrypter.decrypt(entry[0]):
                print("\n-----------------------------------------")
                print(f"Application: {encrypter.decrypt(entry[0])}")
                print(f"Password: {encrypter.decrypt(entry[1])}")
                found = True
        if not found:
            print(f"No password found for '{app}'.")
        input("Press Enter to continue...")

    elif choice == 2:
        password = input("Enter the password to save: ")
        if password:
            passwords.append([encrypter.encrypt(app).decode(), encrypter.encrypt(password).decode()])
            saver.save(passwords)
            print(f"Password for '{app}' saved successfully.")
        else:
            print("Password cannot be empty.")
        input("Press Enter to continue...")

    elif choice == 3:
        found = False
        for entry in passwords:
            if app == encrypter.decrypt(entry[0]):
                confirm = input(f"Are you sure you want to delete the password for '{app}'? [y/n]: ").lower()
                if confirm == "y":
                    passwords.remove(entry)
                    saver.save(passwords)
                    print(f"Password for '{app}' deleted successfully.")
                found = True
                break
        if not found:
            print(f"No password found for '{app}'.")
        input("Press Enter to continue...")
