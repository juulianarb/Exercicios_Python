# Curso básico de python
# Nome do desenvolvedor: Juliana Rodrigues Brito
# Versão 1.0
# Exercício de Lógica de programação com a linguagem python

#  Escreva um programa que leia um número e informe se ele é positivo ou negativo.
# Se for positivo, calcule a raiz quadrada; se for negativo, informe o número ao quadrado.

import math

numero = int(input("Digite um número inteiro:"))

if numero > 0:
    print("Positivo!")
    print(f"A raiz quadrada do número informado {numero}, é: ", math.sqrt(numero))
elif numero < 0:
    print("Negativo!")
    print(f"O número ao quadrado do número informado {numero}, é de: ", pow(numero,2))
else:
    print("O número informado é 0")