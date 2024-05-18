# Curso básico de python
# Nome do desenvolvedor: Juliana Rodrigues Brito
# Versão 1.0
# Exercício de Lógica de programação com a linguagem python

#  Ler as notas da 1a. e 2a. avaliações de um aluno. Calcular a média aritmética simples e escrever uma mensagem que diga se o aluno foi ou não aprovado (considerar que nota igual ou maior que 6 o aluno é aprovado). Escrever também a média calculada.

primeiraAvaliacao = float(input("Digite o valor da primeira nota, para saber se foi aprovado: "))
segundaAvaliacao = float(input("Digite o valor da segunda nota, para saber se foi aprovado: "))

media = ((primeiraAvaliacao + segundaAvaliacao) / 2)

if media >= 6:    
    print("A média do aluno(a) foi de: ", round(media,1) , ", O aluno foi aprovado!")
else:   
    print("A média do aluno(a) foi de: ", round(media,1) , ", O aluno não foi aprovado!")