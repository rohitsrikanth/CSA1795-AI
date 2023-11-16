# Tic-Tac-Toe Program using
# random number in Python

# importing all necessary libraries
import numpy as np
import random
from time import sleep

# Creates an empty board


def create_board():
	return(np.array([["0", "0", "0"],
					["0", "0", "0"],
					["0", "0", "0"]]))

# Check for empty places on board


def possibilities(board):
	l = []

	for i in range(len(board)):
		for j in range(len(board)):

			if board[i][j] == "0":
				l.append((i, j))
	return(l)

# Select a random place for the player


def random_place(board, player):
	selection = possibilities(board)
	current_loc = random.choice(selection)
	print(current_loc)
	board[current_loc] = player
	return(board)

# Checks whether the player has three
# of their marks in a horizontal row
def check_winner(board):
    a="0"
    # Check rows, columns, and diagonals for a winner
    for row in board:
        if row[0] == row[1] == row[2] and row[0] != '0':
            a=row[0]
            return a

    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] != '0':
            a=board[0][col]
            return a

    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != '0':
        a=board[0][0]
        return a

    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != '0':
        a=board[0][2]
        return a
    return a
# Main function to start the game


def play_game():
	board, winner, counter = create_board(), "0", 1
	print(board)
	sleep(2)

	while winner == "0":
		for player in ["X","Y"]:
			board = random_place(board, player)
			print("Board after " + str(counter) + " move")
			print(board)
			sleep(2)
			counter += 1
			winner = check_winner(board)
			if winner !="0":
				break
	return(winner)


# Driver Code
print("Winner is: " + str(play_game()))
