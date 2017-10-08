'''
Alternative knightsPath() solution
    -Bret Farley
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
This is a more straightforward way of solving the knight's path algorithm, as it
does not require previous knowledge of chess or chess theory. It's based off of
some simple calculations that show that if a knight is unhindered by the border
it can legally move +/- 6, 10, 15, or 17 indicies on an 8x8 board. I wrote 4
functions for this:

    1) row() returns one index's row

    2) col() returns one index's 

    3) legalMoves() takes in 1 index and returns all the legal moves to certain
    indices based off of what row ad column it is in. It does this with 8 
    different if statments starting with the -17 location and works it's way 
    around the potential moves clockwise

    4) path() takes in the starting and target indices and then utilizes 
    legalMoves()to figure out how many moves it would take to get to the target
    position. I start with the starting position and make an array of all the
    moves that it can legally make and then I check to see if any of the returned 
    indices match the target, upon which the function prints a statement and 
    returns the amount of moves taken. If not I then do the same thing with the
    returned array until a match is found. The actual logic technically doesn't
    flow like that in case the starting and target point are the same index.

    
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
'''
def row(inx):
    row = inx / 8
    return row

def col(inx):
    col = inx %8
    return col

def legalMoves(inx):
    px = col(inx)
    py = row(inx)
    moves = []

    if py > 1 and px > 0:
        moves.append(inx - 17)
        # print "check1"
    if py > 1 and px < 7:
        moves.append(inx - 15)
        # print "check2"
    if py > 0 and px < 6:
        moves.append(inx - 6)
        # print "check3"
    if py < 7 and px < 6:
        moves.append(inx + 10)
        # print "check4"
    if py < 6 and px < 7:
        moves.append(inx + 17)
        # print "check5"
    if py < 6 and px > 0:
        moves.append(inx + 15)
        # print "check6"
    if py < 7 and px > 1:
        moves.append(inx + 6)
        # print "check7"
    if py > 0 and px > 1:
        moves.append(inx - 10)
        # print "check8"

    return moves

    


def path(inx, target):
    count = 0
    moves = [inx]
    run = True
    while run:
        temp = []
        for i in moves:
            if i == target:
                print "It takes {} moves to move from position {} to position {}".format(count, inx, target)
                run = False
                return count
        
        for i in moves:
            temp.extend(legalMoves(i))

        count += 1
        moves = temp

path(0, 63)            