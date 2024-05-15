# Curso básico de python
# Nome do desenvolvedor: Juliana Rodrigues Brito
# Versão 1.0
# Exercício de Lógica de programação com a linguagem python

# Escreva um programa que peça ao usuário para digitar um número e verifique se é positivo, negativo ou zero.

numeroSolicitado = int(input("Informe um número inteiro, para saber se é positivo, negativo ou zero:"))

if numeroSolicitado > 0:
    print("É positivo")
elif numeroSolicitado == 0:
    print("É zero")
else:
    print("É negativo")