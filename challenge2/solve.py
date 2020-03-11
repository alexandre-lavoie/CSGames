# To prevent having to init dictionary keys.
from collections import defaultdict

# File to read from.
PRIMES_FILE = "../util/primes.txt"
# Write solution to file.
OUTPUT_FILE = "solution.txt"

def getAllRollsForStr(s: str):
    # Rolls string for len(str).
    r = set()

    for _ in range(len(s)):
        if not s in r:
            r.add(s)

        s =  s[1:] + s[0]

    return r

def getCircularPrimes(primes: [str]) -> [int]:
    # Dict for set of primes per size. We don't have to check all primes to determine if circular; only same size primes.
    primes_by_size = defaultdict(lambda: set())

    # Circular primes list.
    circular_primes = set()

    # Seperates primes according to len.
    for prime in primes:
        primes_by_size[len(prime)].add(prime)

    # For all sizes and primes of that size.
    for (size, primes_of_size) in primes_by_size.items():
        # Set of seen circular primes (prevent double calculation).
        seen = set()

        # For all primes of certain size.
        for prime in primes_of_size:
            # Get all rolls of prime.
            rolls = getAllRollsForStr(prime)

            # If we never saw prime and all N rolls are in primes_of_size.
            if not prime in seen and len(primes_of_size.intersection(rolls)) == len(rolls):
                # Add rolls to circular prime.
                circular_primes = circular_primes.union(rolls)
                
                # Add rolls to seen.
                seen = seen.union(rolls)

    return sorted([int(x) for x in circular_primes])

if __name__ == '__main__':
    with open(PRIMES_FILE, 'r') as h:
        # Gets cylic primes using primes file. Assuming all primes are on one line with singular space. Refer to primes.py
        circular_primes = getCircularPrimes([p for p in h.readline().split(" ")[:-1]])
    
    with open(OUTPUT_FILE, 'w') as h:
        h.write(str(len(circular_primes)) + " " + str(circular_primes))