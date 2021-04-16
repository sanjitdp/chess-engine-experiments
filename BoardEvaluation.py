import chess


def board_evaluation(board):
    if board.is_checkmate():
        if board.turn:
            return -999999
        else:
            return 999999

    if board.is_stalemate():
        return 0

    if board.is_insufficient_material():
        return 0

    w_pawns = board.fen().count("P")
    b_pawns = board.fen().count("p")

    w_rooks = board.fen().count("R")
    b_rooks = board.fen().count("r")

    w_queens = board.fen().count("Q")
    b_queens = board.fen().count("q")

    w_bishops = board.fen().count("B")
    b_bishops = board.fen().count("b")

    w_knights = board.fen().count("N")
    b_knights = board.fen().count("n")

    material_score = 900 * (w_queens - b_queens) + 500 * (w_rooks - b_rooks) + 315 * (w_knights - b_knights) + 325 * \
                     (w_bishops - b_bishops) + 1 * (w_pawns - b_pawns)

    pawn_bonus = 0
    pawn_table = [0, 0, 0, 0, 0, 0, 0, 0,
                  50, 50, 50, 50, 50, 50, 50, 50,
                  10, 10, 20, 30, 30, 20, 10, 10,
                  5, 5, 10, 25, 25, 10, 5, 5,
                  0, 0, 0, 20, 20, 0, 0, 0,
                  5, -5, -10, 0, 0, -10, -5, 5,
                  5, 10, 10, -20, -20, 10, 10, 5,
                  0, 0, 0, 0, 0, 0, 0, 0]
    for pawn in board.pieces(chess.PAWN, chess.WHITE):
        pawn_bonus += pawn_table[chess.square_mirror(pawn)]
    for pawn in board.pieces(chess.PAWN, chess.BLACK):
        pawn_bonus -= pawn_table[chess.square_mirror(pawn)]

    knight_bonus = 0
    knight_table = [-50, -40, -30, -30, -30, -30, -40, -50,
                    -40, -20, 0, 0, 0, 0, -20, -40,
                    -30, 0, 10, 15, 15, 10, 0, -30,
                    -30, 5, 15, 20, 20, 15, 5, -30,
                    -30, 0, 15, 20, 20, 15, 0, -30,
                    -30, 5, 10, 15, 15, 10, 5, -30,
                    -40, -20, 0, 5, 5, 0, -20, -40,
                    -50, -40, -30, -30, -30, -30, -40, -50]
    for knight in board.pieces(chess.KNIGHT, chess.WHITE):
        knight_bonus += knight_table[chess.square_mirror(knight)]
    for knight in board.pieces(chess.KNIGHT, chess.BLACK):
        knight_bonus -= knight_table[chess.square_mirror(knight)]

    bishop_bonus = 0
    bishop_table = [-20, -10, -10, -10, -10, -10, -10, -20,
                    -10, 0, 0, 0, 0, 0, 0, -10,
                    -10, 0, 5, 10, 10, 5, 0, -10,
                    -10, 5, 5, 10, 10, 5, 5, -10,
                    -10, 0, 10, 10, 10, 10, 0, -10,
                    -10, 10, 10, 10, 10, 10, 10, -10,
                    -10, 5, 0, 0, 0, 0, 5, -10,
                    -20, -10, -10, -10, -10, -10, -10, -20]
    for bishop in board.pieces(chess.BISHOP, chess.WHITE):
        bishop_bonus += bishop_table[chess.square_mirror(bishop)]
    for bishop in board.pieces(chess.BISHOP, chess.BLACK):
        bishop_bonus -= bishop_table[chess.square_mirror(bishop)]

    # Other bonuses yet to come

    total_score = material_score + pawn_bonus + knight_bonus + bishop_bonus  # plus other bonuses

    return total_score
