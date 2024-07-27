"""

3) Calcular a quantidade de tijolos necessária para a construção de uma parede, tendo como dados de entrada a altura da
parede, a largura da parede, o comprimento do tijolo e a largura do tijolo. Obs: Arredondar para cima a quantidade de
tijolos.

"""
import math

while True:
    try:
        alturaParede = float(input('Qual a ALTURA da PAREDE?(em metros)\n'))
        if alturaParede > 0:
            break
        print("\nPor favor, digite um número válido.")
    except:
        print("\nPor favor, digite um número válido.")

while True:
    try:
        larguraParede = float(input('Qual a LARGURA da PAREDE?(em metros)\n'))
        if larguraParede > 0:
            break
        print("\nPor favor, digite um número válido.")
    except:
        print("\nPor favor, digite um número válido.")

while True:
    try:
        alturaTijolo = float(input('Qual a ALTURA do TIJOLO?(em centímetros)\n'))
        if alturaTijolo > 0:
            break
        print("\nPor favor, digite um número válido.")
    except:
        print("\nPor favor, digite um número válido.")

while True:
    try:
        larguraTijolo = float(input('Qual a LARGURA do TIJOLO?(em centímetros)\n'))
        if larguraTijolo > 0:
            break
        print("\nPor favor, digite um número válido.")
    except:
        print("\nPor favor, digite um número válido.")

resultadoFinal = math.ceil(((alturaParede * 100) * (larguraParede * 100)) / (alturaTijolo * larguraTijolo))
print("O total de TIJOLOS que serão necessário é de APROXIMADAMENTE =", resultadoFinal)

alturaParede = 0
larguraParede = 0
alturaTijolo = 0
larguraTijolo = 0
resultadoFinal = 0





