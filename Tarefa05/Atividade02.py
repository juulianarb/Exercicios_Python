# Curso básico de python
# Nome do desenvolvedor: Juliana Rodrigues Brito
# Versão 1.0
# Exercício de Lógica de programação com a linguagem python

#  Escreva um algoritmo para ler o salário mensal atual de um funcionário e o percentual de reajuste. Calcular e escrever o valor do novo salário.

salarioMensalAtual = float(input("Digite o valor do salário atual do funcionário, para calcular o reajuste: "))
percentualDoReajuste = float(input("Digite o valor do percentual de reajuste: "))

valorFinalSalario = salarioMensalAtual + (salarioMensalAtual * (percentualDoReajuste / 100))

print("O novo valor do salário do funcionário é de: R$" , valorFinalSalario)