#!/usr/bin/env python3


def find_up(grid, row, col):

    if (row - 3) < 0:
        return 0
    
    tmp_str = ""
    for i in range(4):
        tmp_str += grid[row - i][col]
    
    if tmp_str == "XMAS":
        return 1
    
    return 0


def find_down(grid, row, col, row_max):
    
    if (row + 3) >= row_max:
        return 0
    
    tmp_str = ""
    for i in range(4):
        tmp_str += grid[row + i][col]

    if tmp_str == "XMAS":
        return 1

    return 0

def find_left(grid, row, col):
    
    if (col - 3) < 0:
        return 0
    
    tmp_str = ""
    for j in range(4):
        tmp_str += grid[row][col - j]

    if tmp_str == "XMAS":
        return 1

    return 0

def find_right(grid, row, col, col_max):
    if (col + 3) >= col_max:
        return 0
    
    tmp_str = ""
    for j in range(4):
        tmp_str += grid[row][col + j]

    if tmp_str == "XMAS":
        return 1
    
    return 0

def find_diag(grid, row, col, row_max, col_max):
    
    sum = 0
    if (row - 3) >= 0 and (col - 3) >= 0:
        tmp_str = ""
        for i in range(4):
            tmp_str += grid[row - i][col - i]
        
        if tmp_str == "XMAS":
            sum += 1
    
    if (row - 3) >= 0 and (col + 3) < col_max:
        tmp_str = ""
        for i in range(4):
            tmp_str += grid[row - i][col + i]
        
        if tmp_str == "XMAS":
            sum += 1
   
    if (row + 3) < row_max and (col - 3) >= 0:
        tmp_str = ""
        for i in range(4):
            tmp_str += grid[row + i][col - i]

        if tmp_str == "XMAS":
            sum += 1
    
    if (row + 3) < row_max and (col + 3) < col_max:
        tmp_str = ""
        for i in range(4):
            tmp_str += grid[row + i][col +i]
        
        if tmp_str == "XMAS":
            sum += 1
    
    return sum 





def find_xmas(grid:list[list[str]]):
    rows = len(grid)
    cols = len(grid[0])
    
    sum = 0

    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 'X':
                sum += find_up(grid, i, j)
                sum += find_down(grid, i, j, rows)
                sum += find_left(grid, i, j)
                sum += find_right(grid,i,j,cols)
                sum += find_diag(grid,i,j,rows,cols)
                
    
    return sum


def find_x_mas(grid:list[list[str]]):
    rows = len(grid)
    cols = len(grid[0])

    sum = 0
    key = ["M","S"]
    for i in range(1, rows - 1):
        for j in range(1, cols - 1):
            if grid[i][j] == 'A':
                set_1 = set([grid[i - 1][j-1],grid[i+1][j+1]])
                set_2 =set([grid[i-1][j+1],grid[i+1][j-1]])
                
                if set_1 == set(key) and set_2 == set(key):
                    sum += 1
    return sum



if __name__ == "__main__":

    grid = []
    with open("input.txt", 'r') as fd:
        for line in fd:
            row = []
            for ch in line:
                if ch != '\n':
                    row.append(ch)
            grid.append(row)
    
    ans =find_xmas(grid)
    print("Total number of XMAS: {}".format(ans))
    part2_ans = find_x_mas(grid)
    print("Total number of X-MAS: {}".format(part2_ans))

