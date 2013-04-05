def genPrimes():
    primes = []
    x = 2
    while True:
        candidate = True
        for p in primes:
            if x % p == 0:
                candidate = False
        prime = True
        if True == candidate:
            for i in range(2, x/2):
                if x % i == 0:
                    prime = False
            if True == prime:
                primes.append(x)
                yield x
        x += 1
        
