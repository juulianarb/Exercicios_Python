# Curso básico de python
# Nome do desenvolvedor: Juliana Rodrigues Brito
# Versão 1.0
# Exercício de Lógica de programação com a linguagem python

# Faça um programa que receba três notas de um aluno e calcule sua média.

primeiraNota = float(input("Digite o valor da primeira nota, para calcular a sua média: "))
segundaNota = float(input("Digite o valor da segunda nota, para calcular a sua média: "))
terceiraNota = float(input("Digite o valor da terceira nota, para calcular a sua média: "))

media = ((primeiraNota + segundaNota + terceiraNota) / 3)

print("A média do aluno(a) é de: " , round(media, 1))