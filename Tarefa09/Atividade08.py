# Curso básico de python
# Nome do desenvolvedor: Juliana Rodrigues Brito
# Versão 1.0
# Exercício de Lógica de programação com a linguagem python

# Escreva um programa que leia a nota de um aluno e converta-a para conceito:
# A (nota >= 9), B (7 <= nota < 9), C (5 <= nota < 7), D (3 <= nota < 5) e F (nota < 3).

nota = int(input("Digite o valor da nota do aluno(a) para visualizar o conceito:"))

if nota >= 9:
    print("A")
elif nota >= 7:
    print("B")
elif nota >= 5:
    print("C")
elif nota >= 3:
    print("D")
else:
    print("F")