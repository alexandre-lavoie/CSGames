import numpy as np
import scipy.linalg

GRID_SIZE = 2

def totalSquareSum() -> int:
    
    matrix = []

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

        matrix.append(col * GRID_SIZE)

        # For rows.
        row = []

        for j in range(GRID_SIZE):
            if i == j:
                row += [1] * GRID_SIZE
            else:
                row += [0] * GRID_SIZE

        matrix.append(row)

    matrix.append(main_diag)
    matrix.append(second_diag)

    matrix = np.array(matrix)

    return 0

if __name__ == '__main__':
    print(totalSquareSum())