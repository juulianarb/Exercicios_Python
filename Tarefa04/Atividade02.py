# Curso básico de python
# Nome do desenvolvedor: Juliana Rodrigues Brito
# Versão 1.0
# Exercício de Lógica de programação com a linguagem python

# Faça um programa que peça ao usuário para digitar um número e informe se é par ou ímpar.

numeroSolicitado = int(input("Informe um número inteiro, para saber se é par ou impar:"))
calculoPar = numeroSolicitado % 2

if calculoPar == 0:
    print("O numero informado é par")
else:
    print("O numero informado é impar")