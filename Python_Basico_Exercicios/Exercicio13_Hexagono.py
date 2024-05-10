# Curso básico de python
# Nome do desenvolvedor: Juliana Rodrigues Brito
# Versão 1.0
# Exercício de Lógica de programação com a linguagem python

# Exercício que calcula a área de um hexagono

import math

lado = float(input("Digite o tamanho do lado do hexágono para calcular sua área:"))

area = (3 * math.sqrt(3) * lado ** 2) / 2

print(f"A área do hexágono é de {area: .2f} mt²")