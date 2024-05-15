# Curso básico de python
# Nome do desenvolvedor: Juliana Rodrigues Brito
# Versão 1.0
# Exercício de Lógica de programação com a linguagem python

# Crie um programa que solicite ao usuário sua altura e peso, e calcule seu índice de massa corporal (IMC).

altura = float(input("Informe a sua altura, para calcular o IMC: "))
peso = int(input("Informe o seu peso, para calcular o IMC: "))

imc = peso / (pow(altura,2))

if imc < 16.9:
    print("Seu imc é de: " , round(imc,2) , " ,Muito abaixo do peso")
elif imc < 17:
    print("Seu imc é de: " , round(imc,2) ," ,Abaixo do peso")
elif imc < 18.5:
    print("Seu imc é de: " , round(imc,2) ," ,Peso normal")
elif imc < 25:
    print("Seu imc é de: " , round(imc,2) ," ,Acima do peso")
elif imc < 30:
    print("Seu imc é de: " , round(imc,2) ," ,Obesidade grau I")
elif imc < 35:
    print("Seu imc é de: " , round(imc,2) ," ,Obesidade grau II")
else:
    print("Seu imc é de: " , round(imc,2) ," ,Obesidade grau 3")
