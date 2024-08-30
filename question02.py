# 2) Dado a sequência de Fibonacci, onde se inicia por 0 e 1 e o próximo valor
# sempre será a soma dos 2 valores anteriores 
# (exemplo: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34...), 
# escreva um programa na linguagem que desejar onde, informado um número, 
# ele calcule a sequência de Fibonacci e retorne uma mensagem avisando 
# se o número informado pertence ou não a sequência.

# IMPORTANTE: Esse número pode ser informado através de qualquer entrada 
# de sua preferência ou pode ser previamente definido no código;

def fibonacciSequence(n):
    x, y = 0, 1
    while x <= n:
        if x == n:
            return True
        x, y = y, x + y
    return False

number = int(input("Informe um número: "))
if fibonacciSequence(number):
    print(f"O número {number} que pertence à sequência de Fibonacci.")
else:
    print(f"O número {number} que não pertence à sequência de Fibonacci.")


