# tic-tac-toe game

__author__ = "Andres Gerardy"

import random


def game_board(board):
    # this function prints the board
    """

    param board: the function takes in the list board and prints the
    corresponding spots on the board
    """
    print("|", board[0], "|", board[1], "|", board[2], "|")
    print("|", board[3], "|", board[4], "|", board[5], "|")
    print("|", board[6], "|", board[7], "|", board[8], "|")
    print()
    print()


def win_lose_draw_check(turn, board):
    """
# this function checks if there is a win, loss, or draw
    :param board:
    :param turn: I just wanted to pass in the number 1 into the function
    :return: if the value one is returned, that means that there is a win,
    loss, or draw
    """

    if board[0] == "X" and board[1] == "X" and board[2] == "X":
        print("You won!")
        win = turn
        return win
    elif board[3] == "X" and board[4] == "X" and board[5] == "X":
        print("You won!")
        win = turn
        return win
    elif board[6] == "X" and board[7] == "X" and board[8] == "X":
        print("You won!")
        win = turn
        return win
    elif board[0] == "X" and board[4] == "X" and board[8] == "X":
        print("You won!")
        win = turn
        return win
    elif board[2] == "X" and board[4] == "X" and board[6] == "X":
        print("You won!")
        win = turn
        return win
    elif board[0] == "X" and board[3] == "X" and board[6] == "X":
        print("You won!")
        win = turn
        return win
    elif board[1] == "X" and board[4] == "X" and board[7] == "X":
        print("You won!")
        win = turn
        return win
    elif board[2] == "X" and board[5] == "X" and board[8] == "X":
        print("You won!")
        win = turn
        return win
    if board[0] == "O" and board[1] == "O" and board[2] == "O":
        print("You Lose!")
        lose = turn
        return lose
    elif board[3] == "O" and board[4] == "O" and board[5] == "O":
        print("You Lose!")
        lose = turn
        return lose
    elif board[6] == "O" and board[7] == "O" and board[8] == "O":
        print("You Lose!")
        lose = turn
        return lose
    elif board[0] == "O" and board[4] == "O" and board[8] == "O":
        print("You Lose!")
        lose = turn
        return lose
    elif board[2] == "O" and board[4] == "O" and board[6] == "O":
        print("You Lose!")
        lose = turn
        return lose
    elif board[0] == "O" and board[3] == "O" and board[6] == "O":
        print("You Lose!")
        lose = turn
        return lose
    elif board[1] == "O" and board[4] == "O" and board[7] == "O":
        print("You Lose!")
        lose = turn
        return lose
    elif board[2] == "O" and board[5] == "O" and board[8] == "O":
        print("You Lose!")
        lose = turn
        return lose
    elif "_" not in board:
        print("Its a draw!")
        draw = turn
        return draw


# Level 1
def main():
    board = ["_", "_", "_",
             "_", "_", "_",
             "_", "_", "_"]
    level = 1
    players_turn = 2
    game_board(board)
    while level == 1:
        # players turn
        while players_turn % 2 == 0 and players_turn != 0:
            is_number = False
            while is_number == False:
                player_input = input("enter a number 1-9.")
                # checks if user entered a number
                try:
                    int(player_input)
                    is_number = True
                except:
                    print("Please enter a whole number")
            if int(player_input) == 0:
                print(
                    "idk where the 0 spot is so ill just take my turn")
                players_turn += 1
            elif int(player_input) < 0:
                print("there isn't a", player_input,
                      "box on the board...I'm guessing you meant",
                      abs(int(player_input)))
                player_input = abs(int(player_input))
            if 9 >= int(player_input) > 0 and board[
                int(player_input) - 1] == "_":
                board[int(player_input) - 1] = "X"
                game_board(board)
                # checks if it is  a win or draw by returning 1.
                # If 1 is returned, player_input=0
                # It stops asking for input and the level goes up one
                win_check = win_lose_draw_check(1, board)
                draw_check = win_lose_draw_check(1, board)
                if win_check == 1 or draw_check == 1:
                    players_turn = 0
                    level += 1
                else:
                    players_turn += 1
            # tells user why number in unacceptable
            else:
                if int(player_input) > 9:
                    print("There arent that many spaces on the board"
                          "...try again")
                elif board[int(player_input) - 1] == "O":
                    print("I already went there...try again")
                elif board[int(player_input) - 1] == "X":
                    print("You already went there...try again")
            # computers turn
        while players_turn % 2 != 0:
            computer_input_check = 0
            while computer_input_check == 0:
                # computer picks a random spot that hasn't already been taken
                computer_input = random.randrange(0, 9)
                if board[computer_input] == "_":
                    board[computer_input] = "O"
                    computer_input_check = 1
                    game_board(board)
                    lose_check = win_lose_draw_check(1, board)
                    draw_check = win_lose_draw_check(1, board)
                    # checks for loss or draw
                    if lose_check == 1 or draw_check == 1:
                        players_turn = 0
                        level += 1
                    else:
                        # if there is no draw or loss, the user takes its turn
                        players_turn += 1
                else:
                    computer_input_check = 0

    # level 2
    print("Level 2")
    # the game board gets cleared
    board = ["_", "_", "_",
             "_", "_", "_",
             "_", "_", "_"]
    game_board(board)
    while level == 2:
        players_turn = 2
        # users turn
        # occurs when players_turn is an even number
        while players_turn % 2 == 0 and players_turn != 0:
            is_number = False
            while is_number == False:
                player_input = input("enter a number 1-9")
                # checks if user entered a number
                try:
                    int(player_input)
                    is_number = True
                except:
                    print("Please enter a whole number")
            # checks if number inputted is 0 or negative
            if int(player_input) == 0:
                print(
                    "hmm idk where the 0 spot is so ill just take my turn")
                players_turn += 1
            elif int(player_input) < 0:
                print("there isn't a", player_input,
                      "box on the board...I'm guessing you meant",
                      abs(int(player_input)))
                player_input = abs(int(player_input))
            # checks if number is within range of board
            # and that the spot chosen is not occupied
            if 9 >= int(player_input) > 0 and board[
                int(player_input) - 1] == "_":
                board[int(player_input) - 1] = "X"
                game_board(board)
                win_check = win_lose_draw_check(1, board)
                draw_check = win_lose_draw_check(1, board)
                if win_check == 1 or draw_check == 1:
                    players_turn = 0
                    level = 3
                else:
                    players_turn += 1
            # tells user why number in unacceptable
            else:
                if int(player_input) >= 10:
                    print("There arent that many spaces on the board"
                          "...try again")
                elif board[int(player_input)] == "O":
                    print("I already went there...try again")
                elif board[int(player_input)] == "X":
                    print("You already went there...try again")
        # computers turn
        # occurs when players_turn is an odd number
        while players_turn % 2 != 0:
            # computer blocks user if there are 2 in a row I couldn't think of
            # an algorithm to check if there are 2 in a row, so I coded in
            # every possible scenario At the end of every turn, it calls
            # win_lose_draw_check to check if there is a win loss or draw. If
            # the value 1 is returned, player_input=0,
            # so it stops asking for an
            # input, and the Level number goes up 1
            if board[0] == "X" and board[1] == "X" and board[2] == "_":
                computer_input = 2
                board[computer_input] = "O"
                game_board(board)
                lose_check = win_lose_draw_check(1, board)
                draw_check = win_lose_draw_check(1, board)
                if lose_check == 1 or draw_check == 1:
                    players_turn = 0
                    level += 1
                else:
                    players_turn += 1

            elif board[0] == "X" and board[2] == "X" and board[1] == "_":
                computer_input = 1
                board[computer_input] = "O"
                game_board(board)
                lose_check = win_lose_draw_check(1, board)
                draw_check = win_lose_draw_check(1, board)
                if lose_check == 1 or draw_check == 1:
                    players_turn = 0
                    level += 1
                else:
                    players_turn += 1
            elif board[1] == "X" and board[2] == "X" and board[0] == "_":
                computer_input = 0
                board[computer_input] = "O"
                game_board(board)
                lose_check = win_lose_draw_check(1, board)
                draw_check = win_lose_draw_check(1, board)
                if lose_check == 1 or draw_check == 1:
                    players_turn = 0
                    level += 1
                else:
                    players_turn += 1
            elif board[3] == "X" and board[4] == "X" and board[5] == "_":
                computer_input = 5
                board[computer_input] = "O"
                game_board(board)
                lose_check = win_lose_draw_check(1, board)
                draw_check = win_lose_draw_check(1, board)
                if lose_check == 1 or draw_check == 1:
                    players_turn = 0
                    level += 1
                else:
                    players_turn += 1
            elif board[3] == "X" and board[5] == "X" and board[4] == "_":
                computer_input = 4
                board[computer_input] = "O"
                game_board(board)
                lose_check = win_lose_draw_check(1, board)
                draw_check = win_lose_draw_check(1, board)
                if lose_check == 1 or draw_check == 1:
                    players_turn = 0
                    level += 1
                else:
                    players_turn += 1
            elif board[4] == "X" and board[5] == "X" and board[3] == "_":
                computer_input = 3
                board[computer_input] = "O"
                game_board(board)
                lose_check = win_lose_draw_check(1, board)
                draw_check = win_lose_draw_check(1, board)
                if lose_check == 1 or draw_check == 1:
                    players_turn = 0
                    level += 1
                else:
                    players_turn += 1
            elif board[6] == "X" and board[7] == "X" and board[8] == "_":
                computer_input = 8
                board[computer_input] = "O"
                game_board(board)
                lose_check = win_lose_draw_check(1, board)
                draw_check = win_lose_draw_check(1, board)
                if lose_check == 1 or draw_check == 1:
                    players_turn = 0
                    level += 1
                else:
                    players_turn += 1
            elif board[6] == "X" and board[8] == "X" and board[7] == "_":
                computer_input = 7
                board[computer_input] = "O"
                game_board(board)
                lose_check = win_lose_draw_check(1, board)
                draw_check = win_lose_draw_check(1, board)
                if lose_check == 1 or draw_check == 1:
                    players_turn = 0
                    level += 1
                else:
                    players_turn += 1
            elif board[7] == "X" and board[8] == "X" and board[6] == "_":
                computer_input = 6
                board[computer_input] = "O"
                game_board(board)
                lose_check = win_lose_draw_check(1, board)
                draw_check = win_lose_draw_check(1, board)
                if lose_check == 1 or draw_check == 1:
                    players_turn = 0
                    level += 1
                else:
                    players_turn += 1
            elif board[0] == "X" and board[3] == "X" and board[6] == "_":
                computer_input = 6
                board[computer_input] = "O"
                game_board(board)
                lose_check = win_lose_draw_check(1, board)
                draw_check = win_lose_draw_check(1, board)
                if lose_check == 1 or draw_check == 1:
                    players_turn = 0
                    level += 1
                else:
                    players_turn += 1
            elif board[0] == "X" and board[6] == "X" and board[3] == "_":
                computer_input = 3
                board[computer_input] = "O"
                game_board(board)
                lose_check = win_lose_draw_check(1, board)
                draw_check = win_lose_draw_check(1, board)
                if lose_check == 1 or draw_check == 1:
                    players_turn = 0
                    level += 1
                else:
                    players_turn += 1
            elif board[3] == "X" and board[6] == "X" and board[0] == "_":
                computer_input = 0
                board[computer_input] = "O"
                game_board(board)
                lose_check = win_lose_draw_check(1, board)
                draw_check = win_lose_draw_check(1, board)
                if lose_check == 1 or draw_check == 1:
                    players_turn = 0
                    level += 1
                else:
                    players_turn += 1
            elif board[1] == "X" and board[4] == "X" and board[7] == "_":
                computer_input = 7
                board[computer_input] = "O"
                game_board(board)
                lose_check = win_lose_draw_check(1, board)
                draw_check = win_lose_draw_check(1, board)
                if lose_check == 1 or draw_check == 1:
                    players_turn = 0
                    level += 1
                else:
                    players_turn += 1
            elif board[1] == "X" and board[7] == "X" and board[4] == "_":
                computer_input = 4
                board[computer_input] = "O"
                game_board(board)
                lose_check = win_lose_draw_check(1, board)
                draw_check = win_lose_draw_check(1, board)
                if lose_check == 1 or draw_check == 1:
                    players_turn = 0
                    level += 1
                else:
                    players_turn += 1
            elif board[4] == "X" and board[7] == "X" and board[1] == "_":
                computer_input = 1
                board[computer_input] = "O"
                game_board(board)
                lose_check = win_lose_draw_check(1, board)
                draw_check = win_lose_draw_check(1, board)
                if lose_check == 1 or draw_check == 1:
                    players_turn = 0
                    level += 1
                else:
                    players_turn += 1
            elif board[2] == "X" and board[5] == "X" and board[8] == "_":
                computer_input = 8
                board[computer_input] = "O"
                game_board(board)
                lose_check = win_lose_draw_check(1, board)
                draw_check = win_lose_draw_check(1, board)
                if lose_check == 1 or draw_check == 1:
                    players_turn = 0
                    level += 1
                else:
                    players_turn += 1
            elif board[2] == "X" and board[8] == "X" and board[5] == "_":
                computer_input = 5
                board[computer_input] = "O"
                game_board(board)
                lose_check = win_lose_draw_check(1, board)
                draw_check = win_lose_draw_check(1, board)
                if lose_check == 1 or draw_check == 1:
                    players_turn = 0
                    level += 1
                else:
                    players_turn += 1
            elif board[5] == "X" and board[8] == "X" and board[2] == "_":
                computer_input = 2
                board[computer_input] = "O"
                game_board(board)
                lose_check = win_lose_draw_check(1, board)
                draw_check = win_lose_draw_check(1, board)
                if lose_check == 1 or draw_check == 1:
                    players_turn = 0
                    level += 1
                else:
                    players_turn += 1
            elif board[0] == "X" and board[4] == "X" and board[8] == "_":
                computer_input = 8
                board[computer_input] = "O"
                game_board(board)
                lose_check = win_lose_draw_check(1, board)
                draw_check = win_lose_draw_check(1, board)
                if lose_check == 1 or draw_check == 1:
                    players_turn = 0
                    level += 1
                else:
                    players_turn += 1
            elif board[0] == "X" and board[8] == "X" and board[4] == "_":
                computer_input = 4
                board[computer_input] = "O"
                game_board(board)
                lose_check = win_lose_draw_check(1, board)
                draw_check = win_lose_draw_check(1, board)
                if lose_check == 1 or draw_check == 1:
                    players_turn = 0
                    level += 1
                else:
                    players_turn += 1
            elif board[8] == "X" and board[4] == "X" and board[0] == "_":
                computer_input = 0
                board[computer_input] = "O"
                game_board(board)
                lose_check = win_lose_draw_check(1, board)
                draw_check = win_lose_draw_check(1, board)
                if lose_check == 1 or draw_check == 1:
                    players_turn = 0
                    level += 1
                else:
                    players_turn += 1
            elif board[6] == "X" and board[4] == "X" and board[2] == "_":
                computer_input = 2
                board[computer_input] = "O"
                game_board(board)
                lose_check = win_lose_draw_check(1, board)
                draw_check = win_lose_draw_check(1, board)
                if lose_check == 1 or draw_check == 1:
                    players_turn = 0
                    level += 1
                else:
                    players_turn += 1
            elif board[6] == "X" and board[2] == "X" and board[4] == "_":
                computer_input = 4
                board[computer_input] = "O"
                game_board(board)
                lose_check = win_lose_draw_check(1, board)
                draw_check = win_lose_draw_check(1, board)
                if lose_check == 1 or draw_check == 1:
                    players_turn = 0
                    level += 1
                else:
                    players_turn += 1
            elif board[2] == "X" and board[4] == "X" and board[6] == "_":
                computer_input = 6
                board[computer_input] = "O"
                game_board(board)
                lose_check = win_lose_draw_check(1, board)
                draw_check = win_lose_draw_check(1, board)
                if lose_check == 1 or draw_check == 1:
                    players_turn = 0
                    level += 1
                else:
                    players_turn += 1
            # computer picks middle spot if not already taken
            elif board[4] == "_":
                computer_input = 4
                board[computer_input] = "O"
                game_board(board)
                lose_check = win_lose_draw_check(1, board)
                draw_check = win_lose_draw_check(1, board)
                if lose_check == 1 or draw_check == 1:
                    players_turn = 0
                    level += 1
                else:
                    players_turn += 1
            # computer picks random spot if middle
            # is taken and there aren't 2 X's
            # in a row
            else:
                computer_input_check = 0
                while computer_input_check == 0:
                    computer_input = random.randrange(0, 9)
                    if board[computer_input] == "_":
                        board[computer_input] = "O"
                        computer_input_check = 1
                        game_board(board)
                        lose_check = win_lose_draw_check(1, board)
                        draw_check = win_lose_draw_check(1, board)
                        if lose_check == 1 or draw_check == 1:
                            players_turn = 0
                            level = 3
                        else:
                            players_turn += 1
                    else:
                        computer_input_check == 0
    while level == 3:
        # I needed to use 'for' in my project but could not find a way to
        # implement it more naturally :(
        for x in range(1):
            print("Thank you for playing!")
            level += 1


if __name__ == "__main__":
    main()
