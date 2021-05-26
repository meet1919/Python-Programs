board = {'1': '', '2': '', '3': '',
         '4': '', '5': '', '6': '',
         '7': '', '8': '', '9': ''}

def printboard(tictac):
    print(tictac['1'], '|', tictac['2'], '|', tictac['3'])
    print('-+--+-')
    print(tictac['4'], '|', tictac['5'], '|', tictac['6'])
    print('-+--+-')
    print(tictac['7'], '|', tictac['8'], '|', tictac['9'])

turn = 'X'
for i in range(9):
    printboard(board)
    print("Turn for ", turn, "Please play your move : ")
    move = input()
    board[move] = turn
    if turn == "X":
        turn = "O"
    else:
        turn = "X"

printboard(board)





