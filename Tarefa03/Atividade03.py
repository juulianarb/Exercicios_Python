# Curso básico de python
# Nome do desenvolvedor: Juliana Rodrigues Brito
# Versão 1.0
# Exercício de Lógica de programação com a linguagem python

# Faça um programa que pergunte ao usuário o valor do produto e o percentual de desconto, e retorne o valor final após o desconto.

valorDoProduto = float(input("Digite o valor do produto, para saber o valor final com o desconto: "))
percentualDeDesconto = float(input("Digite o percentual de desconto: "))

valorFinal = valorDoProduto - (valorDoProduto * (percentualDeDesconto / 100))

print("O valor final do produto é de: R$" , valorFinal)