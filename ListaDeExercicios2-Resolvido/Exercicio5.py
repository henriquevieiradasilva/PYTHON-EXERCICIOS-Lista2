"""

5) Um estudante deseja saber quantas divisões, ao todo, ele dispõe em todos os seus cadernos. Para isso, tem de saber
quantos cadernos possui e qual o número de divisões que um caderno tem (todos tem o mesmo número de divisões). Informe
o número total de divisões

"""
while True:
    try:
        quantidadeCadernos = int(input('Qual o número de CADERNOS que você possui?\n'))
        if quantidadeCadernos > 0:
            break
        print("\nPor favor, digite um número válido.")
    except:
        print("\nPor favor, digite um número válido.")

while True:
    try:
        quantidadeDivisoes = int(input('Qual o número de DIVISÕES o tipo do seu caderno possui?\n'))
        if quantidadeDivisoes > 0:
            break
        print("\nPor favor, digite um número válido.")
    except:
        print("\nPor favor, digite um número válido.")

print("O total de DIVISÕES que podem ser usadas é de", quantidadeCadernos * quantidadeDivisoes)

quantidadeCadernos = 0
quantidadeDivisoes = 0