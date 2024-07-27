"""

10) Dado um número com parte fracionária, mostre apenas a parte fracionária do número.

"""
while True:
    try:
        numeroExemplo = float(input("Digite um NÚMERO que tenha CASAS DECIMAIS?\n"))
        numeroExemplo = str(numeroExemplo)
        break
    except:
        print("\nPor favor, digite um número válido.")

localizacaoPonto = numeroExemplo.find(".")
parteFracionaria = numeroExemplo[localizacaoPonto:]
print(f"A parte FRACIONÁRIA do número é {parteFracionaria}")

numeroExemplo = 0
localizacaoPonto = 0
parteFracionaria = 0

