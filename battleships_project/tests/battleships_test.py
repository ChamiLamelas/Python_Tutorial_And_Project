import battleships as bps
import battleships_test_utils as tutils
import battleships_constants as bpsc
import sys
from io import StringIO
from test_runner import Tester, assert_eq

t = Tester()

def filtered_print_test():
    l = [1,2,3]
    f = [True,False,True]
    old = sys.stdout
    buf = StringIO()
    sys.stdout = buf
    bps.filtered_print(l, f)
    sys.stdout = old
    assert_eq("[1,,3]", buf.getvalue().strip())
t.create_test(filtered_print_test)

def copy_list_test():
    s = [1,2]
    c = bps.copy_list(s)
    assert_eq([1,2],c,tutils.ships_eq)
    assert_eq([1,2],s,tutils.ships_eq)
    c[0] = 3
    assert_eq([3,2],c,tutils.ships_eq)
    assert_eq([1,2],s,tutils.ships_eq)
t.create_test(copy_list_test)

def create_board_test():
    a = bps.create_board(3)
    e = []
    for i in range(3):
        e.append([bpsc.UNSEEN_WATER]*3)
    assert_eq(e,a,tutils.board_eq)
t.create_test(create_board_test)

def seen_water_symbol_test():
    a = bps.get_display_symbol([[bpsc.SEEN_WATER]], (0,0))
    assert_eq(bpsc.MISS_MARKER, a)
t.create_test(seen_water_symbol_test)

def seen_ship_symbol_test():
    a = bps.get_display_symbol([[bpsc.SEEN_SHIP]], (0,0))
    assert_eq(bpsc.HIT_MARKER, a)
t.create_test(seen_ship_symbol_test)

def unseen_water_symbol_test():
    a = bps.get_display_symbol([[bpsc.UNSEEN_WATER]], (0,0))
    assert_eq(bpsc.UNSEEN_MARKER, a)
t.create_test(unseen_water_symbol_test)

def unseen_ship_symbol_test():
    a = bps.get_display_symbol([[0]], (0,0))
    assert_eq(bpsc.UNSEEN_MARKER, a)
t.create_test(unseen_ship_symbol_test)

def display_board_test():
    b = bps.create_board(3)
    b[0][0] = 0
    b[1][1] = bpsc.SEEN_SHIP
    b[2][2] = bpsc.SEEN_WATER
    old = sys.stdout
    buf = StringIO()
    sys.stdout = buf
    bps.display_board(b)
    sys.stdout = old
    e = " "+bpsc.UNSEEN_MARKER+" | "+bpsc.UNSEEN_MARKER+" | "+bpsc.UNSEEN_MARKER+" \n---+---+---\n "+bpsc.UNSEEN_MARKER+" | "+bpsc.HIT_MARKER+" | "+bpsc.UNSEEN_MARKER+" \n---+---+---\n "+bpsc.UNSEEN_MARKER+" | "+bpsc.UNSEEN_MARKER+" | "+bpsc.MISS_MARKER+" "
    assert_eq(e,tutils.trim_newlines(buf.getvalue()))
t.create_test(display_board_test)

def ship_at_pos_valid_test():
    b = bps.create_board(2)
    b[0][0] = 0
    b[1][1] = 1
    assert_eq(True, bps.ship_at_pos(b, (0,0)))
    assert_eq(True, bps.ship_at_pos(b, (1,1)))
t.create_test(ship_at_pos_valid_test)

def ship_at_pos_invalid_test():
    b = bps.create_board(2)
    assert_eq(False, bps.ship_at_pos(b, (0,0)))
t.create_test(ship_at_pos_invalid_test)

def place_ship_negative_x():
    board = bps.create_board(2)
    ships = [2, 3]
    a = bps.place_ship(board, ships, 0, (-1,0), bpsc.NORTH)
    assert_eq(False, a)
    assert_eq([[bpsc.UNSEEN_WATER]*2,[bpsc.UNSEEN_WATER]*2],board,tutils.board_eq)
    assert_eq([2,3],ships,tutils.ships_eq)
t.create_test(place_ship_negative_x)

def place_ship_negative_y():
    board = bps.create_board(2)
    ships = [2, 3]
    a = bps.place_ship(board, ships, 0, (0,-1), bpsc.NORTH)
    assert_eq(False, a)
    assert_eq([[bpsc.UNSEEN_WATER]*2,[bpsc.UNSEEN_WATER]*2],board,tutils.board_eq)
    assert_eq([2,3],ships,tutils.ships_eq)
t.create_test(place_ship_negative_y)

def place_ship_too_big_x():
    board = bps.create_board(2)
    ships = [2, 3]
    a = bps.place_ship(board, ships, 0, (2,0), bpsc.NORTH)
    assert_eq(False, a)
    assert_eq([[bpsc.UNSEEN_WATER]*2,[bpsc.UNSEEN_WATER]*2],board,tutils.board_eq)
    assert_eq([2,3],ships,tutils.ships_eq)
t.create_test(place_ship_too_big_x)

def place_ship_too_big_y():
    board = bps.create_board(2)
    ships = [2, 3]
    a = bps.place_ship(board, ships, 0, (0,2), bpsc.NORTH)
    assert_eq(False, a)
    assert_eq([[bpsc.UNSEEN_WATER]*2,[bpsc.UNSEEN_WATER]*2],board,tutils.board_eq)
    assert_eq([2,3],ships,tutils.ships_eq)
t.create_test(place_ship_too_big_y)

def place_ship_invalid_direc():
    board = bps.create_board(2)
    ships = [2, 3]
    a = bps.place_ship(board, ships, 0, (0,0), 'x')
    assert_eq(False, a)
    assert_eq([[bpsc.UNSEEN_WATER]*2,[bpsc.UNSEEN_WATER]*2],board,tutils.board_eq)
    assert_eq([2,3],ships,tutils.ships_eq)
t.create_test(place_ship_invalid_direc)

def place_ship_too_long_n():
    board = bps.create_board(2)
    ships = [2, 3]
    a = bps.place_ship(board, ships, 0, (0,0), bpsc.NORTH)
    assert_eq(False, a)
    assert_eq([[bpsc.UNSEEN_WATER]*2,[bpsc.UNSEEN_WATER]*2],board,tutils.board_eq)
    assert_eq([2,3],ships,tutils.ships_eq)
t.create_test(place_ship_too_long_n)

def place_ship_too_long_s():
    board = bps.create_board(2)
    ships = [2, 3]
    a = bps.place_ship(board, ships, 0, (1,0), bpsc.SOUTH)
    assert_eq(False, a)
    assert_eq([[bpsc.UNSEEN_WATER]*2,[bpsc.UNSEEN_WATER]*2],board,tutils.board_eq)
    assert_eq([2,3],ships,tutils.ships_eq)
t.create_test(place_ship_too_long_s)

def place_ship_too_long_e():
    board = bps.create_board(2)
    ships = [2, 3]
    a = bps.place_ship(board, ships, 0, (0,1), bpsc.EAST)
    assert_eq(False, a)
    assert_eq([[bpsc.UNSEEN_WATER]*2,[bpsc.UNSEEN_WATER]*2],board,tutils.board_eq)
    assert_eq([2,3],ships,tutils.ships_eq)
t.create_test(place_ship_too_long_e)

def place_ship_too_long_w():
    board = bps.create_board(2)
    ships = [2, 3]
    a = bps.place_ship(board, ships, 0, (0,0), bpsc.WEST)
    assert_eq(False, a)
    assert_eq([[bpsc.UNSEEN_WATER]*2,[bpsc.UNSEEN_WATER]*2],board,tutils.board_eq)
    assert_eq([2,3],ships,tutils.ships_eq)
t.create_test(place_ship_too_long_w)

def place_ship_on_ship():
    board = bps.create_board(2)
    board[0][0] = 0
    board[0][1] = 0
    ships = [2, 3]
    a = bps.place_ship(board, ships, 0, (0,0), bpsc.NORTH)
    assert_eq(False, a)
    assert_eq([[0,0],[bpsc.UNSEEN_WATER]*2],board,tutils.board_eq)
    assert_eq([2,3],ships,tutils.ships_eq)
t.create_test(place_ship_on_ship)

def place_ship_on_ship_n():
    board = bps.create_board(2)
    board[0][0] = 0
    board[0][1] = 0
    ships = [2, 3]
    a = bps.place_ship(board, ships, 0, (1,0), bpsc.NORTH)
    assert_eq(False, a)
    assert_eq([[0,0],[bpsc.UNSEEN_WATER]*2],board,tutils.board_eq)
    assert_eq([2,3],ships,tutils.ships_eq)
t.create_test(place_ship_on_ship_n)

def place_ship_on_ship_s():
    board = bps.create_board(2)
    board[1][0] = 0
    board[1][1] = 0
    ships = [2, 3]
    a = bps.place_ship(board, ships, 0, (0,1), bpsc.SOUTH)
    assert_eq(False, a)
    assert_eq([[bpsc.UNSEEN_WATER]*2,[0,0]],board,tutils.board_eq)
    assert_eq([2,3],ships,tutils.ships_eq)
t.create_test(place_ship_on_ship_s)

def place_ship_on_ship_e():
    board = bps.create_board(2)
    board[0][1] = 0
    board[1][1] = 0
    ships = [2, 3]
    a = bps.place_ship(board, ships, 0, (0,0), bpsc.EAST)
    assert_eq(False, a)
    assert_eq([[bpsc.UNSEEN_WATER,0],[bpsc.UNSEEN_WATER,0]],board,tutils.board_eq)
    assert_eq([2,3],ships,tutils.ships_eq)
t.create_test(place_ship_on_ship_e)

def place_ship_on_ship_w():
    board = bps.create_board(2)
    board[0][0] = 0
    board[1][0] = 0
    ships = [2, 3]
    a = bps.place_ship(board, ships, 0, (1,1), bpsc.WEST)
    assert_eq(False, a)
    assert_eq([[0,bpsc.UNSEEN_WATER],[0,bpsc.UNSEEN_WATER]],board,tutils.board_eq)
    assert_eq([2,3],ships,tutils.ships_eq)
t.create_test(place_ship_on_ship_w)

def place_ship_ok_n():
    board = bps.create_board(2)
    board[0][1] = 0
    board[1][1] = 0
    ships = [3, 2]
    a = bps.place_ship(board, ships, 1, (1,0), bpsc.NORTH)
    assert_eq(True, a)
    assert_eq([[1,0],[1,0]],board,tutils.board_eq)
    assert_eq([3,2],ships,tutils.ships_eq)
t.create_test(place_ship_ok_n)

def place_ship_ok_s():
    board = bps.create_board(2)
    board[0][1] = 0
    board[1][1] = 0
    ships = [3, 2]
    a = bps.place_ship(board, ships, 1, (0,0), bpsc.SOUTH)
    assert_eq(True, a)
    assert_eq([[1,0],[1,0]],board,tutils.board_eq)
    assert_eq([3,2],ships,tutils.ships_eq)
t.create_test(place_ship_ok_s)

def place_ship_ok_e():
    board = bps.create_board(2)
    board[0][0] = 0
    board[0][1] = 0
    ships = [3, 2]
    a = bps.place_ship(board, ships, 1, (1,0), bpsc.EAST)
    assert_eq(True, a)
    assert_eq([[0,0],[1,1]],board,tutils.board_eq)
    assert_eq([3,2],ships,tutils.ships_eq)
t.create_test(place_ship_ok_e)

def place_ship_ok_w():
    board = bps.create_board(2)
    board[0][0] = 0
    board[0][1] = 0
    ships = [3, 2]
    a = bps.place_ship(board, ships, 1, (1,1), bpsc.WEST)
    assert_eq(True, a)
    assert_eq([[0,0],[1,1]],board,tutils.board_eq)
    assert_eq([3,2],ships,tutils.ships_eq)
t.create_test(place_ship_ok_w)

def place_ships_all_ok():
    board = bps.create_board(4)
    ships = [2,3,2,4]
    oldin = sys.stdin
    oldout = sys.stdout
    buf = StringIO()
    sys.stdout = buf
    sys.stdin = StringIO("3 3 3 {n}\n1 1 0 {s}\n0 1 1 {e}\n2 2 2 {w}\n".format(n=bpsc.NORTH,s=bpsc.SOUTH,e=bpsc.EAST,w=bpsc.WEST))
    bps.place_ships(board, ships)
    sys.stdin = oldin
    sys.stdout = oldout
    e = [
        [bpsc.UNSEEN_WATER,bpsc.UNSEEN_WATER,bpsc.UNSEEN_WATER,3],
        [1,0,0,3],
        [1,2,2,3],
        [1,bpsc.UNSEEN_WATER,bpsc.UNSEEN_WATER,3]
    ]
    assert_eq(e,board,tutils.board_eq)
    assert_eq([2,3,2,4],ships,tutils.ships_eq)
    rem_prints = ["[2,3,2,4]", "[2,3,2,]", "[2,,2,]", "[,,2,]"]
    assert_eq(True, tutils.check_strs(rem_prints, buf.getvalue()))
t.create_test(place_ships_all_ok)

def place_ships_negative_ship_idx():
    board = bps.create_board(4)
    ships = [2,3,2,4]
    oldin = sys.stdin
    oldout = sys.stdout
    buf = StringIO()
    sys.stdout = buf
    sys.stdin = StringIO("3 3 3 {n}\n-1 1 0 {s}\n1 1 0 {s}\n0 1 1 {e}\n2 2 2 {w}\n".format(n=bpsc.NORTH,s=bpsc.SOUTH,e=bpsc.EAST,w=bpsc.WEST))
    bps.place_ships(board, ships)
    sys.stdin = oldin
    sys.stdout = oldout
    e = [
        [bpsc.UNSEEN_WATER,bpsc.UNSEEN_WATER,bpsc.UNSEEN_WATER,3],
        [1,0,0,3],
        [1,2,2,3],
        [1,bpsc.UNSEEN_WATER,bpsc.UNSEEN_WATER,3]
    ]
    assert_eq(e,board,tutils.board_eq)
    assert_eq([2,3,2,4],ships,tutils.ships_eq)
    rem_prints = ["[2,3,2,4]", "[2,3,2,]", "[2,3,2,]", "[2,,2,]", "[,,2,]"]
    assert_eq(True, tutils.check_strs(rem_prints, buf.getvalue()))
t.create_test(place_ships_negative_ship_idx)

def place_ships_too_big_ship_idx():
    board = bps.create_board(4)
    ships = [2,3,2,4]
    oldin = sys.stdin
    oldout = sys.stdout
    buf = StringIO()
    sys.stdout = buf
    sys.stdin = StringIO("3 3 3 {n}\n4 1 0 {s}\n1 1 0 {s}\n0 1 1 {e}\n2 2 2 {w}\n".format(n=bpsc.NORTH,s=bpsc.SOUTH,e=bpsc.EAST,w=bpsc.WEST))
    bps.place_ships(board, ships)
    sys.stdin = oldin
    sys.stdout = oldout
    e = [
        [bpsc.UNSEEN_WATER,bpsc.UNSEEN_WATER,bpsc.UNSEEN_WATER,3],
        [1,0,0,3],
        [1,2,2,3],
        [1,bpsc.UNSEEN_WATER,bpsc.UNSEEN_WATER,3]
    ]
    assert_eq(e,board,tutils.board_eq)
    assert_eq([2,3,2,4],ships,tutils.ships_eq)
    rem_prints = ["[2,3,2,4]", "[2,3,2,]", "[2,3,2,]", "[2,,2,]", "[,,2,]"]
    assert_eq(True, tutils.check_strs(rem_prints, buf.getvalue()))
t.create_test(place_ships_too_big_ship_idx)

def place_ships_too_long_all_direc():
    board = bps.create_board(4)
    ships = [2,3,2,4]
    oldin = sys.stdin
    oldout = sys.stdout
    buf = StringIO()
    sys.stdout = buf
    sys.stdin = StringIO("1 2 0 {s}\n1 1 0 {s}\n0 1 3 {e}\n0 1 1 {e}\n2 2 0 {w}\n2 2 2 {w}\n3 2 3 {n}\n3 3 3 {n}\n".format(n=bpsc.NORTH,s=bpsc.SOUTH,e=bpsc.EAST,w=bpsc.WEST))
    bps.place_ships(board, ships)
    sys.stdin = oldin
    sys.stdout = oldout
    e = [
        [bpsc.UNSEEN_WATER,bpsc.UNSEEN_WATER,bpsc.UNSEEN_WATER,3],
        [1,0,0,3],
        [1,2,2,3],
        [1,bpsc.UNSEEN_WATER,bpsc.UNSEEN_WATER,3]
    ]
    assert_eq(e,board,tutils.board_eq)
    assert_eq([2,3,2,4],ships,tutils.ships_eq)
    rem_prints = ["[2,3,2,4]","[2,3,2,4]","[2,,2,4]","[2,,2,4]","[,,2,4]","[,,2,4]","[,,,4]","[,,,4]"]
    assert_eq(True, tutils.check_strs(rem_prints, buf.getvalue()))
t.create_test(place_ships_too_long_all_direc)

def place_ships_try_placing_same():
    board = bps.create_board(4)
    ships = [2,3,2,4]
    oldin = sys.stdin
    oldout = sys.stdout
    buf = StringIO()
    sys.stdout = buf
    sys.stdin = StringIO("3 3 3 {n}\n3 3 0 {n}\n1 1 0 {s}\n1 1 1 {s}\n0 1 1 {e}\n0 0 1 {e}\n2 2 2 {w}\n".format(n=bpsc.NORTH,s=bpsc.SOUTH,e=bpsc.EAST,w=bpsc.WEST))
    bps.place_ships(board, ships)
    sys.stdin = oldin
    sys.stdout = oldout
    e = [
        [bpsc.UNSEEN_WATER,bpsc.UNSEEN_WATER,bpsc.UNSEEN_WATER,3],
        [1,0,0,3],
        [1,2,2,3],
        [1,bpsc.UNSEEN_WATER,bpsc.UNSEEN_WATER,3]
    ]
    assert_eq(e,board,tutils.board_eq)
    assert_eq([2,3,2,4],ships,tutils.ships_eq)
    rem_prints = ["[2,3,2,4]", "[2,3,2,]", "[2,3,2,]", "[2,,2,]", "[2,,2,]", "[,,2,]", "[,,2,]"]
    assert_eq(True, tutils.check_strs(rem_prints, buf.getvalue()))
t.create_test(place_ships_try_placing_same)

def place_ships_on_ship_all_direc():
    board = bps.create_board(4)
    ships = [2,3,2,4]
    oldin = sys.stdin
    oldout = sys.stdout
    buf = StringIO()
    sys.stdout = buf
    sys.stdin = StringIO("3 3 3 {n}\n1 1 1 {e}\n1 1 0 {s}\n0 1 1 {w}\n0 1 1 {e}\n2 2 2 {n}\n2 0 2 {s}\n2 2 2 {w}\n".format(n=bpsc.NORTH,s=bpsc.SOUTH,e=bpsc.EAST,w=bpsc.WEST))
    bps.place_ships(board, ships)
    sys.stdin = oldin
    sys.stdout = oldout
    e = [
        [bpsc.UNSEEN_WATER,bpsc.UNSEEN_WATER,bpsc.UNSEEN_WATER,3],
        [1,0,0,3],
        [1,2,2,3],
        [1,bpsc.UNSEEN_WATER,bpsc.UNSEEN_WATER,3]
    ]
    assert_eq(e,board,tutils.board_eq)
    assert_eq([2,3,2,4],ships,tutils.ships_eq)
    rem_prints = ["[2,3,2,4]", "[2,3,2,]", "[2,3,2,]", "[2,,2,]", "[2,,2,]", "[,,2,]", "[,,2,]", "[,,2,]"]
    assert_eq(True, tutils.check_strs(rem_prints, buf.getvalue()))
t.create_test(place_ships_on_ship_all_direc)

def player_turn_negative_x():
    oldin = sys.stdin
    oldout = sys.stdout
    sys.stdout = StringIO()
    sys.stdin = StringIO("-1 0\n1 0\n")
    pt = bps.player_turn(2)
    sys.stdin = oldin
    sys.stdout = oldout
    assert_eq(2, len(pt))
    ax = pt[0]
    ay = pt[1]
    assert_eq(1, ax)
    assert_eq(0, ay)
t.create_test(player_turn_negative_x)

def player_turn_negative_y():
    oldin = sys.stdin
    oldout = sys.stdout
    sys.stdout = StringIO()
    sys.stdin = StringIO("0 -1\n1 0\n")
    pt = bps.player_turn(2)
    sys.stdin = oldin
    sys.stdout = oldout
    assert_eq(2, len(pt))
    ax = pt[0]
    ay = pt[1]
    assert_eq(1, ax)
    assert_eq(0, ay)
t.create_test(player_turn_negative_y)

def player_turn_too_big_x():
    oldin = sys.stdin
    oldout = sys.stdout
    sys.stdout = StringIO()
    sys.stdin = StringIO("2 0\n1 0\n")
    pt = bps.player_turn(2)
    sys.stdin = oldin
    sys.stdout = oldout
    assert_eq(2, len(pt))
    ax = pt[0]
    ay = pt[1]
    assert_eq(1, ax)
    assert_eq(0, ay)
t.create_test(player_turn_too_big_x)

def player_turn_too_big_y():
    oldin = sys.stdin
    oldout = sys.stdout
    sys.stdout = StringIO()
    sys.stdin = StringIO("0 2\n1 0\n")
    pt = bps.player_turn(2)
    sys.stdin = oldin
    sys.stdout = oldout
    assert_eq(2, len(pt))
    ax = pt[0]
    ay = pt[1]
    assert_eq(1, ax)
    assert_eq(0, ay)
t.create_test(player_turn_too_big_y)

def process_turn_miss():
    board = bps.create_board(2)
    ships = [2]
    board[0][0] = 0
    board[1][0] = 0
    aid = bps.process_turn(board, ships, (1,1))
    assert_eq(bpsc.MISS_ID, aid)
    exp_board = [[0,bpsc.UNSEEN_WATER],[0,bpsc.SEEN_WATER]]
    assert_eq(exp_board,board,tutils.board_eq)
    assert_eq([2],ships,tutils.ships_eq)
t.create_test(process_turn_miss)

def process_turn_hit():
    board = bps.create_board(2)
    ships = [2]
    board[0][0] = 0
    board[1][0] = 0
    aid = bps.process_turn(board, ships, (0,0))
    assert_eq(bpsc.HIT_ID, aid)
    exp_board = [[bpsc.SEEN_SHIP,bpsc.UNSEEN_WATER],[0,bpsc.UNSEEN_WATER]]
    assert_eq(exp_board,board,tutils.board_eq)
    assert_eq([1],ships,tutils.ships_eq)
t.create_test(process_turn_hit)

def process_turn_sunk():
    board = bps.create_board(2)
    ships = [2]
    board[0][0] = 0
    board[1][0] = 0
    bps.process_turn(board, ships, (0,0))
    aid = bps.process_turn(board, ships, (1,0))
    assert_eq(bpsc.SUNK_ID, aid)
    exp_board = [[bpsc.SEEN_SHIP,bpsc.UNSEEN_WATER],[bpsc.SEEN_SHIP,bpsc.UNSEEN_WATER]]
    assert_eq(exp_board,board,tutils.board_eq)
    assert_eq([0],ships,tutils.ships_eq)
t.create_test(process_turn_sunk)

def next_player_test():
    oldin = sys.stdin
    oldout = sys.stdout
    sys.stdout = StringIO("")
    sys.stdin = StringIO("x\ny\n")
    bps.next_player()
    nxt = input("")
    sys.stdin = oldin
    sys.stdout = oldout
    assert_eq("y",nxt)
t.create_test(next_player_test)

t.run_all_tests()








