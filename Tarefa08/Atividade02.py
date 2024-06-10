# Curso básico de python
# Nome do desenvolvedor: Juliana Rodrigues Brito
# Versão 1.0
# Exercício de Lógica de programação com a linguagem python

# Apresentar os resultados de uma tabuada de multiplicar (de 1 até 10) de um número qualquer. 
# c) Apresentar o total da soma obtida dos cem primeiros números inteiros (1+2+3+4+...+98+99+100). 
# d) Elaborar um programa que apresente no final o somatório dos valores pares existentes na faixa de 1 até 500.

valor = int(input("Digite um valor para saber a tabuada: "))

contadora = 1

while contadora <= 10:
    print(valor, "x", contadora, "=", valor*contadora)
    contadora += 1

#  Apresentar o total da soma obtida dos cem primeiros números inteiros (1+2+3+4+...+98+99+100).

soma = 0

for i in range(1, 101):
  soma += i
print("A soma dos valores entre 1 e 100 é de: ", soma)


# Elaborar um programa que apresente no final o somatório dos valores pares existentes na faixa de 1 até 500.

soma = 0

for contadora in range(1, 501):
    if contadora % 2 == 0:
        soma += contadora
print("A soma dos valores pares entre os números 1 e 500 é: ", soma)