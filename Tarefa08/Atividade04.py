# Curso básico de python
# Nome do desenvolvedor: Juliana Rodrigues Brito
# Versão 1.0
# Exercício de Lógica de programação com a linguagem python

# Apresentar todos os números divisíveis por 4 que sejam menores que 200. 
# Para verificar se o número é divisível por 4, efetuar dentro da malha a verificação lógica desta condição com a instrução se,
#  perguntando se o número é divisível; sendo, mostre-o; não sendo, passe para o próximo passo. 
# A variável que controlará o contador deve ser iniciada com o valor 1.

contador = 1

while contador < 200:
    if contador % 4 == 0:
        print(contador)
    contador += 1