'''Instructions
Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:

Each row must contain the digits 1-9 without repetition.
Each column must contain the digits 1-9 without repetition.
Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.
Note:

A Sudoku board (partially filled) could be valid but is not necessarily solvable.
Only the filled cells need to be validated according to the mentioned rules.
'''
'''Examples
Input: board = 
[["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]
Output: true

Input: board = 
[["8","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]
Output: false
Explanation: Same as Example 1, except with the 5 in the top left corner being modified to 8. Since there are two 8's in the top left 3x3 sub-box, it is invalid.
'''
'''Thoughts
1. Get a list of all of the 3x3 values
2. Get a list of all of the column values
3. loop through all of the list and check for duplicates
'''

def valid(board:list[list]):
    column = list(map(list, zip(*board)))
    
    squares = []
    for i in range(0, len(board), 3):
        for j in range(0, len(board), 3):
            l = []
            l.extend(board[i][j:j+3])
            l.extend(board[i+1][j:j+3])
            l.extend(board[i+2][j:j+3])
            squares.append(l)
    
    for rule in range(len(board)):
        l1 = [num for num in board[rule] if num != '.']
        l2 = [num for num in column[rule] if num != '.']
        l3 = [num for num in squares[rule] if num != '.']
        if len(set(l1)) != len(l1) or len(set(l2)) != len(l2) or len(set(l3)) != len(l3):
            return False
    return True