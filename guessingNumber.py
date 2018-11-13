import random

def guessingNumber():
    number = random.randint(0, 100)
    userInput = int(input('Digite um número: '))
    while (userInput != number):
        print('Errou')
        if(userInput > number):
            print('Alto')
        else:
            print('Baixo')
        userInput = int(input('Digite um número: '))
    print('Acertou')
    
