from test_runner import Tester, assert_eq
import battleships_test_utils as tutils
import battleships_constants as bpsc
import sys
from io import StringIO
import two_player_battleships as tpbps

t = Tester()

def game_over_fail():
    a = tpbps.game_over([1,0],[0,1])
    assert_eq(False, a)
t.create_test(game_over_fail)

def game_over_pass():
    a1 = tpbps.game_over([0,0],[1,0])
    assert_eq(True, a1)
    a2 = tpbps.game_over([1,0],[0,0])
    assert_eq(True, a2)
t.create_test(game_over_pass)

def init_boards_and_ships_test():
    p1_board, p2_board, p1_ships, p2_ships = tpbps.init_boards_and_ships([2,3],3)
    e = []
    for i in range(3):
        e.append([bpsc.UNSEEN_WATER]*3)
    assert_eq(e, p1_board, tutils.board_eq)
    assert_eq(e, p2_board, tutils.board_eq)
    assert_eq([2,3], p1_ships, tutils.ships_eq)
    assert_eq([2,3], p2_ships, tutils.ships_eq)
    p1_board[0][0] = 0
    assert_eq(bpsc.UNSEEN_WATER, p2_board[0][0])
    p1_ships[0] = 0
    assert_eq(2, p2_ships[0])
t.create_test(init_boards_and_ships_test)

def prepare_boards_test():
    p1_board, p2_board, p1_ships, p2_ships = tpbps.init_boards_and_ships([2,3,2,4],5)
    oldin = sys.stdin
    oldout = sys.stdout
    sys.stdout = StringIO()
    sys.stdin = StringIO("3 3 3 {n}\n1 1 0 {s}\n0 1 1 {e}\n2 2 2 {w}\nx\n3 4 0 {e}\n1 0 1 {s}\n0 0 3 {w}\n2 2 4 {n}\n".format(n=bpsc.NORTH,s=bpsc.SOUTH,e=bpsc.EAST,w=bpsc.WEST))
    tpbps.prepare_boards(p1_board, p2_board, p1_ships, p2_ships)
    sys.stdin = oldin
    sys.stdout = oldout
    e1 = [
        [bpsc.UNSEEN_WATER,bpsc.UNSEEN_WATER,bpsc.UNSEEN_WATER,3,bpsc.UNSEEN_WATER],
        [1,0,0,3,bpsc.UNSEEN_WATER],
        [1,2,2,3,bpsc.UNSEEN_WATER],
        [1,bpsc.UNSEEN_WATER,bpsc.UNSEEN_WATER,3,bpsc.UNSEEN_WATER],
        [bpsc.UNSEEN_WATER]*5
    ]
    e2 = [
        [bpsc.UNSEEN_WATER,1,0,0,bpsc.UNSEEN_WATER],
        [bpsc.UNSEEN_WATER,1,bpsc.UNSEEN_WATER,bpsc.UNSEEN_WATER,2],
        [bpsc.UNSEEN_WATER,1,bpsc.UNSEEN_WATER,bpsc.UNSEEN_WATER,2],
        [bpsc.UNSEEN_WATER]*5,
        [3,3,3,3,bpsc.UNSEEN_WATER]
    ]
    assert_eq(e1,p1_board,tutils.board_eq)
    assert_eq(e2,p2_board,tutils.board_eq)
    assert_eq([2,3,2,4],p1_ships,tutils.ships_eq)
    assert_eq([2,3,2,4],p2_ships,tutils.ships_eq)
t.create_test(prepare_boards_test)

def play_game_player1_wins_1_turn():
    p1_board = [
        [bpsc.UNSEEN_WATER,bpsc.UNSEEN_WATER,bpsc.UNSEEN_WATER,3,bpsc.UNSEEN_WATER],
        [1,0,0,3,bpsc.UNSEEN_WATER],
        [1,2,2,3,bpsc.UNSEEN_WATER],
        [1,bpsc.UNSEEN_WATER,bpsc.UNSEEN_WATER,3,bpsc.UNSEEN_WATER],
        [bpsc.UNSEEN_WATER]*5
    ]
    p2_board = [
        [bpsc.UNSEEN_WATER,1,0,0,bpsc.UNSEEN_WATER],
        [bpsc.UNSEEN_WATER,1,bpsc.UNSEEN_WATER,bpsc.UNSEEN_WATER,2],
        [bpsc.UNSEEN_WATER,1,bpsc.UNSEEN_WATER,bpsc.UNSEEN_WATER,2],
        [bpsc.UNSEEN_WATER]*5,
        [3]*4 + [bpsc.UNSEEN_WATER]
    ]
    p1_ships = [2,3,2,4]
    p2_ships = [2,3,2,4]
    oldin = sys.stdin
    oldout = sys.stdout
    buf = StringIO()
    sys.stdout = buf
    sys.stdin = StringIO("0 1\n1 1\n2 1\n0 2\n0 3\n1 4\n2 4\n4 0\n4 1\n4 2\n4 3\n")
    res = tpbps.play_game(p1_board, p2_board, p1_ships, p2_ships)
    sys.stdin = oldin
    sys.stdout = oldout
    e1 = [
        [bpsc.UNSEEN_WATER,bpsc.UNSEEN_WATER,bpsc.UNSEEN_WATER,3,bpsc.UNSEEN_WATER],
        [1,0,0,3,bpsc.UNSEEN_WATER],
        [1,2,2,3,bpsc.UNSEEN_WATER],
        [1,bpsc.UNSEEN_WATER,bpsc.UNSEEN_WATER,3,bpsc.UNSEEN_WATER],
        [bpsc.UNSEEN_WATER]*5
    ]
    e2 = [
        [bpsc.UNSEEN_WATER,bpsc.SEEN_SHIP,bpsc.SEEN_SHIP,bpsc.SEEN_SHIP,bpsc.UNSEEN_WATER],
        [bpsc.UNSEEN_WATER,bpsc.SEEN_SHIP,bpsc.UNSEEN_WATER,bpsc.UNSEEN_WATER,bpsc.SEEN_SHIP],
        [bpsc.UNSEEN_WATER,bpsc.SEEN_SHIP,bpsc.UNSEEN_WATER,bpsc.UNSEEN_WATER,bpsc.SEEN_SHIP],
        [bpsc.UNSEEN_WATER]*5,
        [bpsc.SEEN_SHIP,bpsc.SEEN_SHIP,bpsc.SEEN_SHIP,bpsc.SEEN_SHIP,bpsc.UNSEEN_WATER]
    ]
    assert_eq(e1,p1_board,tutils.board_eq)  
    assert_eq(e2,p2_board,tutils.board_eq)
    assert_eq([2,3,2,4],p1_ships,tutils.ships_eq)
    assert_eq([0]*4,p2_ships,tutils.ships_eq)
    assert_eq(1, res)
    board_prints = [
        "   |   |   |   |   \n---+---+---+---+---\n   |   |   |   |   \n---+---+---+---+---\n   |   |   |   |   \n---+---+---+---+---\n   |   |   |   |   \n---+---+---+---+---\n   |   |   |   |   \n",
        "   | {x} |   |   |   \n---+---+---+---+---\n   |   |   |   |   \n---+---+---+---+---\n   |   |   |   |   \n---+---+---+---+---\n   |   |   |   |   \n---+---+---+---+---\n   |   |   |   |   \n",
        "   | {x} |   |   |   \n---+---+---+---+---\n   | {x} |   |   |   \n---+---+---+---+---\n   |   |   |   |   \n---+---+---+---+---\n   |   |   |   |   \n---+---+---+---+---\n   |   |   |   |   \n",
        "   | {x} |   |   |   \n---+---+---+---+---\n   | {x} |   |   |   \n---+---+---+---+---\n   | {x} |   |   |   \n---+---+---+---+---\n   |   |   |   |   \n---+---+---+---+---\n   |   |   |   |   \n",
        "   | {x} | {x} |   |   \n---+---+---+---+---\n   | {x} |   |   |   \n---+---+---+---+---\n   | {x} |   |   |   \n---+---+---+---+---\n   |   |   |   |   \n---+---+---+---+---\n   |   |   |   |   \n",
        "   | {x} | {x} | {x} |   \n---+---+---+---+---\n   | {x} |   |   |   \n---+---+---+---+---\n   | {x} |   |   |   \n---+---+---+---+---\n   |   |   |   |   \n---+---+---+---+---\n   |   |   |   |   \n",
        "   | {x} | {x} | {x} |   \n---+---+---+---+---\n   | {x} |   |   | {x} \n---+---+---+---+---\n   | {x} |   |   | {x} \n---+---+---+---+---\n   |   |   |   |   \n---+---+---+---+---\n   |   |   |   |   \n",
        "   | {x} | {x} | {x} |   \n---+---+---+---+---\n   | {x} |   |   | {x} \n---+---+---+---+---\n   | {x} |   |   | {x} \n---+---+---+---+---\n   |   |   |   |   \n---+---+---+---+---\n {x} |   |   |   |   \n",
        "   | {x} | {x} | {x} |   \n---+---+---+---+---\n   | {x} |   |   | {x} \n---+---+---+---+---\n   | {x} |   |   | {x} \n---+---+---+---+---\n   |   |   |   |   \n---+---+---+---+---\n {x} | {x} |   |   |   \n",
        "   | {x} | {x} | {x} |   \n---+---+---+---+---\n   | {x} |   |   | {x} \n---+---+---+---+---\n   | {x} |   |   | {x} \n---+---+---+---+---\n   |   |   |   |   \n---+---+---+---+---\n {x} | {x} | {x} |   |   \n"
    ]
    board_prints = [bp.format(x=bpsc.HIT_MARKER) for bp in board_prints]
    assert_eq(True, tutils.check_strs(board_prints, buf.getvalue()))
t.create_test(play_game_player1_wins_1_turn)

def play_game_iterative():
    p1_board = [
        [bpsc.UNSEEN_WATER,bpsc.UNSEEN_WATER,bpsc.UNSEEN_WATER,3,bpsc.UNSEEN_WATER],
        [1,0,0,3,bpsc.UNSEEN_WATER],
        [1,2,2,3,bpsc.UNSEEN_WATER],
        [1,bpsc.UNSEEN_WATER,bpsc.UNSEEN_WATER,3,bpsc.UNSEEN_WATER],
        [bpsc.UNSEEN_WATER]*5
    ]
    p2_board = [
        [bpsc.UNSEEN_WATER,1,0,0,bpsc.UNSEEN_WATER],
        [bpsc.UNSEEN_WATER,1,bpsc.UNSEEN_WATER,bpsc.UNSEEN_WATER,2],
        [bpsc.UNSEEN_WATER,1,bpsc.UNSEEN_WATER,bpsc.UNSEEN_WATER,2],
        [bpsc.UNSEEN_WATER]*5,
        [3]*4 + [bpsc.UNSEEN_WATER]
    ]
    p1_ships = [2,3,2,4]
    p2_ships = [2,3,2,4]
    oldin = sys.stdin
    oldout = sys.stdout
    buf = StringIO()
    sys.stdout = buf
    sys.stdin = StringIO("0 0\nx\n4 4\nx\n0 1\n0 2\n0 3\n0 4\nx\n4 3\nx\n1 0\nx\n4 2\nx\n1 1\n1 2\nx\n4 1\nx\n1 3\nx\n4 0\nx\n1 4\n2 0\nx\n3 4\nx\n2 1\n2 2\nx\n3 3\n3 2\nx\n2 3\nx\n3 1\nx\n2 4\n3 0\nx\n3 0\n2 4\nx\n3 1\nx\n2 3\n2 2\n2 1\n2 0\n1 4\nx\n3 2\nx\n1 3\n1 2\n1 1\n1 0\n0 4\nx\n3 3\nx\n0 3\n")
    res = tpbps.play_game(p1_board, p2_board, p1_ships, p2_ships)
    sys.stdin = oldin
    sys.stdout = oldout
    e1 = [
        [bpsc.UNSEEN_WATER,bpsc.UNSEEN_WATER,bpsc.UNSEEN_WATER,bpsc.SEEN_SHIP,bpsc.SEEN_WATER],
        [bpsc.SEEN_SHIP,bpsc.SEEN_SHIP,bpsc.SEEN_SHIP,bpsc.SEEN_SHIP,bpsc.SEEN_WATER],
        [bpsc.SEEN_SHIP,bpsc.SEEN_SHIP,bpsc.SEEN_SHIP,bpsc.SEEN_SHIP,bpsc.SEEN_WATER],
        [bpsc.SEEN_SHIP,bpsc.SEEN_WATER,bpsc.SEEN_WATER,bpsc.SEEN_SHIP,bpsc.SEEN_WATER],
        [bpsc.SEEN_WATER]*5
    ]
    e2 = [
        [bpsc.SEEN_WATER,bpsc.SEEN_SHIP,bpsc.SEEN_SHIP,bpsc.SEEN_SHIP,bpsc.SEEN_WATER],
        [bpsc.SEEN_WATER,bpsc.SEEN_SHIP,bpsc.SEEN_WATER,bpsc.SEEN_WATER,bpsc.SEEN_SHIP],
        [bpsc.SEEN_WATER,bpsc.SEEN_SHIP,bpsc.SEEN_WATER,bpsc.SEEN_WATER,bpsc.SEEN_SHIP],
        [bpsc.SEEN_WATER,bpsc.SEEN_WATER,bpsc.SEEN_WATER,bpsc.SEEN_WATER,bpsc.UNSEEN_WATER],
        [3,3,3,3,bpsc.UNSEEN_WATER]
    ]
    assert_eq(e1,p1_board,tutils.board_eq)  
    assert_eq(e2,p2_board,tutils.board_eq)
    assert_eq([0]*4,p1_ships,tutils.ships_eq)
    assert_eq([0,0,0,4],p2_ships,tutils.ships_eq)
    assert_eq(2, res)
    board_prints = [
        "   |   |   |   |   \n---+---+---+---+---\n   |   |   |   |   \n---+---+---+---+---\n   |   |   |   |   \n---+---+---+---+---\n   |   |   |   |   \n---+---+---+---+---\n   |   |   |   |   \n",
        "   |   |   |   |   \n---+---+---+---+---\n   |   |   |   |   \n---+---+---+---+---\n   |   |   |   |   \n---+---+---+---+---\n   |   |   |   |   \n---+---+---+---+---\n   |   |   |   |   \n",
        " {o} |   |   |   |   \n---+---+---+---+---\n   |   |   |   |   \n---+---+---+---+---\n   |   |   |   |   \n---+---+---+---+---\n   |   |   |   |   \n---+---+---+---+---\n   |   |   |   |   \n",
        " {o} | {x} |   |   |   \n---+---+---+---+---\n   |   |   |   |   \n---+---+---+---+---\n   |   |   |   |   \n---+---+---+---+---\n   |   |   |   |   \n---+---+---+---+---\n   |   |   |   |   \n",
        " {o} | {x} | {x} |   |   \n---+---+---+---+---\n   |   |   |   |   \n---+---+---+---+---\n   |   |   |   |   \n---+---+---+---+---\n   |   |   |   |   \n---+---+---+---+---\n   |   |   |   |   \n",
        " {o} | {x} | {x} | {x} |   \n---+---+---+---+---\n   |   |   |   |   \n---+---+---+---+---\n   |   |   |   |   \n---+---+---+---+---\n   |   |   |   |   \n---+---+---+---+---\n   |   |   |   |   \n",
        "   |   |   |   |   \n---+---+---+---+---\n   |   |   |   |   \n---+---+---+---+---\n   |   |   |   |   \n---+---+---+---+---\n   |   |   |   |   \n---+---+---+---+---\n   |   |   |   | {o} \n",
        " {o} | {x} | {x} | {x} | {o} \n---+---+---+---+---\n   |   |   |   |   \n---+---+---+---+---\n   |   |   |   |   \n---+---+---+---+---\n   |   |   |   |   \n---+---+---+---+---\n   |   |   |   |   \n",
        "   |   |   |   |   \n---+---+---+---+---\n   |   |   |   |   \n---+---+---+---+---\n   |   |   |   |   \n---+---+---+---+---\n   |   |   |   |   \n---+---+---+---+---\n   |   |   | {o} | {o} \n",
        " {o} | {x} | {x} | {x} | {o} \n---+---+---+---+---\n {o} |   |   |   |   \n---+---+---+---+---\n   |   |   |   |   \n---+---+---+---+---\n   |   |   |   |   \n---+---+---+---+---\n   |   |   |   |   \n",
        " {o} | {x} | {x} | {x} | {o} \n---+---+---+---+---\n {o} | {x} |   |   |   \n---+---+---+---+---\n   |   |   |   |   \n---+---+---+---+---\n   |   |   |   |   \n---+---+---+---+---\n   |   |   |   |   \n",
        "   |   |   |   |   \n---+---+---+---+---\n   |   |   |   |   \n---+---+---+---+---\n   |   |   |   |   \n---+---+---+---+---\n   |   |   |   |   \n---+---+---+---+---\n   |   | {o} | {o} | {o} \n",
        " {o} | {x} | {x} | {x} | {o} \n---+---+---+---+---\n {o} | {x} | {o} |   |   \n---+---+---+---+---\n   |   |   |   |   \n---+---+---+---+---\n   |   |   |   |   \n---+---+---+---+---\n   |   |   |   |   \n",
        "   |   |   |   |   \n---+---+---+---+---\n   |   |   |   |   \n---+---+---+---+---\n   |   |   |   |   \n---+---+---+---+---\n   |   |   |   |   \n---+---+---+---+---\n   | {o} | {o} | {o} | {o} \n",
        " {o} | {x} | {x} | {x} | {o} \n---+---+---+---+---\n {o} | {x} | {o} | {o} |   \n---+---+---+---+---\n   |   |   |   |   \n---+---+---+---+---\n   |   |   |   |   \n---+---+---+---+---\n   |   |   |   |   \n",
        " {o} | {x} | {x} | {x} | {o} \n---+---+---+---+---\n {o} | {x} | {o} | {o} | {x} \n---+---+---+---+---\n   |   |   |   |   \n---+---+---+---+---\n   |   |   |   |   \n---+---+---+---+---\n   |   |   |   |   \n",
        "   |   |   |   |   \n---+---+---+---+---\n   |   |   |   |   \n---+---+---+---+---\n   |   |   |   |   \n---+---+---+---+---\n   |   |   |   |   \n---+---+---+---+---\n {o} | {o} | {o} | {o} | {o} \n",
        " {o} | {x} | {x} | {x} | {o} \n---+---+---+---+---\n {o} | {x} | {o} | {o} | {x} \n---+---+---+---+---\n {o} |   |   |   |   \n---+---+---+---+---\n   |   |   |   |   \n---+---+---+---+---\n   |   |   |   |   \n",
        " {o} | {x} | {x} | {x} | {o} \n---+---+---+---+---\n {o} | {x} | {o} | {o} | {x} \n---+---+---+---+---\n {o} | {x} |   |   |   \n---+---+---+---+---\n   |   |   |   |   \n---+---+---+---+---\n   |   |   |   |   \n",
        "   |   |   |   |   \n---+---+---+---+---\n   |   |   |   |   \n---+---+---+---+---\n   |   |   |   |   \n---+---+---+---+---\n   |   |   |   | {o} \n---+---+---+---+---\n {o} | {o} | {o} | {o} | {o} \n",
        "   |   |   |   |   \n---+---+---+---+---\n   |   |   |   |   \n---+---+---+---+---\n   |   |   |   |   \n---+---+---+---+---\n   |   |   | {x} | {o} \n---+---+---+---+---\n {o} | {o} | {o} | {o} | {o} \n",
        " {o} | {x} | {x} | {x} | {o} \n---+---+---+---+---\n {o} | {x} | {o} | {o} | {x} \n---+---+---+---+---\n {o} | {x} | {o} |   |   \n---+---+---+---+---\n   |   |   |   |   \n---+---+---+---+---\n   |   |   |   |   \n",
        "   |   |   |   |   \n---+---+---+---+---\n   |   |   |   |   \n---+---+---+---+---\n   |   |   |   |   \n---+---+---+---+---\n   |   | {o} | {x} | {o} \n---+---+---+---+---\n {o} | {o} | {o} | {o} | {o} \n",
        " {o} | {x} | {x} | {x} | {o} \n---+---+---+---+---\n {o} | {x} | {o} | {o} | {x} \n---+---+---+---+---\n {o} | {x} | {o} | {o} |   \n---+---+---+---+---\n   |   |   |   |   \n---+---+---+---+---\n   |   |   |   |   \n",
        " {o} | {x} | {x} | {x} | {o} \n---+---+---+---+---\n {o} | {x} | {o} | {o} | {x} \n---+---+---+---+---\n {o} | {x} | {o} | {o} | {x} \n---+---+---+---+---\n   |   |   |   |   \n---+---+---+---+---\n   |   |   |   |   \n",
        "   |   |   |   |   \n---+---+---+---+---\n   |   |   |   |   \n---+---+---+---+---\n   |   |   |   |   \n---+---+---+---+---\n   | {o} | {o} | {x} | {o} \n---+---+---+---+---\n {o} | {o} | {o} | {o} | {o} \n",
        "   |   |   |   |   \n---+---+---+---+---\n   |   |   |   |   \n---+---+---+---+---\n   |   |   |   |   \n---+---+---+---+---\n {x} | {o} | {o} | {x} | {o} \n---+---+---+---+---\n {o} | {o} | {o} | {o} | {o} \n",
        " {o} | {x} | {x} | {x} | {o} \n---+---+---+---+---\n {o} | {x} | {o} | {o} | {x} \n---+---+---+---+---\n {o} | {x} | {o} | {o} | {x} \n---+---+---+---+---\n {o} |   |   |   |   \n---+---+---+---+---\n   |   |   |   |   \n",
        "   |   |   |   |   \n---+---+---+---+---\n   |   |   |   |   \n---+---+---+---+---\n   |   |   |   | {o} \n---+---+---+---+---\n {x} | {o} | {o} | {x} | {o} \n---+---+---+---+---\n {o} | {o} | {o} | {o} | {o} \n",
        "   |   |   |   |   \n---+---+---+---+---\n   |   |   |   |   \n---+---+---+---+---\n   |   |   | {x} | {o} \n---+---+---+---+---\n {x} | {o} | {o} | {x} | {o} \n---+---+---+---+---\n {o} | {o} | {o} | {o} | {o} \n",
        "   |   |   |   |   \n---+---+---+---+---\n   |   |   |   |   \n---+---+---+---+---\n   |   | {x} | {x} | {o} \n---+---+---+---+---\n {x} | {o} | {o} | {x} | {o} \n---+---+---+---+---\n {o} | {o} | {o} | {o} | {o} \n",
        "   |   |   |   |   \n---+---+---+---+---\n   |   |   |   |   \n---+---+---+---+---\n   | {x} | {x} | {x} | {o} \n---+---+---+---+---\n {x} | {o} | {o} | {x} | {o} \n---+---+---+---+---\n {o} | {o} | {o} | {o} | {o} \n",
        "   |   |   |   |   \n---+---+---+---+---\n   |   |   |   |   \n---+---+---+---+---\n {x} | {x} | {x} | {x} | {o} \n---+---+---+---+---\n {x} | {o} | {o} | {x} | {o} \n---+---+---+---+---\n {o} | {o} | {o} | {o} | {o} \n",
        " {o} | {x} | {x} | {x} | {o} \n---+---+---+---+---\n {o} | {x} | {o} | {o} | {x} \n---+---+---+---+---\n {o} | {x} | {o} | {o} | {x} \n---+---+---+---+---\n {o} | {o} |   |   |   \n---+---+---+---+---\n   |   |   |   |   \n",
        "   |   |   |   |   \n---+---+---+---+---\n   |   |   |   | {o} \n---+---+---+---+---\n {x} | {x} | {x} | {x} | {o} \n---+---+---+---+---\n {x} | {o} | {o} | {x} | {o} \n---+---+---+---+---\n {o} | {o} | {o} | {o} | {o} \n",
        "   |   |   |   |   \n---+---+---+---+---\n   |   |   | {x} | {o} \n---+---+---+---+---\n {x} | {x} | {x} | {x} | {o} \n---+---+---+---+---\n {x} | {o} | {o} | {x} | {o} \n---+---+---+---+---\n {o} | {o} | {o} | {o} | {o} \n",
        "   |   |   |   |   \n---+---+---+---+---\n   |   | {x} | {x} | {o} \n---+---+---+---+---\n {x} | {x} | {x} | {x} | {o} \n---+---+---+---+---\n {x} | {o} | {o} | {x} | {o} \n---+---+---+---+---\n {o} | {o} | {o} | {o} | {o} \n",
        "   |   |   |   |   \n---+---+---+---+---\n   | {x} | {x} | {x} | {o} \n---+---+---+---+---\n {x} | {x} | {x} | {x} | {o} \n---+---+---+---+---\n {x} | {o} | {o} | {x} | {o} \n---+---+---+---+---\n {o} | {o} | {o} | {o} | {o} \n",
        "   |   |   |   |   \n---+---+---+---+---\n {x} | {x} | {x} | {x} | {o} \n---+---+---+---+---\n {x} | {x} | {x} | {x} | {o} \n---+---+---+---+---\n {x} | {o} | {o} | {x} | {o} \n---+---+---+---+---\n {o} | {o} | {o} | {o} | {o} \n",
        " {o} | {x} | {x} | {x} | {o} \n---+---+---+---+---\n {o} | {x} | {o} | {o} | {x} \n---+---+---+---+---\n {o} | {x} | {o} | {o} | {x} \n---+---+---+---+---\n {o} | {o} | {o} |   |   \n---+---+---+---+---\n   |   |   |   |   \n",
        "   |   |   |   | {o} \n---+---+---+---+---\n {x} | {x} | {x} | {x} | {o} \n---+---+---+---+---\n {x} | {x} | {x} | {x} | {o} \n---+---+---+---+---\n {x} | {o} | {o} | {x} | {o} \n---+---+---+---+---\n {o} | {o} | {o} | {o} | {o} \n"
    ]
    board_prints = [bp.format(x=bpsc.HIT_MARKER,o=bpsc.MISS_MARKER) for bp in board_prints]
    assert_eq(True, tutils.check_strs(board_prints, buf.getvalue()))
t.create_test(play_game_iterative)

t.run_all_tests()