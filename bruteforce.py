#### BRUTE FORCE

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

def str_to_puzzle(s):
    puzzleSolution = []
    for i in range(len(s)):  
        if i % 9 == 0:
            temp = []
            for j in s[i:i+9]:
                temp.append(int(j))
            puzzleSolution.append(temp)
    return puzzleSolution

# calidation check
def validation(i, j):
    # check row
    if i//9 == j//9:
        return True
    # check column
    if i%9 == j%9:
        return True
    # check same block
    if ((i//9)//3 == (j//9)//3) & ((i%9)//3 == (j%9)//3):
        return True
    return False

def sudoku_brute_force(s):
    # find empty cell
    i = s.find('0')

    # excluding the cell that already has a number
    cannotuse = {s[j] for j in range(len(s)) if validation(i,j)}
    every_possible_values = {str(i) for i in range(10)} - cannotuse

    # brute force
    for val in every_possible_values:
        s = s[0:i] + val + s[i+1:]
        sudoku_brute_force(s)
        if s.find('0') == -1:
            draw(str_to_puzzle(s))

s = ''.join(map(str,[''.join(map(str, i)) for i in puzzleToSolve]))

print("--------BRUTE FORCE--------")
print("Sudoku Problem: ")
draw(puzzleToSolve)
print("\nSudoku Solution: ")

# execution time measure
from timeit import default_timer as timer
start = timer()
sudoku_brute_force(s)
end = timer()

print("Execution time: ", end - start)
