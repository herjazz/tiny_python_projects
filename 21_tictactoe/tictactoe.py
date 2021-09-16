#!/usr/bin/env python3
"""
Title  : Tictactoe
Author : wrjt <wrjt@localhost>
Date   : 2021-09-15
Purpose: Emulate a game of tictactoe
"""

import argparse


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Tictactoe',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('-b',
                        '--board',
                        help='Current state of the board',
                        metavar='board',
                        type=str,
                        default='.........')

    parser.add_argument('-p',
                        '--player',
                        help='Player to move',
                        metavar='player',
                        type=str,
                        choices=["X", "O"])

    parser.add_argument('-c',
                        '--cell',
                        help='Number of the cell to be taken',
                        metavar='cell',
                        type=int,
                        choices=[1, 2, 3, 4, 5, 6, 7, 8, 9])

    args = parser.parse_args()

    if len(args.board) != 9:
        parser.error(f'--board "{args.board}" must be 9 characters of ., X, O')

    for char in args.board:
        if char not in ".XO":
            parser.error(
                f'--board "{args.board}" must be 9 characters of ., X, O')

    if (args.player and not args.cell) or (args.cell and not args.player):
        parser.error("Must provide both --player and --cell")

    if args.cell:
        if args.board[args.cell - 1] in "XO":
            parser.error(f'--cell "{args.cell}" already taken')

    return args


# --------------------------------------------------
def main():
    """ Main Prog"""

    args = get_args()
    board = args.board

    if args.cell:
        pos = args.cell
        board = board[:pos - 1] + args.player + board[pos:]

    winner = find_winner(board, 'O') or find_winner(board, 'X') or "No winner."

    print(format_board(board) + '\n' + winner)


def format_board(board: str) -> str:
    """ Print out current state of board """
    cells = [str(i + 1) if c == '.' else c for i, c in enumerate(board)]
    divider = "-------------"
    cells_tmpl = "| {} | {} | {} |"
    return '\n'.join([
        divider,
        cells_tmpl.format(*cells[:3]), divider,
        cells_tmpl.format(*cells[3:6]), divider,
        cells_tmpl.format(*cells[6:]), divider
    ])


def find_winner(board: str, player: str) -> str:
    """ Return True if winning combination """
    wins = [('PPP......'), ('...PPP...'), ('......PPP'), ('P..P..P..'),
            ('.P..P..P.'), ('..P..P..P'), ('P...P...P'), ('..P.P.P..')]
    board = ''.join([c.replace(c, '.') if c != player else c for c in board])
    for win in wins:
        matches = 0
        win = win.replace('P', player)
        for w, b in zip(win, board):
            if w == player and b == player:
                matches += 1
            if matches == 3:
                return f"{player} has won!"


# --------------------------------------------------
if __name__ == '__main__':
    main()
