def make_grid(path):
    grid = []
    for row in [line.rstrip("\n") for line in open(path)]:
        grid.append([int(x) for x in row.split()])
    return grid

def horizontal(grid, row, col, length):
    if col < (len(grid[row]) - length):
        return grid[row][col : col + length]
        
def vertical(grid, row, col, length):
    if row < (len(grid) - length):
        return [grid[row + i][col] for i in range(length)]

def diag_ul2lr(grid, row, col, length):
    if col < (len(grid[row]) - length) and row < (len(grid) - length):
        return [grid[row + i][col + i] for i in range(length)]

def diag_ll2ur(grid, row, col, length):
    if col < (len(grid[row]) - length) and row >= length - 1:
        return [grid[row -i][col + i] for i in range(length)]

def product(list):
    if list is not None:
        x = list[0]
        for i in list[1:]:
            x *= i
        return x
    else:
        return 0

grid = make_grid("grid.txt")
max_product = 0
length = 4

for row in range(len(grid)):
    for col in range(len(grid[row])):
        groups = [ 
            horizontal(grid, row, col, length),
            vertical(grid, row, col, length),
            diag_ul2lr(grid, row, col, length),
            diag_ll2ur(grid, row, col, length)
        ]
        for g in groups:
            p = product(g)
            if p > max_product:
                max_product = p

print(max_product)