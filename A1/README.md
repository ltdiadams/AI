## tilepuzzle.py
Template program. There are functions for: Random puzzle generation, puzzle input, puzzle hash, and other useful reusable functions.

## solution_bfs.py
Program to solve the puzzle using BFS.

How to use:

- Run `python solution_bfs.py`
- Input the number of rows
- Input the puzzle on the next N rows

## solution_a_star.py
The code for A* algorithm

## solution_a_star_1.py
Program to solve the puzzle using A* with the number of out-of-place tiles as its heuristics function.

How to use:

- Run `python solution_a_star_1.py`
- Input the number of rows
- Input the puzzle on the next N rows

## solution_a_star_2.py
Program to solve the puzzle using A* with the total Manhattan distance of all tiles as its heuristics function

How to use:

- Run `python solution_a_star_2.py`
- Input the number of rows
- Input the puzzle on the next N rows

## solution_randomized.py
Program to try many different puzzle possibilities for BFS, A* 1st variation, and A* 2nd variation

How to use:

- Run `python solution_randomized.py`
- Input the number of puzzles

## Other notes
You can also write the input into a file and then pipe it into the program using this command (assuming the input is in the in1.txt file)

- `python solution_a_star_1.py < in1.txt`
