#Jokenpo
def jokenpo():
    print('Escolha: \n 1 - Pedra \n 2 - Papel \n 3 - Tesoura \n')
    
    player1 = int(input('Jogador 1: '))
    while(player1 > 3 or player1 < 1):
        player1 = int(input('Jogada Inválida, Jogador 1: '))
        
    player2 = int(input('Jogador 2: '))
    while(player2 > 3 or player2 < 1):
        player2 = int(input('Jogada Inválida, Jogador 2: '))

    result = ''

    if (player1 == player2):
        result = 'Empate'
    else:
        if (player1 == 1):
            if (player2 == 2):
                result = 'Jogador 2 Venceu'
            elif (player2 == 3):
                result = 'Jogador 1 Venceu'
        elif(player1 == 2):
            if (player2 == 1):
                result = 'Jogador 1 Venceu'
            elif (player2 == 3):
                result = 'Jogador 2 Venceu'
        elif(player1 == 3):
            if (player2 == 1):
                result = 'Jogador 2 Venceu'
            elif (player2 == 2):
                result = 'Jogador 1 Venceu'
    return result
