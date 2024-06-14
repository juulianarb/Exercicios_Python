# Curso básico de python
# Nome do desenvolvedor: Juliana Rodrigues Brito
# Versão 1.0
# Exercício de Lógica de programação com a linguagem python

# Escreva um programa que leia um ano e verifique se ele é bissexto.
# Um ano é bissexto se for divisível por 4, mas não por 100, exceto se for divisível por 400.

ano = int(input("Digite o ano para saber se é bissexto: "))

if (ano % 4 == 0 and ano % 100 != 0) or ano % 400 == 0:
    print(f"O ano informado {ano}, é bissexto.")
else:
    print(f"O ano informado {ano}, não é bissexto.")