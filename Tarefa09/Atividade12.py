# Curso básico de python
# Nome do desenvolvedor: Juliana Rodrigues Brito
# Versão 1.0
# Exercício de Lógica de programação com a linguagem python

# Escreva um programa que leia um número e verifique se ele é maior que 100. Se não for, informe o dobro desse número.

numero = int(input("Digite um número inteiro:"))

if numero < 101:
    print(numero * 2)
else:
    print("Maior que 100")