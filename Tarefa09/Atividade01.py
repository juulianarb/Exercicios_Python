# Curso básico de python
# Nome do desenvolvedor: Juliana Rodrigues Brito
# Versão 1.0
# Exercício de Lógica de programação com a linguagem python

# Escreva um programa que leia um número inteiro e informe se ele é par ou ímpar.

numeroInteiro = int(input("Digite um número inteiro para saber se é par ou impar:"))

if numeroInteiro % 2 == 0:
    print("O número informado é par")
else:
    print("O número informado é impar")