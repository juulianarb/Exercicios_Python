# Curso básico de python
# Nome do desenvolvedor: Juliana Rodrigues Brito
# Versão 1.0
# Exercício de Lógica de programação com a linguagem python

#  Ler dois valores (considere que não serão lidos valores iguais) e escrevê-los em ordem crescente.

primeiroNumero = int(input("Digite um número: "))
segundoNumero = int(input("Digite outro número: "))

if primeiroNumero > segundoNumero:
    print("Os números informados em ordem crescente: ", primeiroNumero, ",", segundoNumero)
else:
    print("Os números informados em ordem crescente: ", segundoNumero, ",", primeiroNumero)