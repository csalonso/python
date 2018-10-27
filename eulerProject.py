#Problem 1
def euler1():
    soma = 0
    i = 1
    while i < 1000:
        if i % 3 == 0 or i % 5 == 0:
            soma = soma + i
        i += 1
    return soma
