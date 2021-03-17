import random, time, copy
WIDTH = 60
HEIGHT = 20
# Create a list of lists for the cells
nextCells = []
for x in range(WIDTH):
    column = [] #Create new column
    for y in range(HEIGHT):
        if random.randint(0, 1) == 0:
            column.append('#')
        else:
            column.append(' ')
    nextCells.append(column) #nextCells is a list of column lists.
while True:
    print('n\n\n\n\n')
    currentCells = copy.deepcopy(nextCells)
    #Print currentCells on screen
    for y in range(HEIGHT):
        for x in range(WIDTH):
            print(currentCells[x][y], end='') #Print the # or the sapce
        print() #Print a newline at the end of row
    #Calculate the next step's cell count based on current count
    for x in range(WIDTH):
        for y in range(HEIGHT):
            #Get neighboring coords
            #% WIDTH ensures leftCoord is always between 0 and WIDTH - 1
            leftCoord = (x - 1) % WIDTH
            rightCoord = (x + 1) % WIDTH
            aboveCoord = (y - 1) % HEIGHT
            belowCoord = (y + 1) % HEIGHT
            #Count living neighbors
            numNeighbors = 0
            if currentCells[leftCoord][aboveCoord] == '#':
                numNeighbors += 1
            if currentCells[x][aboveCoord] == '#':
                numNeighbors += 1
            if currentCells[rightCoord][aboveCoord] == '#':
                numNeighbors += 1
            if currentCells[leftCoord][y] == '#':
                numNeighbors += 1
            if currentCells[rightCoord][y] == '#':
                numNeighbors += 1
            if currentCells[leftCoord][belowCoord] == '#':
                numNeighbors += 1
            if currentCells[x][belowCoord] == '#':
                numNeighbors += 1
            if currentCells[rightCoord][belowCoord] == '#':
                numNeighbors += 1
            #Set Game of Life rules:
            if currentCells[x][y] == '#' and (numNeighbors == 2 or numNeighbors == 3) :
                nextCells[x][y] = '#'
            else:
                nextCells[x][y] = ' '
        time.sleep(1)
    
    

