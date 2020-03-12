# Brute-force in O((n^2)^(n^2)) where n is the size of the grid.

GRID_SIZE = 3

def isSquareSum(grid: [[int]]) -> bool:
    len_grid = len(grid)
    total_sum = sum(grid[0])

    for row in grid[1:]:
        if not sum(row) == total_sum:
            return False

    for col in [[row[i] for row in grid] for i in range(len_grid)]:
        if not sum(col) == total_sum:
            return False

    main_diag_sum = 0
    second_diag_sum = 0

    for i in range(len_grid):
        main_diag_sum += grid[i][i]
        second_diag_sum += grid[i][len_grid - i - 1]

    if not main_diag_sum == total_sum or not second_diag_sum == total_sum:
        return False

    return True

def toSquareMartix(nums: [int], size: int) -> [[int]]:
    matrix = []

    for i in range(0, len(nums), size):
        matrix.append(nums[i:i+size])

    return matrix


def totalSquareSum() -> int:
    count = 0

    for x in range(10 ** (GRID_SIZE ** 2) - 1):
        str_num = ("%0" + str(GRID_SIZE ** 2)  + "d") % (x)

        if isSquareSum(toSquareMartix([int(x) for x in str_num], GRID_SIZE)):
            print(str_num)
            count += 1

    return count

if __name__ == '__main__':
    print(totalSquareSum())