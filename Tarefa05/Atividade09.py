# Curso básico de python
# Nome do desenvolvedor: Juliana Rodrigues Brito
# Versão 1.0
# Exercício de Lógica de programação com a linguagem python

#  Ler o ano atual e o ano de nascimento de uma pessoa. Escrever uma mensagem que diga se ela poderá ou não votar este ano (não é necessário considerar o mês em que a pessoa nasceu).

anoAtual = int(input("Digite o ano atual: "))
anoNascimento = int(input("Digite o ano de seu nascimento, para saber se poderá votar:"))

idade = anoAtual - anoNascimento

if idade > 18:
    print("Poderá votar este ano!")
else:
    print("Não pode votar este ano!")