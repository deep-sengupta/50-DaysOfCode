import threading
import socket

username = input('Choose a username |-> ')
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('127.0.0.1', 55000))

print("\nWelcome to the chat room! Type '/exit' to leave the chat room.")

def client_receive():
    while True:
        try:
            message = client.recv(1024).decode('utf-8')
            if message == "username?":
                client.send(username.encode('utf-8'))
            else:
                print(message)
        except:
            print('Chat Ended!')
            client.close()
            break

def client_send():
    while True:
        message = input("")
        if message == '/exit':
            client.send(f'{username} has left the chat room.'.encode('utf-8'))
            print("You have exited the chat room.")
            client.close()
            break
        else:
            client.send(f'{username}: {message}'.encode('utf-8'))

receive_thread = threading.Thread(target=client_receive)
receive_thread.start()

send_thread = threading.Thread(target=client_send)
send_thread.start()
