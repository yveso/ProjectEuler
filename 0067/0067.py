"""
As we are just interessed in the sum of the route,
we don't care about routes at all.
We just traverse through the triangle and remember 
the "costs" to each point
"""

def build_triangle(path):
    lines = [line.rstrip("\n") for line in open(path)]
    t = []
    for line in lines:
        t.append([int(item) for item in line.split()])
    return t

triangle = build_triangle("triangle.txt")
costs = { (0, 0): triangle[0][0] }

def check_next_row_points_for(row, col):
    costs_for_current_location = costs[(row, col)]
    next_row = row + 1
    #check left option in new row
    costs_left = triangle[next_row][col] + costs_for_current_location
    #we could already visited this point (right option of prev. col)
    #let's check and see if we have higher costs now
    if (next_row, col) in costs.keys():
        if costs_left > costs[(next_row, col)]:
            #override value if so
            costs[(next_row, col)] = costs_left
    else:
        #if it's new save it
        #code is duplicated, but therefore more explicit
        costs[(next_row, col)] = costs_left
    #check right option and save it, as it's always new
    costs_right = triangle[next_row][col + 1] + costs_for_current_location
    costs[(next_row, col + 1)] = costs_right

for row_index in range(len(triangle) - 1):
    for col_index in range(len(triangle[row_index])):
        check_next_row_points_for(row_index, col_index)

#little bit hacky, but max value has to be in the last row
#as there aren't negative values in the triangle
answer = max(costs.values())
print(answer)