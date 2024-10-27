# TicTacToe
A command-line-based Tic-Tac-Toe game where two players, or a player and a computer, can engage in a fun and strategic battle. This version supports three modes:

- Player vs Player
- Player vs Computer
- Computer vs Computer

## Board Layou

```
 7 | 8 | 9       7 | 8 | 9 
-----------     -----------
 4 | 5 | 6       4 | 5 | 6 
-----------     -----------
 1 | 2 | 3       1 | 2 | 3 
```

## How to Play

1. Choose Game Mode:
    - Player vs Computer: Enter the player's name to face the computer.
    - Player vs Player: Both players enter their names to compete.
    - Computer vs Computer: Watch two computer players face off automatically.

2. Enter Your Choice:
    - Players select X or O.
    - The player who goes first is chosen randomly.

3. Making Moves:
    - Input a number (1-9) corresponding to the board's position.
    - If the position is valid, your symbol is placed on the board.

4. Winning and Draws:
    - The game detects wins automatically when three identical symbols are aligned horizontally, vertically, or diagonally.
    - If all spaces are filled without a winner, the game ends in a draw.

5. Replay:
    - After the game finishes, choose whether to play again or exit.

## Example Gameplay

```
Select an option [0]-[2]: 1
Enter NAME of PLAYER 1: Alice
Enter NAME of PLAYER 2: Bob
Alice, Do you want to be X or O? X
Alice: X
Bob: O
Alice will go first!

    X |   |   
    -----------        
      |   |   
    -----------        
      |   |   

Alice (X), Choose your next position: (1-9) 7
```