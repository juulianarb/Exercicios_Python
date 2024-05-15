# Curso básico de python
# Nome do desenvolvedor: Juliana Rodrigues Brito
# Versão 1.0
# Exercício de Lógica de programação com a linguagem python

# )Crie um programa que pergunte ao usuário a quantidade de dias, horas, minutos e segundos, e calcule o total em segundos.

dias = int(input("Digite a quantidade de dias: "))
horas = int(input("Digite a quantidade de horas: "))
minutos = int(input("Digite a quantidade de minutos: "))
segundos = int(input("Digite a quantidade de segundos: "))

totalEmSegundos = (dias * 24 * 3600) + (horas * 3600) + (minutos * 60) + segundos

print(f"O total em segundos é: {totalEmSegundos}")