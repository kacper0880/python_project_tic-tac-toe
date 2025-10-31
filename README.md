# **Tic-Tac-Toe Game**



## GitHub Repository



GitHub contains everything in the file needed to run the games including the history of all the commits and changes that happened over the course of the game's creation.

GitHub URL: https://github.com/kacper0880/python\_project\_tic-tac-toe    



## Description



This is a basic Tic-Tac-Toe game built in python using the Pygame extension library. The user can choose to play against the computer (PvE) where the user is playing as X's and computer as O's. The other choice is to play player vs player (PvP) offline where each player will alternate making moves. The winner is decided by having 3 consecutive grid spaces filled with their respective symbol ('X' or 'O') in a horizontal, vertical or diagonal direction.



## Instructions

This game follows the simple Tic-Tac-Toe rules where two players play as either 'X' or an 'O'. The winner is decided by achieving a consecutive line of their respective symbol in either horizontal, vertical or diagonal direction. 



The game launches with a simple interface telling the user keybinds:

* Key 'Y' places the user in a player vs player mode where the user is inputting both X's and O's. It is intended to play the game alongside someone else.
* To place a symbol, simply hover over a grid cell with your mouse and left-click (LMB).
* Key 'A' places the user in a player vs computer (PvE) where the player plays as X's and the computer as the O's.
* Key 'Spacebar' will display for roughly 1.5 seconds the scoreboard at the bottom of the screen which shows the record of the number of times 'X' won, 'O' won and 'Draws'. 
* Key 'Q' quits the game at any time



The end of each match is decided by whether a player has managed to get 3 consecutive symbols or all the cells in the grid are occupied. The user will be prompted to either start a new match ('Y') or quit ('Q').



## Launching the game

1. Download the folder onto your desktop
2. Open up the folder in VSS
3. Select the tic-tac-toe.py on the explorer on the left
4. Run the code CTRL + ALT + N or press the "Play" button at the top right
5. Play the game



## File Contents

* cross.png = 'X' image
* letter-o.png = 'O' image
* Flowchart.drawio = Flowchart of the Tic-Tac-Toe game
* flowchart.drawio.png = Picture of the flowchart showing the logic of the game
* tic-tac-toe.py = Python file of the game



## Dependencies

* Download Python (tested with Python version 3.13.5)
* Download the file contents from GitHub link/folder
* Download and install Pygame
* Download and install Visual Studio Code (VSS)

Tested on:
Version: 1.105.1 (user setup)

OS: Windows\_NT x64 10.0.26200



## Flowchart



There are two files that show the same diagram.

* Flowchart.drawio = Used if you want to open the file on the website draw.io
* Flowchart.drawio.png = A picture of the flowchart if the user doesn't want to use the website to view it



In essence the flowchart demonstrates the game's logic. It showcases the game loop, the decisions that the user can make and how that influences the loop whilst highlighting the questions dictating the flow of logic.



