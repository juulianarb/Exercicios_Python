# Curso básico de python
# Nome do desenvolvedor: Juliana Rodrigues Brito
# Versão 1.0
# Exercício de Lógica de programação com a linguagem python

#  Ler quatro valores referentes a quatro notas escolares de um aluno e imprimir uma mensagem dizendo que o aluno foi aprovado,
# se o valor da média escolar for maior ou igual a 5. Se o aluno não foi aprovado, indicar uma mensagem informando esta condição.
# Apresentar junto das mensagens o valor da média do aluno para qualquer condição.

primeiraNota = float(input("Digite a primeira nota para saber se foi aprovado: "))
segundaNota = float(input("Digite a segunda nota para saber se foi aprovado: "))
terceiraNota = float(input("Digite a terceira nota para saber se foi aprovado: "))
quartaNota = float(input("Digite a quarta nota para saber se foi aprovado: "))

media = ((primeiraNota + segundaNota + terceiraNota + quartaNota) / 4)

if media >= 5: 
    print("O aluno(a) foi aprovado! A média dele foi de: " , round(media, 1))
else:
    print("O aluno(a) não foi aprovado! A média dele foi de: " , round(media, 1))