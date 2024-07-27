"""

4) Uma indústria produz dois tipos de peças, cada qual em uma determinada quantidade. Como os pedidos aumentaram, ele
deseja subir a produção da primeira peça em 17% e da segunda em 26%. Informe os novos totais produzidos para cada uma
das peças. Obs: Arrendonde a quantidade para mais.

"""
import math
while True:
    try:
        totalPrimeiraPeca = int(input('Qual a QUANTIDADE produzidas da PRIMEIRA peça?\n'))
        if totalPrimeiraPeca > 0:
            break
        print("\nPor favor, digite um número válido.")
    except:
        print("\nPor favor, digite um número válido.")

while True:
    try:
        totalSegundaPeca = int(input('Qual a QUANTIDADE produzidas da SEGUNDA peça?\n'))
        if totalSegundaPeca > 0:
            break
        print("\nPor favor, digite um número válido.")
    except:
        print("\nPor favor, digite um número válido.")

print("A PRIMEIRA PEÇA deve ser produzida um total de APROXIMADAMENTE =", math.ceil(totalPrimeiraPeca * 1.17))
print(" A SEGUNDA PEÇA deve ser produzida um total de APROXIMADAMENTE =", math.ceil(totalSegundaPeca * 1.26))

totalPrimeiraPeca = 0
totalSegundaPeca = 0