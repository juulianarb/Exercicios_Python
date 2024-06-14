# Curso básico de python
# Nome do desenvolvedor: Juliana Rodrigues Brito
# Versão 1.0
# Exercício de Lógica de programação com a linguagem python

# Escreva um programa que leia o valor de uma compra e a categoria do cliente (1 para comum, 2 para associado e 3 para VIP).
# Aplique os seguintes descontos:

# Comum: Sem desconto
# Associado: 10% de desconto
# VIP: 20% de desconto
# Informe o valor final da compra.

valorDaCompra = float(input("Digite o valor da compra:"))
categoria = int(input("Digite o número da categoria da compra (1 - comum, 2 - associado, 3 - VIP):"))

if categoria == 1:
    print(f"Comum: Sem desconto \n O valor da compra é de: R${valorDaCompra}")
elif categoria == 2:
    valorFinal = valorDaCompra - (valorDaCompra * 0.1)
    print(f"Associado: 10% de desconto \n O valor da compra é de: R${valorFinal}")
elif categoria == 3:
    valorFinal = valorDaCompra - (valorDaCompra * 0.2)
    print(f"VIP: 20% de desconto \n O valor da compra é de: R${valorFinal}")
else:
    print("Categoria inválida")