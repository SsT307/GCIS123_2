#This function just creates a 9x9 2D list, using list comprehension, then returns the new lsit.
def make_board():
    
    #Why didn't we use i for i? Because it is being incremented and it will fill the table with values. By using " we are keeping empty values.
    actualBoard = [[" " for i in range(3)] for i in range(3)]
    return actualBoard


#Function does simple printing, takes the board as input and prints the rows.
def print_board(board):
    for row in board:
        print(row)

#This function simply makes a move, takes board and symbol for input. Symbol refers to "X" or "O"
def make_move(board,symbol):
    row = int(input("Enter Row!\n"))-1
    column = int(input("Enter Column!\n"))-1

    #Directly access the value and modifies it with the desired symbol.
    board[row][column] = symbol
    print_board(board)


#Main function, where we create a board, print, then allow for the user to attempt to play the game.
def main():
    myFirstBoard=make_board()

    print_board(myFirstBoard)

    #So we can simulate multiple turns, I decided that using even/odd distribution can easily allow for each turn to take place,
    #One turn being X (started with), and the other being O.
    for i in range(9):
        if i%2==0:
            make_move(myFirstBoard,"X")
        else:
            make_move(myFirstBoard,"O")

    print("Enjoy the game!")

main()
