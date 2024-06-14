# Curso básico de python
# Nome do desenvolvedor: Juliana Rodrigues Brito
# Versão 1.0
# Exercício de Lógica de programação com a linguagem python

# Escreva um programa que leia o código de um produto e informe a sua categoria:
# 1 a 10: Alimento não-perecível
# 11 a 20: Alimento perecível
# 21 a 30: Vestuário
# 31 a 40: Eletrônicos
# Outros: Código inválido

codigoProduto = int(input("Digite o número do código do produto para saber a sua categoria:"))

if codigoProduto > 0 and codigoProduto < 11:
    print("Alimento não-perecível")
elif codigoProduto >= 11 and codigoProduto < 21:
    print("Alimento perecível")
elif codigoProduto >= 21 and codigoProduto < 31:
    print("Vestuário")
elif codigoProduto >= 31 and codigoProduto < 41:
    print("Eletrônicos")
else:
    print("Código inválido")
    