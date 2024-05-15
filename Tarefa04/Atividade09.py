# Curso básico de python
# Nome do desenvolvedor: Juliana Rodrigues Brito
# Versão 1.0
# Exercício de Lógica de programação com a linguagem python

#   As maçãs custam R$ 1,30 cada se forem compradas menos de uma dúzia, e R$ 1,00 se forem compradas pelo menos 12.
# Escreva um programa que leia o número de maçãs compradas, calcule e escreva o custo total da compra.

macasCompradas = int(input("Digite o número de maçãs compradas, para saber o custo total da compra: "))

if macasCompradas < 12:
    totalMacas = macasCompradas * 1.30
    print("O custo total da compra de maças é de: R$" , round(totalMacas,2))
else:
    totalMacas = macasCompradas * 1.00
    print("Você obteu um desconto! O custo total da compra de maças é de: R$" , round(totalMacas,2))
          