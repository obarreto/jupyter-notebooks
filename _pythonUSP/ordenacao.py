# Exercício 5 - Verificando ordenação
# Receba 3 números inteiros na entrada e imprima crescente
# se eles forem dados em ordem crescente. Caso contrário, imprima
# não está em ordem crescente.

integer1 = int( input("Insert 1st number: "))
integer2 = int( input("Insert 2st number: "))
integer3 = int( input("Insert 3st number: "))

if(integer1 < integer2 and integer2 < integer3):
    print("Crescente")
else:
        print("Não está em ordem crescente")