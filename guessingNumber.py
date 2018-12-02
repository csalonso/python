import random

def guessing_number():
    number = random.randint(0, 100)
    user_input = int(input('Digite um número: '))
    while (user_input != number):
        print('Errou')
        if(user_input > number):
            print('Alto')
        else:
            print('Baixo')
        user_input = int(input('Digite um número: '))
    print('Acertou')
    
