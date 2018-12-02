def calc():
    n1 = int(input('Digite o primeiro número: '))
    n2 = int(input('Digite o segundo número: '))
    op(n1, n2)

def op(n1, n2):
    print('\nSelecione a operação:\n1 - Soma\n2 - Subtração\n3 - Divisão\n4 - Multiplicação')
    opc = int(input('Opção: '))

    if (opc == 1):
        print(n1 + n2)
    elif (opc == 2):
        print(n1 - n2)
    elif (opc == 3):
        if (n2 == 0):
            print('Não é possível dividir por "0"\n')
            calc()
        else:
            print(n1 / n2)
    elif (opc == 4):
        print(n1 * n2)
    else:
        print('Opcão inválida\n')
        op(n1, n2)
