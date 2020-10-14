import math
import random
import numpy as np

def is_valid_square(pt, n):
    """Checks if pt is a valid square in the sliding tile puzzle of size n."""
    return (pt[0] >= 0) and (pt[0] < n) and (pt[1] >= 0) and (pt[1] < n)

def empty_pos(puzzle):
    """Get the position of the empty square."""
    for i in range(puzzle.shape[0]):
        for j in range(puzzle.shape[1]):
            if puzzle[i, j] == 0:
                return (i, j)

def make_move(puzzle, pos):
    """Moves the tile at position pos to the empty square (no change if the move is invalid)"""
    puzzle_new = np.copy(puzzle)
    empty = empty_pos(puzzle)
    if ((abs(empty[0] - pos[0]) == 1) and (empty[1] == pos[1])) or ((abs(empty[1] - pos[1]) == 1) and (empty[0] == pos[0])):
        puzzle_new[empty[0], empty[1]] = puzzle[pos[0], pos[1]]
        puzzle_new[pos[0], pos[1]] = 0
    return puzzle_new

def init_solved_puzzle(n):
    """Creates a solved initial puzzle of size n"""
    return np.reshape(np.arange(n**2), [n, n])

def generate_move_list(empty, n):
    """Create list of horizontal and vertical moves (positions of tiles that can be moved to the empty square)"""
    candidate_moves = [(empty[0]-1, empty[1]), (empty[0]+1, empty[1]), (empty[0], empty[1]-1), (empty[0], empty[1]+1)]
    return [x for x in candidate_moves if is_valid_square(x, n)]

def init_scrambled_puzzle(n, m):
    """Creates a scrambled puzzle of size n by making m moves"""
    puzzle = init_solved_puzzle(n)
    for i in range(m):
        empty = empty_pos(puzzle)
        move_list = generate_move_list(empty, n)
        # Select move at random and carry it out
        move = random.sample(move_list, 1)
        move = move[0]
        puzzle = make_move(puzzle, move)
    return puzzle

def hash_puzzle(puzzle):
    """Get puzzle unique identifier"""
    MOD = 387421297
    res = 0
    nm = (puzzle.shape[0] * puzzle.shape[1]) % MOD
    to_multiply = 1

    for i in range(puzzle.shape[0]):
        for j in range(puzzle.shape[1]):
            res = (res + (puzzle[i, j] * to_multiply) % MOD) % MOD
            to_multiply = (to_multiply * nm) % MOD
    return res

def is_solved(puzzle):
    """Checks whether the puzzle is solved or not"""
    counter = 0
    for i in range(puzzle.shape[0]):
        for j in range(puzzle.shape[1]):
            if puzzle[i, j] != counter:
                return False
            counter += 1
    return True

def read_integers():
    """Reads space separated integers from user input"""
    return [int(x) for x in input().split(' ')]

def read_puzzle():
    """Reads puzzle from user input"""
    n = int(input("Input number of rows: "))
    puzzle = []
    print("Input puzzle:")
    for i in range(n):
        row = read_integers()
        puzzle.append(row)
    return np.array(puzzle)

def main():
    print("Run solution_bfs.py, solution_a_star_1.py, solution_a_star_2.py, " +
        "or solution_randomized.py to try the program")

if __name__ == "__main__":
    main()
