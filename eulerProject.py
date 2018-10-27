#Problem 1
def euler1():
    soma = 0
    i = 1
    while i < 1000:
        if i % 3 == 0 or i % 5 == 0:
            soma = soma + i
        i += 1
    return soma

#Fibonacci term
def fib(x):
    if x < 2:
        return x
    else:
        return fib(x - 1) + fib(x - 2)

#Problem 2   
def euler2():
    soma = 0
    i = 1
    while fib(i) < 4000000:
        if fib(i) % 2 == 0:
            soma = soma + fib(i)
        i += 1
    return soma

#Check if number is a prime number
def isPrime(x):
    soma = 0
    i = 1
    while i <= x:
        if x % i == 0:
            soma = soma + 1
        i += 1
    if soma == 2:
        return True
    else:
        return False

#Problem 3
def euler3():
    x = 600851475143
    i = 1
    primes = []
    while i <= x:
        if x % i == 0:
            if isPrime(i):
                primes = primes + [i]
        i += 1
    return max(primes)
