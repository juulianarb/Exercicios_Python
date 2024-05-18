# Curso básico de python
# Nome do desenvolvedor: Juliana Rodrigues Brito
# Versão 1.0
# Exercício de Lógica de programação com a linguagem python

# Faça um algoritmo que leia três notas de um aluno, calcule e escreva a média final deste aluno.
# Considerar que a média é ponderada e que o peso das notas é 2, 3 e 5. Fórmula para o cálculo da média final é:
# mediafinal =(n1 * 2 + n2 * 3 + n3 * 5)/10

primeiraNota = float(input("Digite a primeira nota do aluno(a), para calcular a média ponderada: "))
segundaNota = float(input("Digite a segunda nota do aluno(a), para calcular a média ponderada: "))
terceiraNota = float(input("Digite a terceira nota do aluno(a), para calcular a média ponderada: "))

mediaFinal = (primeiraNota * 2 + segundaNota * 3 + terceiraNota * 5) / 10

print("A média ponderada do aluno(a) é de: " , round(mediaFinal,1))
