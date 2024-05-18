# Curso básico de python
# Nome do desenvolvedor: Juliana Rodrigues Brito
# Versão 1.0
# Exercício de Lógica de programação com a linguagem python

#  Ler um valor e escrever se é positivo, negativo ou zero.

numero = int(input("Informe um número inteiro:"))

if numero > 0:
    print("Este número é positivo!")
elif numero == 0:
    print("Zero!")
else:
    print("Este número é negativo!")