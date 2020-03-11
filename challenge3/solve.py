# File with N primes.
PRIMES_FILE = '../util/primes.txt'
# Solution file path.
OUTPUT_FILE = 'solution.txt'
# Max size of primes.
MAX_SIZE = 1000000

# Gets N primes from PRIMES_FILE.
def getPrimesUntilN(n: int) -> [int]:
    # Temp storage for primes.
    temp_primes = []

    with open(PRIMES_FILE, 'r') as h:
        # For each prime on first line. While primes are less than max.
        for prime in [int(x) for x in h.readline().split(" ")[:-1]]:
            if prime < n:
                temp_primes.append(prime)
            else:
                break

    # Return N primes.
    return temp_primes

def getLargestSumPrime() -> (int, int, [int]):
    # List of primes.
    primes = getPrimesUntilN(MAX_SIZE)
    # Array of rolling sum.
    rolling_sums = [0]

    # For all primes in prime.
    for i, prime in enumerate(primes):
        # Append the next rolling sum -> simply previous_sum + next_prime.
        rolling_sums.append(rolling_sums[-1] + prime)
        # If current rolling_sum is greater than MAX, stop.
        if rolling_sums[-1] > MAX_SIZE:
            break

    # For all consecutive size intervals. From largest size to smallest size.
    for size in range(len(rolling_sums) - 1, 0, -1):
        # For all (i, j) where j = i + size in the size limit of the rolling_sums.
        # We start from the right to make sure we get the largest prime.
        for i, j in [(x, x + size) for x in list(range(len(rolling_sums) - size - 1, -1, -1))]:
            # Gets sum for interval. Sum to j - Sum to i = Sum between i and j.
            sum_interval = rolling_sums[j] - rolling_sums[i]
            # If the sum interval of primes is a prime, then we found the largest prime.
            if sum_interval in primes:
                return sum_interval, size, primes[i:j]

if __name__ == '__main__':
    (largest_sum_prime, len_terms, primes) = getLargestSumPrime()

    with open(OUTPUT_FILE, 'w') as h:
        h.write(str(largest_sum_prime)  + " " + str(primes) + " " + str(len(primes)))