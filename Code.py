import numpy as np

grid = [
    [5,6,0,0,0,0,4,7,0],
    [4,0,9,3,6,0,5,0,1],
    [3,0,8,5,1,0,2,0,0],
    [0,4,5,0,9,0,0,1,0],
    [0,3,2,7,5,1,0,0,0],
    [1,0,0,0,0,2,3,0,7],
    [0,1,0,9,0,5,7,0,0],
    [0,0,7,1,3,0,0,4,6],
    [0,0,4,0,0,0,0,0,0]
]

print(np.matrix(grid))

def solve(board) :
	find = findEmpty(board)
	if not find :
		return True
	else :
		row, column = find

	for n in range(1, 10) :
		if possible(board, row, column, n) :
			board[row][column] = n
			
			if solve(board) :
				return True
			
			board[row][column] = 0

	return False

def possible(board, y, x, n) :
	for x1 in range(0, 8) :
		if (board[y][x1] == n and x != x1) :
			return False
	for y1 in range(0, 8) :
		if board[y1][x] == n and y != y1:
			return False

	x0 = (x//3) * 3
	y0 = (y//3) * 3

	for i in range(x0, x0 + 3) :
		for j in range(y0, y0 + 3) :
			if( board[j][i] == n and j != y and x != i) :
				return False

	return True


def findEmpty(board) :
	for i in range(9) :
		for j in range(9) :
			if (board[i][j] == 0) :
				return (i, j)
	return None 



solve(grid)
print(np.matrix(grid))





