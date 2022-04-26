import os
import random

clear = lambda: os.system('clear')

def display_board(board):
    clear()
    print(board[1]+"|"+board[2]+"|"+board[3])
    print(board[4]+"|"+board[5]+"|"+board[6])
    print(board[7]+"|"+board[8]+"|"+board[9])

def  player_input():
    marker = ''

    while marker != 'X' and marker != 'O':
        marker = input("Player 1, choose X or O: ")
        if marker != 'X' and marker != 'O':
            print("Please choose X or O")

    player1 = marker
    if player1 == 'X':
        player2 = 'O'
    else:
        player2 = 'X'

    return (player1, player2)

def place_marker(board, marker, position):
    board[position] = marker

def win_check(board, mark):
    result = False
    if board[1] == board[2] == board[3] == mark:
        result = True
    elif board[4] == board[5] == board[6] == mark:
        result = True
    elif board[7] == board[8] == board[9] == mark:
        result = True
    elif board[1] == board[4] == board[7] == mark:
        result = True
    elif board[2] == board[5] == board[8] == mark:
        result = True
    elif board[3] == board[6] == board[9] == mark:
        result = True
    elif board[1] == board[5] == board[9] == mark:
        result = True
    elif board[3] == board[5] == board[7] == mark:
        result = True
    else:
        result = False
    return result

def choose_first():
    result = ""
    rand = random.randint(0, 1)
    if rand == 0:
        result = "Player 1"
    else:
        result = "Player 2"
    return result

def space_check(board, position):
    return board[position] == ' '

def full_board_check(board):
    for i in range(1, 10):
        if space_check(board, i):
            return False
    return True

def player_choice(board):
    choice = 'wrong'
    acceptable_range = range(1, 10)
    within_range = False
    position_status = False

    while choice.isdigit() == False or within_range == False or position_status == False:
        choice = input("Please select position (1-9): ")

        if choice.isdigit() == False:
            print("Sorry, but you entered not a number")

        if choice.isdigit():
            if int(choice) in acceptable_range:
                within_range = True
                if space_check(board, int(choice)):
                    position_status = True
                else:
                    print("Sorry, but position is not empty")
            else:
                print("Sorry, but you entered value out of range (1-9)")

    return int(choice)

def replay():
    choice = ''
    result = False
    while choice not in ['Y', 'N']:
        choice = input("Do you want to play again? (Y or N) ")

        if choice not in ['Y', 'N']:
            print("Sorry, but I don't understand, please choose Y or N")
        
    if choice == 'Y':
        result = True
    return result 

while True:
    board = ['#',' ',' ',' ',' ',' ',' ',' ',' ',' ']
    player1, player2 = player_input()

    turn = choose_first()
    print(turn + " will go first")

    play_game = input('Ready to play? y or n? ')

    if play_game == 'y':
        game_on = True
    else:
        game_on = False

    while game_on:

        if turn == 'Player 1':
            display_board(board)
            position = player_choice(board)
            place_marker(board, player1, position)
            if win_check(board, player1):
                display_board(board)
                print('Player 1 HAS WON!!!')
                game_on = False
            else:
                if full_board_check(board):
                    display_board(board)
                    print('TIE GAME!!!')
                    game_on = False
                else:
                    turn = 'Player 2'
        else:
            display_board(board)
            position = player_choice(board)
            place_marker(board, player2, position)
            if win_check(board, player2):
                display_board(board)
                print('Player 2 HAS WON!!!')
                game_on = False
            else:
                if full_board_check(board):
                    display_board(board)
                    print('TIE GAME!!!')
                    game_on = False
                else:
                    turn = 'Player 1'

    if not replay():
        break