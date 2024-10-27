def default():
    print("\n🎮 Welcome to TIC-TAC-TOE! 🎮\nGet ready to showcase your strategy skills!\n")

def rules():
    print("📝 Here’s how the board maps to your keypad:\n")
    print(" 7 | 8 | 9 ")
    print("-----------")
    print(" 4 | 5 | 6 ")
    print("-----------")
    print(" 1 | 2 | 3 ")
    print("\nSimply input the position number (1-9) when prompted.")

def play():
    return input("\nReady to start the game? Type [Y]es or [N]o: ").upper().startswith('Y')

def names():
    p1_name = input("\nPlayer 1, what’s your name? ").capitalize()
    p2_name = input("Player 2, what’s your name? ").capitalize()
    return (p1_name, p2_name)

def choice():
    p1_choice = ' '
    p2_choice = ' '
    while p1_choice != 'X' or p1_choice != 'O':
        p1_choice = input(f"\n{p1_name}, would you like to play as X or O? ").upper()[0]
        if p1_choice == 'X' or p1_choice == 'O':
            break
        print("❌ Invalid choice! Choose either 'X' or 'O'.")
    if p1_choice == 'X':
        p2_choice = 'O'
    else:
        p2_choice = 'X'
    return (p1_choice, p2_choice)

def first_player():
    import random
    return random.choice((0, 1))

def display_board(board, avail):
    print("\n" + "    " + " {} | {} | {} ".format(board[7], board[8], board[9]) + 
          "        ⇄        " + " {} | {} | {} ".format(avail[7], avail[8], avail[9]))
    print("    " + "-----------" + "                " + "-----------")
    print("    " + " {} | {} | {} ".format(board[4], board[5], board[6]) + 
          "        ⇄        " + " {} | {} | {} ".format(avail[4], avail[5], avail[6]))
    print("    " + "-----------" + "                " + "-----------")
    print("    " + " {} | {} | {} ".format(board[1], board[2], board[3]) + 
          "        ⇄        " + " {} | {} | {} ".format(avail[1], avail[2], avail[3]))
    print("\n")

def player_choice(board, name, choice):
    position = 0
    while position not in [1, 2, 3, 4, 5, 6, 7, 8, 9] or not space_check(board, position):
        position = int(input(f'\n{name} ({choice}), it’s your turn! Choose a position (1-9): '))
        if position not in [1, 2, 3, 4, 5, 6, 7, 8, 9] or not space_check(board, position):
            print("⚠️ Oops! That’s not a valid move. Try again.")
    print("\n")
    return position

def CompAI(board, name, choice):
    position = 0
    possibilities = [x for x, letter in enumerate(board) if letter == ' ' and x != 0]
    for let in ['O', 'X']:
        for i in possibilities:
            boardCopy = board[:]
            boardCopy[i] = let
            if win_check(boardCopy, let):
                return i
    openCorners = [x for x in possibilities if x in [1, 3, 7, 9]]
    if openCorners:
        return selectRandom(openCorners)
    if 5 in possibilities:
        return 5
    openEdges = [x for x in possibilities if x in [2, 4, 6, 8]]
    if openEdges:
        return selectRandom(openEdges)

def selectRandom(board):
    import random
    return random.choice(board)

def place_marker(board, avail, choice, position):
    board[position] = choice
    avail[position] = ' '

def space_check(board, position):
    return board[position] == ' '

def full_board_check(board):
    return all(board[i] != ' ' for i in range(1, 10))

def win_check(board, choice):
    return (
        (board[1] == board[2] == board[3] == choice) or
        (board[4] == board[5] == board[6] == choice) or
        (board[7] == board[8] == board[9] == choice) or
        (board[1] == board[4] == board[7] == choice) or
        (board[2] == board[5] == board[8] == choice) or
        (board[3] == board[6] == board[9] == choice) or
        (board[1] == board[5] == board[9] == choice) or
        (board[3] == board[5] == board[7] == choice)
    )

def delay(mode):
    if mode == 2:
        import time
        time.sleep(2)

def replay():
    return input('\nWould you like to play another round? [Y]es or [N]o: ').lower().startswith('y')

print("\n\t\t WELCOME LONDO \n")
input("Press ENTER to start!")

default()
rules()

while True:
    theBoard = [' '] * 10
    available = [str(num) for num in range(10)]

    print("\n[0] Player vs. Computer\n[1] Player vs. Player\n[2] Computer vs. Computer")
    mode = int(input("\nSelect an option [0]-[2]: "))

    if mode == 1:
        p1_name, p2_name = names()
        p1_choice, p2_choice = choice()
    elif mode == 0:
        p1_name = input("\nEnter your name to play against the Computer: ").capitalize()
        p2_name = "Computer"
        p1_choice, p2_choice = choice()
    else:
        p1_name, p2_name = "Computer1", "Computer2"
        p1_choice, p2_choice = "X", "O"

    turn = p2_name if first_player() else p1_name
    print(f"\n✨ {turn} will make the first move. Good luck! 🎯")

    play_game = play() if mode != 2 else input("\nThis will be fast! Press ENTER to start!\n") == ''

    while play_game:
        display_board(theBoard, available)
        if turn == p1_name:
            position = player_choice(theBoard, p1_name, p1_choice) if mode != 2 else CompAI(theBoard, p1_name, p1_choice)
            place_marker(theBoard, available, p1_choice, position)
            if win_check(theBoard, p1_choice):
                display_board(theBoard, available)
                print(f"\n🏆 Hooray! {p1_name} wins! 🏆")
                break
            turn = p2_name
        else:
            position = player_choice(theBoard, p2_name, p2_choice) if mode == 1 else CompAI(theBoard, p2_name, p2_choice)
            place_marker(theBoard, available, p2_choice, position)
            if win_check(theBoard, p2_choice):
                display_board(theBoard, available)
                print(f"\n🏆 Hooray! {p2_name} wins! 🏆")
                break
            turn = p1_name

        if full_board_check(theBoard):
            display_board(theBoard, available)
            print("\nIt’s a draw! Well played both! 🤝")
            break

        delay(mode)

    if not replay():
        print("\nThanks for playing! See you next time! 👋")
        break