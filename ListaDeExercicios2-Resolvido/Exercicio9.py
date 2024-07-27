"""

9) Construa um algoritmo para que, dadas duas variáveis quaisquer, seus valores possam ser invertidos (ex: variáveis a e
b, o valor de a passa para b e vice-versa).

"""
while True:
    try:
        X = float(input("Digite um número qualquer para atribuir para X:\n"))
        break
    except:
        print("\nPor favor, digite um número válido.")

while True:
    try:
        Y = float(input("Digite um número qualquer para atribuir para Y:\n"))
        break
    except:
        print("\nPor favor, digite um número válido.")

print(f"Antes X tinha o valor {X} e Y o valor {Y},")
Z = X
X = Y
Y = Z
print(f"Agora X tem o valor {X} e Y o valor {Y},")

X = 0
Y = 0
Z = 0