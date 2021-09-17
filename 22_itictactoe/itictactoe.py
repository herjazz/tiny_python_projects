#!/usr/bin/env python3
"""
Title  : ITictactoe
Author : wrjt <wrjt@localhost>
Date   : 2021-09-15
Purpose: Play an interactive game of tictactoe
"""

import os
import sys


def main() -> None:
    """ Main Prog"""

    board = '.' * 9
    player = 'X'
    print('\n' + format_board(board))

    while True:
        move = input(f"Player {player}, what is your move? [q to quit]: ")
        if move == 'q':
            sys.exit("You lose, loser!")
        try:
            move = int(move)
            if move not in range(1, 10):
                raise ValueError
        except ValueError:
            print(f'Invalid cell "{move}", please use 1-9')
            continue
        else:
            if board[move - 1] in "XO":
                print(f'Cell "{move}" already taken.')
            else:
                board = board[:move - 1] + player + board[move:]
                print('\n' + format_board(board))
                if find_winner(board, player):
                    sys.exit(f"{player} has won!")
                if "." not in board:
                    sys.exit("All right, we'll call it a draw.")
                player = 'O' if player == 'X' else 'X'


def clear() -> None:
    """ Clear screen (depending on OS) """
    if os.name == 'nt':
        _ = os.system('cls')
    else:
        _ = os.system('clear')


def format_board(board: str) -> str:
    """ Print out current state of board """
    clear()
    cells = [str(i) if c == '.' else c for i, c in enumerate(board, start=1)]
    divider = "-------------"
    cells_tmpl = "| {} | {} | {} |"
    return '\n'.join([
        divider,
        cells_tmpl.format(*cells[:3]), divider,
        cells_tmpl.format(*cells[3:6]), divider,
        cells_tmpl.format(*cells[6:]), divider
    ])


def find_winner(board: str, player: str) -> bool:
    """ Return the winner """
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
                return True


# --------------------------------------------------
if __name__ == '__main__':
    main()
