"""
    factorization

    Time    O(sqrt(N))
    Space   O(sqrt(N)) <- the result array
"""


def getFactors(n):
    smalls = []
    bigs = []
    i = 1
    while i * i <= n:
        if n % i == 0:
            if i == n//i:
                smalls.append(i)
            else:
                smalls.append(i)
                bigs.append(n//i)
        i += 1
    return smalls + bigs[::-1]


print(getFactors(49))
print(getFactors(60))
print(getFactors(400))
print(getFactors(500))
print(getFactors(2310))


print("-----")


def getPrimeFactors(n):
    i = 2
    factors = set()
    while i * i <= n:
        if n % i == 0:
            factors.add(i)
            n //= i
        else:
            i += 1
    if n > 1:
        factors.add(n)
    return list(factors)


print(getPrimeFactors(40))
print(getPrimeFactors(60))
print(getPrimeFactors(400))
print(getPrimeFactors(500))
print(getPrimeFactors(2310))
