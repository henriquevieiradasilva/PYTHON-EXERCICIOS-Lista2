"""

2) Um aluno faz duas provas no semestre, obtendo duas notas. A primeira corresponde a 40% de sua média final, a segunda
corresponde a 60%. Calcule a média final.

"""
while True:
    try:
        notaPrimeiraProva = float(input('Qual a sua nota na PRIMEIRA prova?\n'))
        if notaPrimeiraProva >= 0 and notaPrimeiraProva <= 10:
            break
        print('\nPor favor, digite um número válido')
    except:
        print('\nPor favor, digite um número válido')

while True:
    try:
        notaSegundaProva = float(input('Qual a sua nota na SEGUNDA prova?\n'))
        if notaSegundaProva >= 0 and notaSegundaProva <= 10:
            break
        print('\nPor favor, digite um número válido')
    except:
        print('\nPor favor, digite um número válido')

print(f"O valor da sua MÉDIA FINAL é de = {notaPrimeiraProva * 0.4 + notaSegundaProva * 0.6:.2f}")

notaPrimeiraProva = 0
notaSegundaProva = 0