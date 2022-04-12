def get_primes(n):
    seive = dict()
    primes = []
    # n = n * 2  # del
    for i in range(2, n + 1):
        if not seive.get(i):
            primes.append(i)
            for j in range(i * i, n + 1, i):
                seive[j] = True

            # if i > n / 2:  # del
            #     return i  # del

    return primes


def is_prime(num):

    return get_primes(num)[-1] == num

