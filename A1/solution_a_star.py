import heapq
import time
from tilepuzzle import empty_pos, make_move, is_solved, generate_move_list, hash_puzzle

def do_a_star(puzzle, heuristic_function):
    """A* Search Algorithm"""
    n = puzzle.shape[0]
    heap = []
    puzzle_dict = {}
    visited = {}
    puzzle_counter = 0
    iterations = 0
    start_time = time.time()
    
    visited[hash_puzzle(puzzle)] = True
    puzzle_dict[puzzle_counter] = puzzle
    heapq.heappush(heap, [heuristic_function(puzzle), 0, puzzle_counter])
    puzzle_counter += 1

    while len(heap) > 0:
        out_of_place_tiles, dist_now, puzzle_id = heapq.heappop(heap)
        puzzle_now = puzzle_dict[puzzle_id]
        del puzzle_dict[puzzle_id]
        iterations += 1

        if is_solved(puzzle_now):
            return {
                "distance": dist_now,
                "iterations": iterations,
                "time": time.time() - start_time
            }
        
        empty = empty_pos(puzzle_now)
        move_list = generate_move_list(empty, n)
        for move in move_list:
            new_puzzle = make_move(puzzle_now, move)
            hash_new_puzzle = hash_puzzle(new_puzzle)
            if hash_new_puzzle not in visited:
                visited[hash_new_puzzle] = True
                puzzle_dict[puzzle_counter] = new_puzzle
                heapq.heappush(heap, [heuristic_function(new_puzzle) + dist_now + 1,
                    dist_now + 1, puzzle_counter])
                puzzle_counter += 1
    
    return {
        "distance": -1,
        "iterations": iterations,
        "time": time.time() - start_time,
        "message": "Solution not found"
    }

def main():
    print("Run solution_a_star_1.py or solution_a_star_2.py to use the A* algorithm")

if __name__ == "__main__":
    main()
