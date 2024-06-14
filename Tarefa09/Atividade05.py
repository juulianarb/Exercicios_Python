# Curso básico de python
# Nome do desenvolvedor: Juliana Rodrigues Brito
# Versão 1.0
# Exercício de Lógica de programação com a linguagem python

# Escreva um programa que leia três notas de um aluno e calcule a média.
# Informe se o aluno está aprovado (média >= 7), em recuperação (5 <= média < 7) ou reprovado (média < 5).

primeiraNota = float(input("Digite o valor da primeira nota do aluno(a) para calcular a média:"))
segundaNota = float(input("Digite o valor da segunda nota do aluno(a) para calcular a média:"))
terceiraNota = float(input("Digite o valor da terceira nota do aluno(a) para calcular a média:"))

media = ((primeiraNota + segundaNota + terceiraNota) / 3)

if media >= 7:
    print(f"A média do aluno foi de {round(media,1)} , o aluno(a) foi aprovado!")
elif media >= 5:
    print(f"A média do aluno foi de {round(media,1)} , o aluno(a) está em recuperação!")
else:
    print(f"A média do aluno foi de {round(media,1)} , o aluno(a) foi reprovado!")