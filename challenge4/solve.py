# Brute-force approach using linear algebra system. In the case of a 4x4, time complexity is 10^12. 3x3 is simply 10^2.
# I'm kind of disappointed that all online solutions I could find have similar complexities. 

import numpy as np
import sympy

GRID_SIZE = 4
MAX_NUM = 9
OUTPUT_FILE = 'solution.txt'

def crissCross() -> int:
    
    # Matrix system of equations.
    matrix = []

    # Symbol
    N = sympy.Symbol('N')

    # Generate matrix relation.
    main_diag = []
    second_diag = []

    for i in range(GRID_SIZE):
        # For diags.
        diag = [0] * GRID_SIZE
        diag[i] = 1

        main_diag += diag

        diag = [0] * GRID_SIZE
        diag[GRID_SIZE - i - 1] = 1

        second_diag += diag

        # For columns.
        col = [0] * GRID_SIZE
        col[i] = 1

        matrix.append(col * GRID_SIZE + [N])

        # For rows.
        row = []

        for j in range(GRID_SIZE):
            if i == j:
                row += [1] * GRID_SIZE
            else:
                row += [0] * GRID_SIZE

        matrix.append(row + [N])

    # Adding row to matrix.
    matrix.append(main_diag + [N])
    matrix.append(second_diag + [N])

    # Converting plain array to matrix.
    matrix = sympy.Matrix(matrix)

    # Row Echelon Form.
    row_echelon, leading_ones = matrix.rref()

    # Get free variables.
    free_variables = list(set(range(GRID_SIZE ** 2)) - set(leading_ones))

    free_variable_len = len(free_variables)

    # If no free variables, only solution is if they're all the same.
    if free_variable_len == 0:
        return MAX_NUM + 1

    # Returns the system of free variables.
    free_matrix = []

    for row_index, leading_one_index in enumerate(leading_ones):
        free_matrix.append([row_echelon[row_index, free_variable] * -1 for free_variable in free_variables] + [row_echelon[row_index, GRID_SIZE ** 2]])

    free_matrix = np.array(free_matrix)

    # Form for numbers.
    form = '%0' + str(free_variable_len) + 'd'

    # Total number of variables.
    count = 0

    # Assuming a row is a certain sum.
    for target_sum in range(MAX_NUM ** GRID_SIZE + 1):
        # For variables (which is simply a number).
        for variables_int in range(int(str(MAX_NUM) * free_variable_len)):
            # Create variables.
            variables_vector = np.array([int(x) for x in form % variables_int])
            # For each row, check if condition is met.
            for row in free_matrix:
                s = row[-1].subs([(N, target_sum)]) + variables_vector.dot(np.array(row[:-1]))

                if s < 0 or s > 9:
                    break
            else:
                count += 1

    return count

if __name__ == '__main__':
    with open(OUTPUT_FILE, 'w') as h:
        h.write(str(crissCross()))