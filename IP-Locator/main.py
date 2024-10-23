import subprocess
import IPlocate
import pyfiglet

def display_menu():
    header = pyfiglet.figlet_format("IP LOOKUP")
    print(header)

    print("\nSelect an action from the list below:")
    print("* Press 1 to trace the location of a specific IP address")
    print("* Press 2 to display your current public IP address")
    print("* Press 3 to close the application")
    print("* Type clear to reset the screen")
    print("* Type q to stop any ongoing task")

def option_1():
    IPlocate.locate_ip()
    home()

def option_2():
    IPlocate.get_ip()
    home()

def option_3():
    quit()

def home():
    available_options = (1, 2, 3)

    while True:
        try:
            selected_option = input("\nPlease select an option\n>>> ")
            if selected_option == 'clear':
                subprocess.call('cls', shell=True)
                display_menu()
                continue
            else:
                selected_option = int(selected_option)
        except ValueError:
            print("Invalid input. Enter the number corresponding to an option.")
            continue
        else:
            if selected_option not in available_options:
                print("The option is not valid. Try again.")
                continue
            else:
                break

    if selected_option == 1:
        option_1()
    elif selected_option == 2:
        option_2()
    elif selected_option == 3:
        option_3()

def start_program():
    display_menu()
    home()

start_program()