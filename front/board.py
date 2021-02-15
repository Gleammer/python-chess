import numpy as np

''' Variables set-up '''
matrix = np.zeros([8,8])

''' Function defines '''
def init_board(board):
    board[7][0] = board[7][7] = 5
    board[7][1] = board[7][6] = board[7][2] = board[7][5] = 3
    board[7][3] = 9
    board[7][4] = 100
    for i in range(8):
        board[0][i] = -board[7][i]
        board[1][i] = -1
        board[6][i] = 1

def get_context(board):
    sum = 0
    for i in range(8):
        for j in range(8):
            sum += board[i][j]
    return sum

def get_visual():
    print(matrix)
    print(pieces)

''' Set-up values '''
init_board(matrix)
pieces = np.array([['r', 'n', 'b', 'q', 'k', 'b', 'n', 'r'],
          ['p', 'p', 'p', 'p', 'p', 'p', 'p', 'p'],
          ['p', 'p', 'p', 'p', 'p', 'p', 'p', 'p'],
          ['p', 'p', 'p', 'p', 'p', 'p', 'p', 'p'],
          ['p', 'p', 'p', 'p', 'p', 'p', 'p', 'p'],
          ['p', 'p', 'p', 'p', 'p', 'p', 'p', 'p'],
          ['p', 'p', 'p', 'p', 'p', 'p', 'p', 'p'],
          ['r', 'n', 'b', 'q', 'k', 'b', 'n', 'r']])

''' Function calls '''
get_visual()
