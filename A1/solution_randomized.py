from tilepuzzle import init_scrambled_puzzle
from solution_bfs import do_bfs
from solution_a_star_1 import do_a_star_1
from solution_a_star_2 import do_a_star_2

def main():
    puzzle_count = int(input("How many randomized puzzle do you want? "))
    total_distance_lst = [0] * 3
    total_iterations_lst = [0] * 3
    total_running_time = [0] * 3

    for i in range(puzzle_count):
        puzzle = init_scrambled_puzzle(3, 100)
        print("Running Puzzle #{}:".format(i + 1))
        print(puzzle)

        bfs_result = do_bfs(puzzle)
        print("BFS: {}".format(bfs_result))

        a_star1_result = do_a_star_1(puzzle)
        print("A* (out-of-place tiles): {}".format(a_star1_result))
        
        a_star2_result = do_a_star_2(puzzle)
        print("A* (Manhattan distance): {}".format(a_star2_result))
        print()

        # if the puzzle size is 3 x 3, search result will never be -1
        # but if the puzzle is larger, it might happen
        if bfs_result["distance"] != -1:
            total_distance_lst[0] += bfs_result["distance"]
            total_iterations_lst[0] += bfs_result["iterations"]
            total_running_time[0] += bfs_result["time"]
        if a_star1_result["distance"] != -1:
            total_distance_lst[1] += a_star1_result["distance"]
            total_iterations_lst[1] += a_star1_result["iterations"]
            total_running_time[1] += a_star1_result["time"]
        if a_star2_result["distance"] != -1:
            total_distance_lst[2] += a_star2_result["distance"]
            total_iterations_lst[2] += a_star2_result["iterations"]
            total_running_time[2] += a_star2_result["time"]
    
    print("Successfully ran {} test cases".format(puzzle_count))
    print()
    print("BFS Average Distance: {:.5f}".format(total_distance_lst[0] / puzzle_count))
    print("BFS Average Iterations: {:.5f}".format(total_iterations_lst[0] / puzzle_count))
    print("BFS Average Running Time: {:.5f} seconds".format(total_running_time[0] / puzzle_count))
    print()
    print("A* (out-of-place tiles) Average Distance: {:.5f}".format(total_distance_lst[1] / puzzle_count))
    print("A* (out-of-place tiles) Average Iterations: {:.5f}".format(total_iterations_lst[1] / puzzle_count))
    print("A* (out-of-place tiles) Average Running Time: {:.5f} seconds".format(total_running_time[1] / puzzle_count))
    print()
    print("A* (Manhattan distance) Average Distance: {:.5f}".format(total_distance_lst[2] / puzzle_count))
    print("A* (Manhattan distance) Average Iterations: {:.5f}".format(total_iterations_lst[2] / puzzle_count))
    print("A* (Manhattan distance) Average Running Time: {:.5f} seconds".format(total_running_time[2] / puzzle_count))

if __name__ == "__main__":
    main()
