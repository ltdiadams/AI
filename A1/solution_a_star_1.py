from tilepuzzle import read_puzzle
from solution_a_star import do_a_star

def count_out_of_place_tiles(puzzle):
    total = 0
    counter = 0
    for i in range(puzzle.shape[0]):
        for j in range(puzzle.shape[1]):
            if puzzle[i, j] != counter:
                total += 1
            counter += 1
    return total

def do_a_star_1(puzzle):
    print("Running A* using the number of out-of-place tiles")
    return do_a_star(puzzle, count_out_of_place_tiles)

def main():
    puzzle = read_puzzle()
    print(do_a_star_1(puzzle))

if __name__ == "__main__":
    main()
