from tilepuzzle import read_puzzle
from solution_a_star import do_a_star

def count_total_manhattan(puzzle):
    n = puzzle.shape[0]
    m = puzzle.shape[1]
    total = 0

    for i in range(n):
        for j in range(m):
            target_coor = [puzzle[i, j] // m, puzzle[i, j] % m]
            total += abs(target_coor[0] - i) + abs(target_coor[1] - j)

    return total

def do_a_star_2(puzzle):
    print("Running A* using the total Manhattan distance of all tiles")
    return do_a_star(puzzle, count_total_manhattan)

def main():
    puzzle = read_puzzle()
    print(do_a_star_2(puzzle))

if __name__ == "__main__":
    main()
