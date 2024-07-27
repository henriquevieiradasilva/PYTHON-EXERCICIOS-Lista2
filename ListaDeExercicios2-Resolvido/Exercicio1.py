"""

1) Um comerciante deseja descobrir qual o lucro de sua loja em uma semana. Sabe-se que ele tem um gasto diário fixo,
assim como um ganho diário fixo. A loja funciona de segunda à sexta. Calcule esse lucro semanal.

"""
while True:
    try:
        gastoDiario = float(input('Qual o GASTO DIÁRIO do seu estabelecimento?\n'))
        if gastoDiario >= 0:
            break
        print('\nPor favor, digite um número válido')
    except:
        print('\nPor favor, digite um número válido')

while True:
    try:
        ganhoDiario = float(input('Qual o GANHO DIÁRIO do seu estabelecimento?\n'))
        if ganhoDiario >= 0:
            break
        print('\nPor favor, digite um número válido')
    except:
        print('\nPor favor, digite um número válido')

print(f'O LUCRO SEMANAL do seu estabelecimento é de R${(ganhoDiario - gastoDiario) * 5:.2f}')

gastoDiario = 0
ganhoDiario = 0
