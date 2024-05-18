# Curso básico de python
# Nome do desenvolvedor: Juliana Rodrigues Brito
# Versão 1.0
# Exercício de Lógica de programação com a linguagem python

#   Escreva um algoritmo para ler uma temperatura em graus Fahrenheit, calcular e escrever o valor correspondente em graus Celsius (baseado na fórmula abaixo):
#   C= (F - 32)*5/9
#   Observação: Para testar se a sua resposta está correta saiba que 100oC = 212F

tempFahrenheit = int(input("Digite a temperatura em fahrenheit para converter em grau celcius: "))

celcius = (tempFahrenheit - 32) * 5/9

print("A temperatura " , tempFahrenheit , "ºF em graus celcius é de: ", celcius, "ºC")