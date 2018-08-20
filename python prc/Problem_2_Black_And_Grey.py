# returns the factors (as an ArrayList of integers) of the parameter n
# and this needs to return the list in descending order, hence the direction of the loops */
def getFactors(n):

    factors = [] # list of factors to be returned

    i = n
    while (i >= n ** 0.5): # only test up to the square root of the number because that will contain exactly half of the factors, excluding the square root (increases speed)
        if n % i == 0: factors.append(i) # if the looping variable is a factor of the number, add it to the factors list
        i -= 1

    size = len(factors) # size of the factors

    # add the other half of the factors of the number
    for i in range(size - 1, -1, -1): # for every factor in the factors list
        if (factors[i] != n ** 0.5): # only add the corresponding factor if the factor is not the square root of the number (the corresponding factor is itself - a duplicate)
            factors.append(int(n / factors[i])) # add the corresponding factor (the number divided by this factor) to the list

    return factors;

list = []

# read in the file to list
with open('C:\\Users\\Mike\\Desktop\\problem_2_black_and_grey_DATA21.txt') as f:
    for line in f:
        list.append(line.split('\n')[0])

index = 0

while index < len(list):

    # generate this data set in file (data sets come in increments of six lines)
    dataSet = []
    for i in range(index, index + 6):
        dataSet.append(list[i])
    index += 6
    
    # do stuff with data set
    n = (int)(dataSet[0])
    dataSet.remove(dataSet[0]) # don't need it anymore

    # find largest row and column in any of the six tiles
    maxRow = 0
    maxCol = 0
    for s in dataSet:
        rowAndCol = s.split() # split by whitespace. array has two elements: row and column
        row = (int)(rowAndCol[0])
        col = (int)(rowAndCol[1])
        
        # if this row is larger than the previous largest row, this row is the new largest row
        if row > maxRow: maxRow = row
        if col > maxCol: maxCol = col

    # board and transformed board matrices: are used to perform transformations throughout the stages
    # the dimensions are reduced to the maximum row and column values. the board won't need to be any
    # larger than that because no tiles on the board outside of this range will be tested (calculated above)
    board = [[0 for x in range(maxCol)] for x in range(maxRow)]
    transformed = [[0 for x in range(maxCol)] for x in range(maxRow)]
    
    factors = getFactors(n) # factors of the board dimensions (not reduced board)
    
    for factor in factors: # for every factor
        
        gridDimensions = n / factor # the square dimensions of the grids inside the larger board
        numberOfGrids = factor # the number of grids per side inside the larger board
        
        # make the checkerboards for each factor
        for i in range(0, numberOfGrids): # for every grid in each row
            for j in range(0, numberOfGrids): # for every grid in each column

                # colour each grid going row by row
                # i and j increment each grid
                # k and l increment each tile in each grid
                # start at the beginning of a grid (i * gridDimensions) and go until the end of the grid is reached (i * gridDimensions + gridDimensions)
                # the + gridDimensions would mean that it's iterating over a new grid
                # k < maxRow just makes sure that it's iterating within the reduced board array
                k = (int)(i * gridDimensions)
                while k < i * gridDimensions + gridDimensions and k < maxRow:
                    l = (int)(j * gridDimensions)
                    while l < j * gridDimensions + gridDimensions and l < maxCol:
                        # if one of the row and column is even and one is odd, the grid is grey (if the checkerboard has the top left grid being black)
                        if (i+j)%2 == 1:
                            board[k][l] = 0 # grey tile
                        else:
                            board[k][l] = 1 # black tile
                        l += 1
                    k += 1
        
        # add matrices (board matrix, which is the factored checkerboard, and transformed matrix, which is the last transformed board by adding, but will become the new transformed board)
        # I call it adding the matrices, but it's really just putting them together and getting the resultant matrix
        for i in range(0, maxRow):
            for j in range(0, maxCol):
                
                # this is like an XOR operation: if either one is black, but not both, the result is black; otherwise (both the same), the result is grey.
                if transformed[i][j] == board[i][j]: # if both squares are the same colour
                    transformed[i][j] = 0 # turns grey
                else: # different colours
                    transformed[i][j] = 1 # turns black
                    
                # Another way of doing is using the actual XOR operator:
                #if transformed[i][j] ^ board[i][j] == 1: # use XOR operator to test if the tiles are not the same colour (one of them is black, but not both; or the same thing with grey)
                #    transformed[i][j] = 1 # turns black                       
                #else: # same colour; failed the XOR test
                #    transformed[i][j] = 0 # turns grey

    result = ""
    for i in range(0, len(dataSet)): # for every tile to be looked at in the data set
        row = (int)(dataSet[i].split()[0]) # split the row and column string for the tile by whitespace and the first element will be the row
        col = (int)(dataSet[i].split()[1]) # second element is the column
        
        # find the tiles that the data set requests to be looked at
        # and remember to subtract 1 from the array index because arrays start indexing at 0, but the data set starts at 1
        if transformed[row-1][col-1] == 0:
            result += "G" # grey
        else:
            result += "B" # black
            
    print(result) # print the result of this data set
