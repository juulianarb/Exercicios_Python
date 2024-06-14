# Curso básico de python
# Nome do desenvolvedor: Juliana Rodrigues Brito
# Versão 1.0
# Exercício de Lógica de programação com a linguagem python

# Escreva um programa que leia um número e verifique se ele está no intervalo de 10 a 20 (inclusive).

numero = int(input("Digite um número inteiro:"))

if numero > 9 and numero < 21:
    print("O número informado está no intervalo de 10 a 20")
else:
    print("O número informado não está no intervalo de 10 a 20")