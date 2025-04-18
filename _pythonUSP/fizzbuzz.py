# Exercício 4 - FizzBuzz parcial, parte 1

# Receba um número inteiro na entrada e imprima FizzBuzz se o numero
# for divisível por 3 e 5. Caso contrário, imprima o mesmo número que 
# foi dado na entrada.

integer = int( input("Insira um numero inteiro: "))

x = integer % 3
y = integer % 5

if(x == 0 and y == 0):
    print("FizzBuzz")
else:
    print(integer)