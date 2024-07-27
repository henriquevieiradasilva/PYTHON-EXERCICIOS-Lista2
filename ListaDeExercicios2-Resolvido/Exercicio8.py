"""

8) Construa um algoritmo para que, dado um número inteiro maior que 9 e menor do que 100, seja possível inverter seus
dois algarismos (por exemplo, entrada = 28, saída = 82).

"""
while True:
    try:
        numeroDigitado = int(input("Digite um número que possui DUAS casas inteiras(XY)?\n"))
        if numeroDigitado >= 10 and numeroDigitado <= 99:
            break
        print("\nPor favor, digite um número válido com DOIS DÍGITOS..")
    except:
        print("\nPor favor, digite um número válido com DOIS DÍGITOS..")

algarismoUnidade = numeroDigitado
algarismoDezena = numeroDigitado

while algarismoUnidade >= 10:
    algarismoUnidade -= 10

algarismoDezena -= algarismoUnidade
algarismoDezena //= 10
print(f"O número invertido fica: {str(algarismoUnidade) + str(algarismoDezena)}")

numeroDigitado = 0
algarismoUnidade = 0
algarismoDezena = 0