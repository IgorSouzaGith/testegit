def calculate():
    operation = input('''
Gentileza selecione a operação desejada:
+ Para adição
- Para subtrair
* Para Multiplicar
/ Para Divisão
''')

    number_1 = int(input('Digite o primeiro numero: '))
    number_2 = int(input('Digite o segundo numero: '))

    if operation == '+':
        print('{} + {} = '.format(number_1, number_2))
        print(number_1 + number_2)

    elif operation == '-':
        print('{} - {} = '.format(number_1, number_2))
        print(number_1 - number_2)

    elif operation == '*':
        print('{} * {} = '.format(number_1, number_2))
        print(number_1 * number_2)

    elif operation == '/':
        print('{} / {} = '.format(number_1, number_2))
        print(number_1 / number_2)

    else:
        print('Você não inseriu corretamente o operador, porfavor click em Run e insira novamente.')

    # Adiciona novamente() função calculate() função
    again()


def again():
    calc_again = input('''
Deseja fazer mais um calculo?
Porfavor se deja digite Y para Sim ou N para Não.
''')

    if calc_again.upper() == 'Y':
        calculate()
    elif calc_again.upper() == 'N':
        print('Até mais.')
    else:
        again()


calculate()