import time
from queue import Queue
from tilepuzzle import read_puzzle, empty_pos, make_move, is_solved, generate_move_list, hash_puzzle

def do_bfs(puzzle):
    print("Running BFS")
    n = puzzle.shape[0]
    bfs_queue = Queue()
    visited = {}
    iterations = 0
    start_time = time.time()

    visited[hash_puzzle(puzzle)] = True
    bfs_queue.put({
        "puzzle": puzzle,
        "distance": 0
    })

    while not bfs_queue.empty():
        front_queue = bfs_queue.get()
        puzzle_now = front_queue["puzzle"]
        dist_now = front_queue["distance"]
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
                bfs_queue.put({
                    "puzzle": new_puzzle,
                    "distance": dist_now + 1
                })

    return {
        "distance": -1,
        "iterations": iterations,
        "time": time.time() - start_time,
        "message": "Solution not found"
    }

def main():
    puzzle = read_puzzle()
    print(do_bfs(puzzle))

if __name__ == "__main__":
    main()
