# Curso básico de python
# Nome do desenvolvedor: Juliana Rodrigues Brito
# Versão 1.0
# Exercício de Lógica de programação com a linguagem python

# Faça um programa que receba um número inteiro e retorne se é primo ou não.

numero = int(input("Digite um número inteiro, para saber se ele é primo: "))

if numero <= 1:
    numeroPrimo = False
else:
    numeroPrimo = True
    for i in range(2, int(numero ** 0.5) + 1):
        if numero % i == 0:
            numeroPrimo = False
            break

if numeroPrimo:
    print(f"O número {numero} é primo.")
else:
    print(f"O número {numero} não é primo.")