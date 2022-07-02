"""
Battleships utilities library for battleships assignment. 

Chami Lamelas

7/3/2021
"""

import battleships_constants as bpsc


def copy_list(ls):
    # Returns a deep copy of list ls

    # add each element of ls into a new list and return that list
    copy = []
    for e in ls:
        copy.append(e)
    return copy


def create_board(size):
    # Returns a 2D list of size lists that each have length size. The elements will be the starting state of a board
    # before the game has started - UNSEEN_WATER

    # board will be our 2D list, add size lists of size UNSEEN_WATERs (these are the rows)
    board = []
    for i in range(size):
        board.append([bpsc.UNSEEN_WATER]*size)
    return board


def get_display_symbol(board, pos):
    # Returns a string symbol that should be displayed to the player shooting at board corresponding to row, column tuple pos
    # It will be based on the player's history of shooting at this board which is represented by the numerical values stored
    # in the elements of board

    # If player has seen a ship at this position, return HIT_MARKER
    # For the player to have seen a ship, that means they hit it in the past
    if board[pos[0]][pos[1]] == bpsc.SEEN_SHIP:
        return bpsc.HIT_MARKER

    # If player has seen water at this position, return MISS_MARKER
    # For the player to have seen water, that means they hit water (i.e. a miss) in the past
    elif board[pos[0]][pos[1]] == bpsc.SEEN_WATER:
        return bpsc.MISS_MARKER

    # Otherwise, return UNSEEN_MARKER, this means a player hasn't fired at this position and has not discovered whether
    # there is a ship here or water here
    else:
        return bpsc.UNSEEN_MARKER


def display_board(board):
    # Prints a board as it would be shown to the player shooting at it (making use of get_display_symbol)
    # Note that there are many ways to implement this function

    print("")
    # for each row of the board
    for i in range(len(board)):

        # for each column in the row
        for j in range(len(board)):

            # print the display symbol corresponding to this position surrounded by spaces
            print(" " + get_display_symbol(board, (i, j)) + " ", end="")

            # other than the last column, print a | following the symbol and spaces
            if j < len(board) - 1:
                print("|", end="")

        # if we aren't in the last row
        if i < len(board) - 1:

            # move to the next line (note end settings above to "")
            print("")

            # for each column, print --- (this will go underneath the 2 spaces and a symbol printed above)
            for j in range(len(board)):
                print("---", end="")

                # other than the last column, print a + following the symbol and spaces (this will go under | above)
                if j < len(board) - 1:
                    print("+", end="")

            # move to next line so that column prints are correct
            print("")
    print("")


def ship_at_pos(board, pos):
    # Returns bool whether there is a ship at pos in board assuming that player has not fired at pos on board

    # Based on assumption, we know board[pos[0]][pos[1]] != SEEN_SHIP != SEEN_WATER
    # That leaves board[pos[0]][pos[1]] = UNSEEN_WATER and board[pos[0]][pos[1]] >= 0 for an unseen ship
    # Hence, we return True when board[pos[0]][pos[1]] >= 0 and False otherwise
    return board[pos[0]][pos[1]] >= 0


def place_ship(board, ships, ship_id, pos, direc):
    # Tries to place ships[ship_id] on board at (row,column) tuple pos and direction direc
    # Return True if placement could be completed and False otherwise

    # If placement position is off the board, return False (can't place)
    if pos[0] < 0 or pos[0] >= len(board) or pos[1] < 0 or pos[1] >= len(board):
        return False

    # If pointing north, ship will go from (pos[0],pos[1]) to (pos[0]-ships[ship_id]+1,pos[1])
    # This is b/c going north means going in negative rows for ships[ship_id] positions
    if direc == bpsc.NORTH:

        # Check that the end of the ship isn't < 0 (i.e. the ship fits on the board)
        ship_end = pos[0] - ships[ship_id] + 1
        if ship_end < 0:
            return False

        # Once we know whole ship fits, make sure that a ship hasn't been placed along any position that
        # the new ship will be placed onto
        for i in range(pos[0], ship_end - 1, -1):
            if ship_at_pos(board, (i, pos[1])):
                return False

        # we know ALL ship positions are empty and on the board, fill the positions the board will go on with the ship_id
        # emphasis on ALL because we check ALL of the positions before placing any "part" of the ship
        for i in range(pos[0], ship_end - 1, -1):
            board[i][pos[1]] = ship_id

    # If pointing south, ship will go from (pos[0],pos[1]) to (pos[0]+ships[ship_id]-1,pos[1])
    # This is b/c going south means going in positive rows for ships[ship_id] positions
    # Here, the ship being on the board means making sure its within the no. of rows on the board
    # Other steps are similar to above
    elif direc == bpsc.SOUTH:
        ship_end = pos[0] + ships[ship_id] - 1
        if ship_end >= len(board):
            return False
        for i in range(pos[0], ship_end + 1):
            if ship_at_pos(board, (i, pos[1])):
                return False
        for i in range(pos[0], ship_end + 1):
            board[i][pos[1]] = ship_id

    # If pointing east, ship will go from (pos[0],pos[1]) to (pos[0],pos[1]+ships[ship_id]-1)
    # This is b/c going east means going in positive columns for ships[ship_id] positions
    # Here, the ship being on the board means making sure its within the no. of columns on the board
    # Other steps are similar to above
    elif direc == bpsc.EAST:
        ship_end = pos[1] + ships[ship_id] - 1
        if ship_end >= len(board):
            return False
        for i in range(pos[1], ship_end + 1):
            if ship_at_pos(board, (pos[0], i)):
                return False
        for i in range(pos[1], ship_end + 1):
            board[pos[0]][i] = ship_id

    # If pointing west, ship will go from (pos[0],pos[1] to (pos[0],pos[1]-ships[ship_id]+1))
    # This is b/c going west means going in negative columns for ships[ship_id] positions
    # Here, the ship being on the board means making sure the end isn't < 0
    # Other steps are similar to above
    elif direc == bpsc.WEST:
        ship_end = pos[1] - ships[ship_id] + 1
        if ship_end < 0:
            return False
        for i in range(pos[1], ship_end - 1, -1):
            if ship_at_pos(board, (pos[0], i)):
                return False
        for i in range(pos[1], ship_end - 1, -1):
            board[pos[0]][i] = ship_id

    # Otherwise, invalid direction
    else:
        return False

    # If we've reached this point, one of the directions reached the final loop which places a ship -> successful placement
    return True


def filtered_print(ls, filter):
    # Prints only the elements of ls that have been marked with True in filter.
    # Can assume len(ls) == len(filter)

    # Print [ at the start (later, will print ] at the end)
    print("[", end="")
    for i in range(len(ls)):

        # If we want to include ls[i], print it
        if filter[i]:
            print(ls[i], end="")
        # Otherwise, nothing is printed

        # If we haven't reached the last list element, print a ,
        if i < len(ls) - 1:
            print(",", end="")
    print("]")


def place_ships(board, ships):
    # Places all the ships in ships on board using user inputs of form <id> <row> <column> <direction>.
    # Prints are done throughout to keep user updated.

    # Will keep iterating till we have 0 ships left to place
    ships_left = len(ships)

    # Keep bool list of which ships have been placed (False) and not placed (True) - can use filtered_print
    unplaced_ships = [True]*len(ships)

    while ships_left > 0:
        # This print is required, you could add additional prints here with information on the size of the board,
        # how inputs need to be formatted, etc.
        filtered_print(ships, unplaced_ships)

        # prompt for position, split on spaces to get the 4 components
        pos_in = input("Position? ")
        pos_in = pos_in.split(" ")

        # ID will be first posotion
        ship_id = int(pos_in[0])

        # Make sure that the ID is valid and that ship hasn't been placed yet
        if ship_id >= 0 and ship_id < len(ships) and unplaced_ships[ship_id]:

            # Get row (2nd position), column (3rd position), direction (4th position)
            row = int(pos_in[1])
            col = int(pos_in[2])
            direc = pos_in[3]

            # Try to place the ship with this information
            res = place_ship(board, ships, ship_id, (row, col), direc)

            # If was successful, mark that it was placed in bool list and that 1 less ship is left to placed
            if res:
                unplaced_ships[ship_id] = False
                ships_left -= 1


def next_player():
    # Prompts user for input.

    # I add a bunch of newlines with the hope of one player not seeing the other's board - but it isn't perfect)
    input("%sPress enter to continue" % ("\n"*20))


def player_turn(size):
    # Executes a player turn with a board of dimension size. That is, it waits for player to enter a valid (row,column) tuple
    # for them to fire at.

    # Initialize, row column to < 0 so while loop is entered
    row = -1
    col = -1

    # (row,col) invalid if either < 0 or either are >= dimension size
    while row < 0 or row >= size or col < 0 or col >= size:

        # Get input and split it (row is 1st position, column is 2nd position)
        uin = input("Enter coordinates: ")
        uin = uin.split(" ")
        row = int(uin[0])
        col = int(uin[1])

    # Return valid row, column once we've got it
    return (row, col)


def process_turn(board, ships, pos):
    # Processes a position indicating a player move as returned by player_turn as to whether it is a hit, miss, or sink.
    # Since pos came from player_turn, we may assume that is valid

    # If ship at pos on board (this will either be a hit or sink).
    if ship_at_pos(board, pos):

        # Get ship id of ship at this position and use it to decrease health in ships (i.e. how much ship hasn't been hit)
        ship_id = board[pos[0]][pos[1]]
        ships[ship_id] -= 1

        # Will return SUNK_ID if hit resulted in 0 health, otherwise just say it was HIT_ID
        out_id = bpsc.SUNK_ID if ships[ship_id] == 0 else bpsc.HIT_ID

        # Mark on the board the position has been seen as a ship, return correct ID
        board[pos[0]][pos[1]] = bpsc.SEEN_SHIP
        return out_id

    # If ship isn't at pos on board, all we say is that the water (i.e. no ship) has now been seen (by the player firing at
    # board) in board. Then return MISS_ID
    else:
        board[pos[0]][pos[1]] = bpsc.SEEN_WATER
        return bpsc.MISS_ID
