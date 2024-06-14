# Curso básico de python
# Nome do desenvolvedor: Juliana Rodrigues Brito
# Versão 1.0
# Exercício de Lógica de programação com a linguagem python

# Escreva um programa que leia a idade de uma pessoa e informe se ela é uma criança (0-12 anos), 
# adolescente (13-17 anos),
# adulto (18-59 anos) ou idoso (60 anos ou mais).

idade = int(input("Digite a sua idade para saber se é criança, adolescente, adulto ou idoso: "))

if idade < 0:
    print("Digite uma idade válida")
elif idade <= 12:
    print("Você é uma criança!")
elif idade <= 17:
    print("Você é um adolescente!")
elif idade <= 59:
    print("Você é um adulto")
else:
    print("Você é um idoso!")
