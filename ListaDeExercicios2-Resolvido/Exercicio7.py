"""

7) Construa um algoritmo para que, dado um número inteiro maior que 9 e menor do que 100, seja possível determinar o
algarismo que representa as unidades deste número.

"""
while True:
    try:
        numeroDigitado = int(input("Digite um número que possui DUAS casas inteiras(XY)?\n"))
        if numeroDigitado >= 10 and numeroDigitado <= 99:
            break
        print("\nPor favor, digite um número válido com DOIS DÍGITOS.")
    except:
        print("\nPor favor, digite um número válido com DOIS DÍGITOS.")

while numeroDigitado >= 10:
    numeroDigitado -= 10

print(f"O algarismo que ocupa a posição de UNIDADES no número digitado é {numeroDigitado}")

numeroDigitado = 0
