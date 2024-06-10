# Curso básico de python
# Nome do desenvolvedor: Juliana Rodrigues Brito
# Versão 1.0
# Exercício de Lógica de programação com a linguagem python

# Ler quatro valores referentes a quatro notas escolares de um aluno e imprimir uma mensagem dizendo que o aluno foi aprovado, 
# se o valor da média escolar for maior ou igual a 7. Se o valor da média for menor que 7, solicitar a nota de exame, somar com o valor da média e obter nova média.
# Se a nova média for maior ou igual a 5, apresentar uma mensagem dizendo que o aluno foi aprovado em exame.
# Se o aluno não foi aprovado, indicar uma mensagem informando esta condição.
# Apresentar com as mensagens o valor da média do aluno, para qualquer condição.

primeiraNota = float(input("Digite a primeira nota para saber se foi aprovado: "))
segundaNota = float(input("Digite a segunda nota para saber se foi aprovado: "))
terceiraNota = float(input("Digite a terceira nota para saber se foi aprovado: "))
quartaNota = float(input("Digite a quarta nota para saber se foi aprovado: "))

media = ((primeiraNota + segundaNota + terceiraNota + quartaNota) / 4)
notaExame = 0
novaNota = notaExame + media

if media >= 7:
    print("O aluno(a) foi aprovado! A média dele foi de: " , round(media, 1))
elif media < 7:
    solicitarNotaExame = float(input("Digite a nota de exame para saber se foi aprovado:"))
    novaNota = notaExame + media

    if novaNota >= 5:
        print("O aluno(a) foi aprovado em exame.\n A média do aluno foi de: ", novaNota)
    else:
        print("O aluno(a) não foi aprovado em exame, pois, a nova nota foi abaixo de 5.\n A média do aluno foi de: ", novaNota) 