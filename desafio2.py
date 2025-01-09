# 2) Dado a sequência de Fibonacci, onde se inicia por 0 e 1 e o próximo valor sempre será a soma dos 2 valores anteriores (exemplo: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34...), escreva um programa na linguagem que desejar onde, informado um número, ele calcule a sequência de Fibonacci e retorne uma mensagem avisando se o número informado pertence ou não a sequência.

# IMPORTANTE: Esse número pode ser informado através de qualquer entrada de sua preferência ou pode ser previamente definido no código;

def verificar_fibonacci(numero):
    a, b = 0, 1

    while b <= numero:
        if b == numero or a == numero:
            print(f"O número {numero} pertence à sequência de Fibonacci.")
            return
        a, b = b, a + b

    print(f"O número {numero} não pertence à sequência de Fibonacci.")

verificar_fibonacci(5)
verificar_fibonacci(21)
verificar_fibonacci(33)
verificar_fibonacci(35)
verificar_fibonacci(100)
