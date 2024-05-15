# Curso básico de python
# Nome do desenvolvedor: Juliana Rodrigues Brito
# Versão 1.0
# Exercício de Lógica de programação com a linguagem python

# Escreva um programa que peça ao usuário para digitar uma frase e conte quantas vogais (a, e, i, o, u) ela possui.

def contadorDevogais(frase):
    vogais = "aeiouAEIOU" 
    contagem = 0
    for letra in frase:
        if letra in vogais:
            contagem += 1
    return contagem

frase = input("Digite uma frase: ")

totalDevogais = contadorDevogais(frase)

print(f"A frase possui {totalDevogais} vogais.")