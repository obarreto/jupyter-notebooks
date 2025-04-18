# Exercício 2 - FizzBuzz parcial, parte 1

# Receba um número inteiro na entrada e imprima Fizz se o numero
# for divisível por 3. Caso contrário, imprima o mesmo número que 
# foi dado na entrada.

integer = int( input("Insira um numero inteiro: "))

x = integer % 3

if(x == 0):
    print("Fizz")
else:
    print(integer)