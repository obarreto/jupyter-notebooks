# Exercício 3 - FizzBuzz parcial, parte 1

# Receba um número inteiro na entrada e imprima Buzz se o numero
# for divisível por 5. Caso contrário, imprima o mesmo número que 
# foi dado na entrada.

integer = int( input("Insira um numero inteiro: "))

x = integer % 5

if(x == 0):
    print("Buzz")
else:
    print(integer)