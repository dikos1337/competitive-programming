# Get the next prime number!

# You will get a numbern (>= 0) and your task is to find the next prime number.

# Make sure to optimize your code: there will numbers tested up to about 10^12.

# Examples
# 5   =>  7
# 12  =>  13


def get_primes(n):
    seive = dict()
    # primes = []
    n = n * 2  # del
    for i in range(2, n + 1):
        if not seive.get(i):
            # primes.append(i)
            for j in range(i * i, n + 1, i):
                seive[j] = True

            if i > n / 2:  # del
                return i  # del

    return i


# def next_prime(n):
#     if n < 1:
#         return 2
#     return get_primes(n)[-1]

# print(next_prime(2000))

print(get_primes(10**8))