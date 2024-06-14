# Curso básico de python
# Nome do desenvolvedor: Juliana Rodrigues Brito
# Versão 1.0
# Exercício de Lógica de programação com a linguagem python

# Escreva um programa que leia um número inteiro e informe se ele é positivo, negativo ou zero.

numeroInteiro = int(input("Digite um número inteiro para saber se é positivo, negativo ou zero:"))

if numeroInteiro > 0:
    print("Positivo!")
elif numeroInteiro == 0:
    print("Zero!")
else:
    print("Negativo!")