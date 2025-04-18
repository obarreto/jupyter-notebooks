#Atividade para entregar !

# Exercício 1 - Par ou impar ?
# Receba um numero inteiro na entrada e impra PAR quando o numero for par ou impar quando onumero for impar

integer = int( input("Insira um numero inteiro: "))

x = integer % 2

if(x == 0):
    print("PAR !")
else:
    print("ÍMPAR")
