# Curso básico de python
# Nome do desenvolvedor: Juliana Rodrigues Brito
# Versão 1.0
# Exercício de Lógica de programação com a linguagem python

# Elaborar um programa que apresente os valores de conversão de graus Celsius em Fahrenheit, de 10 em 10 graus,
#  iniciando a contagem em 10 graus Celsius e finalizando em 100 graus Celsius. O programa deve apresentar os valores das duas temperaturas.
#  A fórmula de conversão F = (9C +160)/5, sendo F a temperatura em Fahrenheit e C a temperatura em Celsius.

def celsiusParaFahrenheit(celsius):
    fahrenheit = (9 * celsius + 160) / 5
    return fahrenheit

celsius = 10
while celsius <= 100:
    fahrenheit = celsiusParaFahrenheit(celsius)
    print(f'{celsius} graus Celsius equivalem a {fahrenheit:.2f} graus Fahrenheit')
    celsius += 10
