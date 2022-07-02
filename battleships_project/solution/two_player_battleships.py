"""
Battleships two player game library for battleships assignment. 

Chami Lamelas

7/3/2021
"""

import battleships as bps
import battleships_constants as bpsc


def init_boards_and_ships(ships, size):
    # Initializes boards and ships given a board dimension size and a list of ships that will be available to the 2 players.

    # create boards for each player with dimension size
    player1_board = bps.create_board(size)
    player2_board = bps.create_board(size)

    # create copies of ships for each player (we make DEEP copies because remember we will be decrementing the values of
    # ships in order to efficiently track the ships' health on each of the players' boards in process_turn)
    player1_ships = bps.copy_list(ships)
    player2_ships = bps.copy_list(ships)
    return player1_board, player2_board, player1_ships, player2_ships


def prepare_boards(player1_board, player2_board, player1_ships, player2_ships):
    # Have player 1 place their ships onto the board, then player 2 having a player switch in the middle.

    bps.place_ships(player1_board, player1_ships)
    bps.next_player()
    bps.place_ships(player2_board, player2_ships)


def game_over(player1_ships, player2_ships):
    # Returns True if the game is over, False otherwise.

    player1_rem = 0
    player2_rem = 0
    # Add up health (parts of ships not hit) for player 1, player 2
    for i in range(len(player1_ships)):
        player1_rem += player1_ships[i]
        player2_rem += player2_ships[i]
    # If either is 0, that means all of the ships for one of the players has been destroyed
    return player1_rem == 0 or player2_rem == 0


def play_game(player1_board, player2_board, player1_ships, player2_ships):
    # Plays a 2-player game given player 1's board and ships, player 2's board and ships

    # Tracks whose turn it is - True if player 1 is shooting now, False if it's player 2
    on_player1 = True

    # Until the game is over
    while not game_over(player1_ships, player2_ships):

        # If player 1 is shooting, we will be seeing his progress on player 2's ships (b/c that's what
        # player 1 will be shooting at). Similarly, we will be using player 2's board. The board that player
        # 1 sees of their shooting history will be the display symbols corresponding to player 2's board.
        # The same idea applies for when player 2 is shooting.
        curr_ships = player2_ships if on_player1 else player1_ships
        curr_board = player2_board if on_player1 else player1_board
        bps.display_board(curr_board)

        # Since both boards are the same size, we can run a player_turn using either board's dimension
        pos = bps.player_turn(len(player1_board))

        # However, when player 1's turn is processed we will be working with player 2's board and ships
        # and the opposite if player 2's turn is being processed
        res = bps.process_turn(curr_board, curr_ships, pos)

        # If there was a miss, switch players (if we're on player 1, we'll go to player 2, if we're on player 2
        # we'll go to player 1)
        if res == bpsc.MISS_ID:
            print("You missed! Switching players..")
            bps.next_player()
            on_player1 = not on_player1

        # This isn't necessary, but for user I distinguish between hits and sinks (can thus make use of the IDs)
        elif res == bpsc.HIT_ID:
            print("You hit an enemy ship!")
        else:
            print("You sunk an enemy ship!")

    # If game ends, the current player is the winner (b/c their last turn would have been sinking the last part of
    # the last ship that hadn't been sunk of their opponent). Remember, turns only swap after a player misses.
    return 1 if on_player1 else 2


if __name__ == '__main__':
    # Initialize boards, ships and have players place their ships. Then, play the game with the prepared boards, ships.
    player1_board, player2_board, player1_ships, player2_ships = init_boards_and_ships([
                                                                                       2, 3], 5)
    prepare_boards(player1_board, player2_board, player1_ships, player2_ships)
    print(play_game(player1_board, player2_board, player1_ships, player2_ships))
