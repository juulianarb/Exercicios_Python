# Curso básico de python
# Nome do desenvolvedor: Juliana Rodrigues Brito
# Versão 1.0
# Exercício de Lógica de programação com a linguagem python

# Escreva um programa que leia três lados de um triângulo e verifique se eles formam um triângulo válido.
# Para isso, a soma de dois lados deve ser sempre maior que o terceiro lado.

ladoA = int(input("Digite o valor do primeiro lado para formar um triângulo válido:"))
ladoB = int(input("Digite o valor do segundo lado para formar um triângulo válido:"))
ladoC = int(input("Digite o valor do terceiro lado para formar um triângulo válido:"))

if ladoA + ladoB > ladoC and ladoA + ladoC > ladoB and ladoB + ladoC > ladoA:
    print("Os lados formam um triângulo!")
else:
    print("Os lados não formam um triângulo")

