# Curso básico de python
# Nome do desenvolvedor: Juliana Rodrigues Brito
# Versão 1.0
# Exercício de Lógica de programação com a linguagem python

# Escreva um programa que leia o peso e a altura de uma pessoa, calcule o IMC e informe a categoria:

# Abaixo do peso: IMC < 18.5
# Peso normal: 18.5 <= IMC < 24.9
# Sobrepeso: 25 <= IMC < 29.9
# Obesidade grau I: 30 <= IMC < 34.9
# Obesidade grau II: 35 <= IMC < 39.9
# Obesidade grau III: IMC >= 40

peso = float(input("Digite o seu peso em kg: "))
altura = float(input("Digite a sua altura: "))

imc = peso / (altura ** 2)

if imc < 18.5:
    print("Abaixo do peso")
elif 18.5 <= imc < 24.9:
    print("Peso normal")
elif 25 <= imc < 29.9:
    print("Sobrepeso")
elif 30 <= imc < 34.9:
    print("Obesidade grau I")
elif 35 <= imc < 39.9:
    print("Obesidade grau II")
else:
    print("Obesidade grau III")

