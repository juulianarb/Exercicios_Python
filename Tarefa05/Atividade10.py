# Curso básico de python
# Nome do desenvolvedor: Juliana Rodrigues Brito
# Versão 1.0
# Exercício de Lógica de programação com a linguagem python

#  Ler dois valores (considere que não serão lidos valores iguais) e escrever o maior deles

primeiroNumero = int(input("Informe o primeiro número inteiro:"))
segundoNumero = int(input("Informe o segundo número inteiro:"))

if primeiroNumero > segundoNumero:
    print("O maior número é: ", primeiroNumero)
else:
    print("O maior número é: ", segundoNumero)