# Curso básico de python
# Nome do desenvolvedor: Juliana Rodrigues Brito
# Versão 1.0
# Exercício de Lógica de programação com a linguagem python

# Exercício que calcula a área do círculo

import math

raio = float(input("Digite o valor do raio do círculo, para calcular a área:"))

area = math.pi * pow(raio, 2)

print(f"A área do círculo é de {area: .2f} mt²")