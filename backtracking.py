##### BACKTRACKING

# copy and paste the sudoku here
puzzleToSolve = [
    [0, 0, 0, 0, 0, 4, 6, 7, 0],
    [0, 0, 9, 2, 0, 0, 8, 0, 1],
    [0, 0, 7, 6, 1, 3, 0, 4, 9],
    [0, 5, 0, 1, 0, 0, 2, 8, 4],
    [0, 1, 0, 0, 0, 0, 3, 9, 6],
    [4, 9, 6, 8, 0, 0, 0, 5, 0],
    [3, 0, 0, 0, 6, 1, 0, 2, 0],
    [0, 8, 5, 4, 0, 0, 0, 6, 0],
    [9, 0, 0, 0, 7, 8, 0, 0, 0]
]

# draw the puzzle
def draw(puzzle):
    for r in range(len(puzzle)):
        if r == 0 or r == 3 or r == 6:
            print("+-------+-------+-------+")
        for c in range(len(puzzle[r])):
            if c == 0 or c == 3 or c ==6:
                print("| ", end = "")
            if puzzle[r][c] != 0:
                print(puzzle[r][c], end = " ")
            else:
                print(end = "  ")
            if c == 8:
                print("|")
    print("+-------+-------+-------+")

def solve(puzzle):
    # find empty cell location
    empty_cell = find_empty(puzzle)
    # if there is no empty cell left then its solved
    if not empty_cell:
        return True
    # assign empty cell location list to row and col
    else:
        row, col = empty_cell

    # try digits 1 to 9
    for i in range(1,10):
        # if promising then assign the i to empty cell
        if promising(puzzle, i, (row, col)):
            puzzle[row][col] = i
            # reccursive function, finishing the solution, return true if success
            if solve(puzzle):
                return True
            # failed solution, reset and try again
            puzzle[row][col] = 0
    # trigger backtrack
    return False
  
# find empty cell
def find_empty(puzzle):
    for r in range(len(puzzle)):
        for c in range(len(puzzle[0])):
            if puzzle[r][c] == 0:
                # (row, col)
                return (r, c)  

    return None

# validation check (Promising or Nonpromising)
def promising(puzzle, num, pos):
    # check row
    for i in range(len(puzzle[0])):
        if puzzle[pos[0]][i] == num and pos[1] != i:
            return False
    # check column
    for i in range(len(puzzle)):
        if puzzle[i][pos[1]] == num and pos[0] != i:
            return False
    # check 3x3 box
    puzzlex_x = pos[1] // 3
    puzzlex_y = pos[0] // 3

    for i in range(puzzlex_y*3, puzzlex_y*3 + 3):
        for j in range(puzzlex_x * 3, puzzlex_x*3 + 3):
            if puzzle[i][j] == num and (i,j) != pos:
                return False

    return True

print("--------BACKTRACKING--------")
print("Sudoku Problem : ")
draw(puzzleToSolve)

# execution time measure
from timeit import default_timer as timer
start = timer()
solve(puzzleToSolve)
end = timer()

# print solved sudoku
print("\nSudoku Solution : ")
draw(puzzleToSolve)

print("Execution time: ", end - start)
