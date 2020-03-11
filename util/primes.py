# Generates primes until MAX in file. 

FILE = "primes.txt"
MAX = 1000000

def getPrimes():
    primes = []

    with open(FILE, 'w') as h:
        for i in range(2, MAX + 1):
            for p in primes:
                if i % p == 0:
                    break
            else:
                h.write(str(i) + " ")
                primes.append(i)
    
    return primes

if __name__ == '__main__':
    print(getPrimes()[-1])