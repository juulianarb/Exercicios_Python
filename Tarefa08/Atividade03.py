# Curso básico de python
# Nome do desenvolvedor: Juliana Rodrigues Brito
# Versão 1.0
# Exercício de Lógica de programação com a linguagem python

# Apresentar todos os valores numéricos inteiros ímpares situados na faixa de 0 a 20.
#  Para verificar se o número é ímpar, efetuar dentro da malha a verificação lógica desta condição com a instrução se,
#  perguntando se o número é ímpar; sendo, mostre-o; não sendo, passe para o próximo passo.

for contadora in range(21):
    if contadora % 2 != 0:
        print(contadora)


