def get_primes(n):
    seive = dict()
    primes = []
    for i in range(2, n + 1):
        if not seive.get(i):
            primes.append(i)
            for j in range(i * i, n + 1, i):
                seive[j] = True

    return primes


def sum_primes(lower, upper):
    # Your code here
    primes = get_primes(upper)

    return sum(filter(lambda x: x >= lower, primes))


# print(get_primes(120))
print(sum_primes(4, 20))
print(sum_primes(20, 4))
print(sum_primes(2, 7))
print(sum_primes(1, 30))
