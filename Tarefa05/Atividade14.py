# Curso básico de python
# Nome do desenvolvedor: Juliana Rodrigues Brito
# Versão 1.0
# Exercício de Lógica de programação com a linguagem python

# Escreva um programa que peça ao usuário para digitar três números e retorne o maior deles.

primeiroNumero = int(input("Informe o primeiro número inteiro:"))
segundoNumero = int(input("Informe o segundo número inteiro:"))
terceiroNumero = int(input("Informe o terceiro número inteiro:"))

if primeiroNumero > segundoNumero & primeiroNumero > terceiroNumero:
   print("O maior número entre os valores informados é: " , primeiroNumero)
elif segundoNumero > primeiroNumero & segundoNumero > terceiroNumero:
    print("O maior número entre os valores informados é: " , segundoNumero)
else:
    print("O maior número entre os valores informados é: " , terceiroNumero) 