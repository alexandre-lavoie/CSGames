# Gets greatest product on grid. Solved in O(n^2).

INPUT_FILE = "grid.txt"
OUTPUT_FILE = "solution.txt"

def product(items: [int]) -> int:
    # Performs a list product.
    prod = 1

    for i in items:
        prod *= i

    return prod

def greatestGridProduct(grid: [[int]]) -> int:
    # Size of grid.
    lgrid = len(grid)

    # Set of products.
    products = set()

    for i, row in enumerate(grid):
        for j, _ in enumerate(row):
            # For rows and columns:
            temp_prods = set([
                product(grid[i][max(j - 3, 0):j + 1]),
                product(grid[i][j:j + 4]),
                product([r[j] for r in grid[max(i - 3, 0):i + 1]]),
                product([r[j] for r in grid[i:i + 4]])
            ])

            # For diagonals:
            for (di, dj) in [(1,1), (1,-1), (-1,1), (-1,1)]:
                ele_to_prod = []

                for (ni, nj) in [(i + m * di, j + m * dj) for m in range(4)]:
                    if ni >= 0 and ni < lgrid and nj >= 0 and nj < lgrid:
                        ele_to_prod.append(grid[ni][nj])
                
                temp_prods.add(product(ele_to_prod))

            # Insert products to set.
            products = products.union(temp_prods)

    return max(products)

if __name__ == '__main__':
    # Reads file.
    with open(INPUT_FILE, 'r') as h:
        grid = [[int(y) for y in x.strip().split(' ')] for x in h.readlines()]

    with open(OUTPUT_FILE, 'w') as h:
        h.write(str(greatestGridProduct(grid)))