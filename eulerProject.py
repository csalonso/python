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

