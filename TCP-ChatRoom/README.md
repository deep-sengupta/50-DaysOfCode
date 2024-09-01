# TCP Chat Room
This is a simple multi-user chat room application implemented using Python's socket and threading modules. The application consists of a server that handles multiple clients, allowing them to send and receive messages in real-time.

## Files
- `server.py`: This file contains the server-side code. The server handles multiple clients, broadcasts messages, and manages user connections and disconnections.
- `client.py`: This file contains the client-side code. Each client connects to the server, sends and receives messages, and can exit the chat room.

## How to Run
### Running the Server
1. Open a terminal.
2. Navigate to the directory where `server.py` is located.
3. Run the server using Python:

```
python3 server.py
```
Output:
```
Server is running and listening...
```

The server will start and begin listening for incoming client connections.

### Running the Client
1. Open a new terminal window for each client.
2. Navigate to the directory where client.py is located.
3. Run the client using Python:

```
python3 client.py
```
Output:
```
Choose a username >>> Deep

Welcome to the chat room! Type '/exit' to leave the chat room.
```

4. When prompted, enter a username for the chat room.
5. After entering the username, you will see a welcome message. You can now start typing messages to send them to the chat room.
6. To exit the chat room, type /exit. This will close the connection, and a message will be sent to the server indicating that you have left.

## Exiting the Chat Room
To exit, simply type `/exit`. The following will be displayed:
```
You have exited the chat room.
```

And on the server:
```
Deep has exited the chat room.
```