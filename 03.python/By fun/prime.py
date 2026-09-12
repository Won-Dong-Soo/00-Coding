def prime(a,b):
    check = [False, False] + [True] * (b - a-1)
    primes = []
    for i in range(2, len(check)):
        if check[i]:
            primes.append(i)
            for j in range(i*2, len(check), i):
                check[j] = False
    return [x for x in primes if x >= a]