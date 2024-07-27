"""

6) Calcular o salário mensal de um funcionário, considerando os seguintes dados de entrada: número de dias trabalhados
no mês, valor da hora de trabalho, número de horas extras. Considere que cada dia de trabalho tem 8 horas e que o valor
da hora extra é 20% maior que o valor da hora normal.

"""
while True:
    try:
        diasTrabalhados = int(input("Quantos DIAS trabalhados você possui nesse mês?\n"))
        if diasTrabalhados > 0:
            break
        print("\nPor favor, digite um número válido.")
    except:
        print("\nPor favor, digite um número válido.")

while True:
    try:
        valorHora = float(input("Qual o VALOR da sua HORA de trabalho?\n"))
        if valorHora > 0:
            break
        print("\nPor favor, digite um número válido.")
    except:
        print("\nPor favor, digite um número válido.")

while True:
    try:
        horasExtras = int(input("Quantos HORAS EXTRAS você possui nesse mês?\n"))
        if horasExtras >= 0:
            break
        print("\nPor favor, digite um número válido.")
    except:
        print("\nPor favor, digite um número válido.")

print(f"O seu SALÁRIO esse mês será de R${(diasTrabalhados*8)* valorHora + horasExtras * (valorHora*1.20):.2f}")

diasTrabalhados = 0
valorHora = 0
horasExtras = 0
