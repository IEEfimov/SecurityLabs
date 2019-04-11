import math
from math import ceil, sqrt


def codedist(a, b):
    dist = 0
    for i in range(0, a.__len__()):
        xor = a[i] ^ b[i]
        if xor == 1:
            dist += 1

    return dist


def gcd(a, b):
    while a != 0 and b != 0:
        if a > b:
            a = a % b
        else:
            b = b % a
    return a+b


def euler(N):
    count = 0
    for i in range(1, N):
        if gcd(N, i) == 1:
            # print(str(i))
            count += 1
        # else:
            # print("no: " + str(i) + " > " + str(gcd(N, i)))
    return count


def inverse(a, n):
    if gcd(a, n) != 1:
        print("числа не взаємо прості")
        return

    print(str(euler(n)))

    value = (a ** (euler(n) - 1)) % n

    return round(value)


def testprime(n):
    maximal = math.ceil(math.sqrt(n))
    for i in range(2, maximal):
        if i > 3:
            if (i % 2 == 0) or (i % 3 == 0):
                continue

        if n % i == 0:
            return 0
    return 1


def theprime(n1, n2):
    for i in range(n1, n2):
        if testprime(i) == 1:
            return i
    return 0


def bsgs(g, h, p):
    '''
    Solve for x in h = g^x mod p given a prime p.
    If p is not prime, you shouldn't use BSGS anyway.
    '''
    N = ceil(sqrt(p - 1))  # phi(p) is p-1 if p is prime

    # Store hashmap of g^{1...m} (mod p). Baby step.
    tbl = {pow(g, i, p): i for i in range(N)}

    # Precompute via Fermat's Little Theorem
    c = pow(g, N * (p - 2), p)

    # Search for an equivalence in the table. Giant step.
    for j in range(N):
        y = (h * pow(c, j, p)) % p
        if y in tbl:
            return j * N + tbl[y]

    # Solution not found
    return None
