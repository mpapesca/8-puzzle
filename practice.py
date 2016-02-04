import time


# Global variables
boardpieces = [-1] * 9
globalPiecesInfo = []
openList = []
closedList = []
LEFT = -1
RIGHT = 1
UP = -3
DOWN = 3
nodes = []
nodeindex = 0
testedlayouts = []



# NODEINDEX = None
# parentnode = None


class Node:
    id = None
    parent = None
    children = []
    layout = []
    moves = [LEFT, UP, RIGHT, DOWN]
    pieces = []
    previous_move = None


class pieceInfo():
    value = None
    position = None
    distance = None
    x_coor = None
    y_coor = None


def calculatedistance(value, position):
    if value == 0:
        if position == 0:
            distance = 0
        elif [1, 3].count(position) > 0:
            distance = 1
        elif [2, 4, 6].count(position) > 0:
            distance = 2
        elif [5, 7].count(position) > 0:
            distance = 3
        elif [8].count(position) > 0:
            distance = 4
    elif value == 1:
        if position == 1:
            distance = 0
        elif [0, 2, 4].count(position) > 0:
            distance = 1
        elif [3, 5, 7].count(position) > 0:
            distance = 2
        elif [6, 8].count(position) > 0:
            distance = 3
    elif value == 2:
        if position == 2:
            distance = 0
        elif [1, 5].count(position) > 0:
            distance = 1
        elif [0, 4, 8].count(position) > 0:
            distance = 2
        elif [3, 7].count(position) > 0:
            distance = 3
        elif [6].count(position) > 0:
            distance = 4
    elif value == 3:
        if position == 3:
            distance = 0
        elif [0, 4, 6].count(position) > 0:
            distance = 1
        elif [1, 5, 7].count(position) > 0:
            distance = 2
        elif [2, 8].count(position) > 0:
            distance = 3
    elif value == 4:
        if position == 4:
            distance = 0
        elif [1, 2, 3, 5, 6, 7, 8].count(position) > 0:
            distance = 1
    elif value == 5:
        if position == 5:
            distance = 0
        elif [2, 4, 8].count(position) > 0:
            distance = 1
        elif [1, 3, 7].count(position) > 0:
            distance = 2
        elif [0, 6].count(position) > 0:
            distance = 3
    elif value == 6:
        if position == 6:
            distance = 0
        elif [3, 7].count(position) > 0:
            distance = 1
        elif [0, 4, 8].count(position) > 0:
            distance = 2
        elif [1, 5].count(position) > 0:
            distance = 3
        elif [2].count(position) > 0:
            distance = 4
    elif value == 7:
        if position == 7:
            distance = 0
        elif [4, 6, 8].count(position) > 0:
            distance = 1
        elif [1, 3, 5].count(position) > 0:
            distance = 2
        elif [0, 2].count(position) > 0:
            distance = 3
    elif value == 8:
        if position == 8:
            distance = 0
        elif [5, 7].count(position) > 0:
            distance = 1
        elif [2, 4, 6].count(position) > 0:
            distance = 2
        elif [1, 3].count(position) > 0:
            distance = 3
        elif [0].count(position) > 0:
            distance = 4

    return distance


# End of calculatedistance()

def calculatexcoor(i):
    if [0, 3, 6].count(i) > 0:
        return 0
    elif [1, 4, 7].count(i) > 0:
        return 1
    elif [2, 5, 8].count(i) > 0:
        return 2


# End of calculatexcoor()


def calculateycoor(i):
    if [0, 1, 2].count(i) > 0:
        return 2
    elif [3, 4, 5].count(i) > 0:
        return 1
    elif [6, 7, 8].count(i) > 0:
        return 0


# End of calculateycoor()


def resetpieceinfo(layout):
    global globalPiecesInfo
    for num in range(0, 9):
        piece = layout[num]
        globalPiecesInfo[piece].position = num
        globalPiecesInfo[piece].distance = calculatedistance(piece, num)
        globalPiecesInfo[piece].x_coor = calculatexcoor(num)
        globalPiecesInfo[piece].y_coor = calculateycoor(num)


# End of resetpieceinfo()


def displayboard():
    global boardpieces
    display_pieces = boardpieces[:]

    for index, boardPiece in enumerate(boardpieces):

        if boardPiece == -1 or boardPiece == 0:
            display_pieces[index] = ' '
        else:
            display_pieces[index] = str(boardPiece)

    print "-------------"
    print "| %s | %s | %s |" % (display_pieces[0], display_pieces[1], display_pieces[2])#, openList
    print "-------------"
    print "| %s | %s | %s |" % (display_pieces[3], display_pieces[4], display_pieces[5])#, closedList
    print "-------------"
    print "| %s | %s | %s |" % (display_pieces[6], display_pieces[7], display_pieces[8])
    print "-------------"


# End of displayboard()


def startprogram():
    global globalPiecesInfo
    for num in range(0, 9):
        piece = pieceInfo()
        piece.value = num
        globalPiecesInfo.append(piece)

    print '\nWelcome to the 8 Puzzle Solver by Michael Papesca!'
    print '\nPlease enter the digits 1 through 8 to fill the board and 0 for the space.'
    displayboard()


# End of startprogram()


def receiveboardpieces():
    global boardpieces, globalPiecesInfo
    i = 0
    while i < 9:
        try:
            value_entered = int(raw_input("Enter value then press enter: "))
        except ValueError:
            print "You did not enter a number."
        else:
            if value_entered > 8 or value_entered < 0:
                print "The number you entered is out of the range."
            else:
                if boardpieces.count(value_entered) > 0:
                    print "The number you enter has already been used."
                else:
                    boardpieces[i] = value_entered
                    # globalPiecesInfo[value_entered].value = value_entered
                    # globalPiecesInfo[value_entered].position = i
                    # globalPiecesInfo[value_entered].distance = calculatedistance(value_entered, i)
                    # globalPiecesInfo[value_entered].x_coor = calculatexcoor(i)
                    # globalPiecesInfo[value_entered].y_coor = calculateycoor(i)
                    i += 1
                    displayboard()
    resetpieceinfo(boardpieces)


# End of receiveboardpieces()


def verifymove(current_position, direction):
    if [0, 3, 6].count(current_position) == 1 and direction == LEFT:
        return -1
    elif [0, 1, 2].count(current_position) == 1 and direction == UP:
        return -1
    elif [2, 5, 8].count(current_position) == 1 and direction == RIGHT:
        return -1
    elif [6, 7, 8].count(current_position) == 1 and direction == DOWN:
        return -1
    else:
        return current_position + direction


# End of verifymove()


def moveblankspace(direction):
    global boardpieces
    current_position = boardpieces.index(0)
    next_position = verifymove(current_position, direction)
    if next_position != -1:
        switched_piece = boardpieces[next_position]
        boardpieces[next_position] = 0
        boardpieces[current_position] = switched_piece
        # displayboard()
        time.sleep(1)
        return next_position  # Return piece that was switched with blank space.
    else:
    #     time.sleep(0)
        return -1


# End of moveblankspace


def checksuccess():
    global boardpieces, nodeindex, nodes
    if boardpieces == [0, 1, 2, 3, 4, 5, 6, 7, 8]:
        displayboard()
        return 1
    elif nodeindex % 100 == 0 and nodeindex != 0:
        # for num in range(0,nodeindex):
        #     print nodes[num].parent, " -> ", nodes[num].id
        #     boardpieces = nodes[num].layout[:]
        displayboard()
    return 0


# End of checksuccess()


def scanpreviouslayouts():
    global boardpieces
    currentlayout = "%d%d%d%d%d%d%d%d%d" % (boardpieces[0], boardpieces[1], boardpieces[2], boardpieces[3], boardpieces[4], boardpieces[5], boardpieces[6], boardpieces[7], boardpieces[8])
    for index in range(0, len(testedlayouts)):
        if currentlayout == testedlayouts[index]:
            return 0
    testedlayouts.append(currentlayout)
    return 1



def solve():

    global boardpieces, globalPiecesInfo, openList, closedList, nodes, nodeindex
    if checksuccess():
        return 1

    firstnode = Node()
    firstnode.id = nodeindex
    nodeindex += 1
    firstnode.layout = boardpieces[:]
    firstnode.pieces = globalPiecesInfo[:]
    nodes.append(firstnode)
    openList.append(firstnode.id)

    for item in openList:
        parentnode = item
        for direction in nodes[item].moves:
            boardpieces = nodes[parentnode].layout[:]
            move = moveblankspace(direction)
            newlayout = scanpreviouslayouts()
            if move != -1 and newlayout:
                child = Node()
                child.id = nodeindex
                nodeindex += 1
                child.parent = parentnode
                child.layout = boardpieces[:]
                nodes.append(child)
                openList.append(child.id)
        closedList.append(item)
        # openList.remove(parentnode)
        if checksuccess():
            return 1
