import time
import sys
import numpy as np
import random

# This function generates a random problem instance
def make_random_problem(n_variables, n_clauses):
    # This is a helper function to check if a row occurs in a matrix
    def find_row(mx, row):
        for i in range(mx.shape[0]):
            if np.all(mx[i, :] == row):
                return True
        return False
    # This is a helper function to make a random clause (represented as a row
    # in a Numpy matrix)
    def make_random_clause(n_variables):
        # Create a Numpy matrix to store the row
        clause_mx = np.zeros((1, n_variables))
        # Fill in a random clause
        for i in range(n_variables):
            clause_mx[0, i] = random.choice((-1, 0, 1))
        return clause_mx
    # Start with a random row (representing one clause)
    problem_mx = make_random_clause(n_variables)
    # Add unique, non-empty clauses until the problem reaches the required size
    while problem_mx.shape[0] < n_clauses:
        temp = make_random_clause(n_variables)
        if not find_row(problem_mx, temp) and not np.all(temp == np.zeros((1, n_variables))):
            problem_mx = np.vstack((problem_mx, temp))
    return problem_mx

# This function makes a random assignment of values to variables
def make_random_assignment(n_variables):
    # Allocate a Numpy array
    assignment_mx = np.zeros((1, n_variables))
    # Assign random truth values to the variables
    for i in range(n_variables):
        assignment_mx[0, i] = random.choice((-1, 1))
    return assignment_mx

# This function calculates the number of violations a solution has
def calculate_violation(problem, solution):
    violations = 0
    for i in range(problem.shape[0]):
        row_result = False
        exist_literal = False
        for j in range(problem.shape[1]):
            if problem[i, j] == 1:
                exist_literal = True
                literal = solution[0, j] == 1
                row_result = row_result or literal
            elif problem[i, j] == -1:
                exist_literal = True
                literal = solution[0, j] == 1
                row_result = row_result or literal
        if exist_literal and not row_result:
            violations += 1
    return violations

# Main program
def main():
    n_variables = int(input("Number of variables: "))
    n_clauses = int(input("Number of clauses: "))
    iterations_logging = True
    if len(sys.argv) > 1:
        if sys.argv[1] == "--no-logging":
            iterations_logging = False

    print("Generating problem...")
    problem = make_random_problem(n_variables, n_clauses)
    print("Generating starting solution...")
    candidate_solution = make_random_assignment(n_variables)
    steps = 0

    start_time = time.time()
    print("Running Local Search...")
    for i in range(10):
        steps = i
        violations = calculate_violation(problem, candidate_solution)

        print(f"Iterations #{i + 1}")
        if iterations_logging:
            print("Problem:")
            print(problem)
            print("Candidate solution:")
            print(candidate_solution)
            print(f"Violations: {violations}")
            print()

        if violations == 0:
            print("-- Found global minimum --")
            break

        lowest_violations = violations
        lowest_idx = -1
        for i in range(n_variables):
            candidate_solution[0, i] = 1 if candidate_solution[0, i] == -1 else -1
            new_violations = calculate_violation(problem, candidate_solution)
            if new_violations < lowest_violations:
                lowest_violations = new_violations
                lowest_idx = i
            candidate_solution[0, i] = 1 if candidate_solution[0, i] == -1 else -1

        if lowest_idx == -1:
            print("-- Found local minimum --")
            break
        else:
            candidate_solution[0, lowest_idx] = 1 if candidate_solution[0, lowest_idx] == -1 else -1

    print("-- in {} step(s) --".format(steps))
    print("-- in {:.5f} seconds".format(time.time() - start_time))
    if not iterations_logging:
        print("Problem:")
        print(problem)
        print("Solution:")
        print(candidate_solution)

if __name__ == "__main__":
    main()
