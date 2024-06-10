# Curso básico de python
# Nome do desenvolvedor: Juliana Rodrigues Brito
# Versão 1.0
# Exercício de Lógica de programação com a linguagem python

#  Efetuar a leitura de três valores (variáveis A, B e C) e apresentá-los dispostos em ordem crescente.

a = int(input("Digite o primeiro valor: "))
b = int(input("Digite o segundo valor: "))
c = int(input("Digite o terceiro valor: "))

if a <= b and b <= c:
    print("Valores em ordem crescente: ", a, b, c)
elif a <= c and c <= b:
    print("Valores em ordem crescente: ", a, c, b)
elif b <= a and a <= c:
    print("Valores em ordem crescente: ", b, a, c)
elif b <= c and c <= a:
    print("Valores em ordem crescente: ", b, c, a)
elif c <= a and a <= b:
    print("Valores em ordem crescente: ", c, a, b)
else:
    print("Valores em ordem crescente: ", c, b, a)