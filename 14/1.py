import sys
grids = open(sys.argv[1]).read().split('\n\n')
grids = [grid.split('\n') for grid in grids]
for grid in grids:
    for i in range(len(grid[0])):
        # go through a column and split by #
        # if there is with 'o's (mandatory) and dots (optional)
        # count the number of 'o's and add index+1 of the last # to the result
        column = ''.join([row[i] for row in grid])
        splits = column.split('#')