# Curso básico de python
# Nome do desenvolvedor: Juliana Rodrigues Brito
# Versão 1.0
# Exercício de Lógica de programação com a linguagem python

# Escreva um programa que leia dois números inteiros e informe qual deles é o maior.

primeiroNumeroInteiro = int(input("Digite um número inteiro para saber qual é o maior deles:"))
segundoNumeroInteiro = int(input("Digite um número inteiro para saber qual é o maior deles:"))

if primeiroNumeroInteiro > segundoNumeroInteiro:
    print(f"O maior número entre {primeiroNumeroInteiro} e {segundoNumeroInteiro} é o: " , primeiroNumeroInteiro)
else:
    print(f"O maior número entre {primeiroNumeroInteiro} e {segundoNumeroInteiro} é o: " , segundoNumeroInteiro)